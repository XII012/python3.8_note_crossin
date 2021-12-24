import requests
from bs4 import BeautifulSoup

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers = headers)
    # 得到一个requests.models.Response
    return r.text
    # 得到一个str


def get_content(html, page):
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n"""
    soup = BeautifulSoup(html, 'html.parser')
    # 解析str为xml得到一个(类str)bs4.BeautifulSoup
    con = soup.find('div', class_='col1')
    # 得到一个find结果→(类str)bs4.element.Tag
    con_list = con.find_all('div', class_='article')
    # 得到一个find_all结果→(类list)bs4.element.ResultSet
    for i in con_list:
        author = i.find('h2').string
        content = i.find('div', class_='content').find('span').get_text()
        stats = i.find('div', class_='stats')
        vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
        author_info = i.find('div', class_='atricleGender')
        if author_info:
            class_list = author_info['class']
            if 'womenIcon' in class_list:
                gender = '女'
            elif 'manIcon' in class_list:
                gender = '男'
            else:
                gender = ''
            age = author_info.string
        else:
            gender = ''
            age = ''
        save_txt(output.format(page, author, gender, age, vote, comment, content))

def save_txt(text):
    with open('qiubai.txt','a', encoding='utf-8') as f:
        # 'a'表示append
        f.write(text)


def main():
    for i in range(1,2):
        url = 'https://qiushibaike.com/text/page/{}'.format(i)
        html = download_page(url)
        get_content(html, i)

if __name__ == '__main__':
    main()






















