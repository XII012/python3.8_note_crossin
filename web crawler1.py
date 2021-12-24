import requests
from bs4 import BeautifulSoup

# 'https://qiushibaike.com/text/page/{}'




def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


def get_content(html, page):
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n"""
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find('div', class_='col1 old-style-col1')
    con_list = con.find_all('div', class_='article')
    count = 0
    for i in con_list:
        count += 1
        author = i.find('div', class_='author').find('h2').text
        author_info = i.find('div', class_='articleGender')
        if author_info:
            class_list = author_info['class']
            if 'manIcon' in class_list:
                gender = '男'
            elif 'womenIcon' in class_list:
                gender = '女'
            else:
                gender = ''
            age = author_info.text
        else:
            gender = ''
            age = ''
        content = i.find('div', class_='content').get_text()
        stats = i.find('div', class_='stats')
        stats_vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        stats_comments = stats.find('span', class_='stats-comments').find('i', class_='number').string
        if count == 1:
            print(author, '\n', author_info)
            print(con_list)

        save_txt(output.format(page, author, gender, age, stats_vote, stats_comments, content))


def save_txt(text):
    with open('qiubai.txt', 'a', encoding='utf-8') as f:
        f.write(text)


def main():
    for i in range(1,2):
        url = 'https://qiushibaike.com/text/page/%s' % i
        html = download_page(url)
        get_content(html, i)

if __name__ == '__main__':
    main()





