import requests, time, threading, os
from bs4 import BeautifulSoup
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
# download_url
'''可以用来下载model一个album的所有图片
测试得知，16.2月上传album亦可用'''


def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


# get_pic_list
def get_pic_list(html1):
    soup1 = BeautifulSoup(html1, 'html.parser')
    pic = soup1.find('ul', id='hgallery')
    if pic:
        pic_list = pic.find_all('img')
        return pic_list
    else:
        print('quit')
        quit()


def download_pic(pic_list):
    for i in pic_list:
        link = i.get('src')
        text = i.get('alt')
        name1 = text.split('_')
        name2 = 'pic/' + name1[0]
        create_file(name2)
        link2 = link.replace('/s/', '/')
        # 得到图片地址
        print(text)
        print(link2)
        img = requests.get(link2)
        # 下载图片
        with open('%s/%s' % (name2, text + '.jpg'), 'wb') as f:
            f.write(img.content)
            # 保存图片
            time.sleep(1)


def create_file(name):
    if not os.path.exists(name):
        os.makedirs(name)


def execute(url):
    html1 = download_page(url)
    pic_list = get_pic_list(html1)
    download_pic(pic_list)


def main1():
    queue = [i for i in range(1, 55)]
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0:
            cur_page = queue.pop(0)
            url = 'https://www.nvshens.net/g/%s/%s.html' % (32996, cur_page)
            thread = threading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('%s正在下载%s页' % (threading.current_thread().name, cur_page))
            threads.append(thread)
            if cur_page == 1:
                time.sleep(1)


if __name__ == '__main__':
    s1 = time.time()
    main1()
    s2 = time.time()
    print(s2-s1)
