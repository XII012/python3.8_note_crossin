import requests, time, threading, os
from bs4 import BeautifulSoup

# https://www.nvshens.net/girl/22162/album/1.html
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
'''2的改进版，可以对一名模特进行所有album图片的下载
测试得知，16.2月上传album亦可用
测试穆菲菲，31部全部下载无遗漏无error(每部图片不确定)，平均每部47s，平均一页(30部)23min
'''


def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    # 得到一个requests.models.Response
    return r.text
# 得到一个str


def main0(url):
    html1 = download_page(url)
    soup1 = BeautifulSoup(html1, 'html.parser')
    # 解析str为xml得到一个(类str)bs4.BeautifulSoup
    post = soup1.find('ul', class_='photo_ul')
    # 得到一个find结果→(类str)bs4.element.Tag
    if post:
        post_list = post.find_all('li', class_='igalleryli')
        # 得到一个find_all结果→(类list)bs4.element.ResultSet
        for i in post_list:
            name = i.find('a', class_='caption').text
            link_name = i.find('a', class_='caption').get('href')
            print(name, link_name)
            main1(link_name)
    else:
        pass



# get_pic_list
def get_pic_list(html1):
    soup1 = BeautifulSoup(html1, 'html.parser')
    pic = soup1.find('ul', id='hgallery')
    if pic:
        pic_list = pic.find_all('img')
        return pic_list
    else:
        quit()


def download_pic(pic_list):
    for i in pic_list:
        link = i.get('src')
        text = i.get('alt')
        name1 = text.split('_')
        name2 = 'pic/' + name1[0]
        create_file(name2)
        link2 = link.replace('/s/', '/')
        print(text)
        img = requests.get(link2)
        with open('%s/%s' % (name2, text + '.jpg'), 'wb') as f:
            f.write(img.content)
            time.sleep(1)


def create_file(name):
    if not os.path.exists(name):
        os.makedirs(name)


def execute(url):
    html1 = download_page(url)
    pic_list = get_pic_list(html1)
    download_pic(pic_list)


def main1(link_name):
    queue = [i for i in range(1, 55)]
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0:
            cur_page = queue.pop(0)
            url = 'https://www.nvshens.net%s/%s.html' % (link_name, cur_page)
            thread = threading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('%s正在下载%s页' % (threading.current_thread().name, cur_page))
            threads.append(thread)
            if cur_page == 1:
                time.sleep(1)


if __name__ == '__main__':
    s3 = time.time()
    model_list = [18071, 23033, 18723, 20352, 24410, 21501, 22067, 25332, 20015, 19411, 22359, 24936, 16232]
    for num in model_list:
        for i in range(1, 15):
            s1 = time.time()
            url = 'https://www.nvshens.net/girl/{}/album/{}.html'.format(num, i)
            main0(url)
            s2 = time.time()
            print(s2 - s1)
        s4 = time.time()
        print(s4 - s3)
        time.sleep(num * 0.01)
