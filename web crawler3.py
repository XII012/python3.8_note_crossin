import requests, time, threading, os
from bs4 import BeautifulSoup
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
# download_url
'''可以用来下载manhwa18.com上manga某一chapter的所有图片'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
    'Host': 'axwxrnk5ydzy.com',
    'Referer': 'https://manhwa18.com/manga-list.html?listType=pagination&page=1&artist=&author=&group=&m_status=&name=&genre=&ungenre=&sort=last_update&sort_type=DESC',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

}


def download_page(url):
    r = requests.get(url, headers=headers)
    print(r)
    return r.text


# get_pic_list
def get_pic_list(html1):
    soup1 = BeautifulSoup(html1, 'html.parser')
    pic_list = soup1.find_all('img', class_="_lazy chapter-img")
    print(pic_list)
    return pic_list


def download_pic(num1, i):
    link = i.get('src').strip()
    text = i.get('alt')
    name2 = 'pic/manga/' + text
    create_file(name2)
    # 得到图片地址
    img = requests.get(link, headers=headers)
    # 下载图片
    with open('%s/%s' % (name2, '%02d.jpg' % num1), 'wb') as f:
        f.write(img.content)
        # 保存图片


def create_file(name):
    if not os.path.exists(name):
        os.makedirs(name)


def execute():
    for i in range(119, 124):
        url = "https://manhwa18.com/read-her-4-incher-raw-chapter-%d.html" % i
        html1 = download_page(url)
        pic_list = get_pic_list(html1)
        queue = list(enumerate(pic_list, start=1))
        threads = []
        while len(queue) > 0:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < 5 and len(queue) > 0:
                cur_page = queue.pop(0)
                thread = threading.Thread(target=download_pic, args=cur_page)
                thread.setDaemon(True)
                thread.start()
                print('%s正在下载%s页' % (threading.current_thread().name, cur_page[0]))
                threads.append(thread)
                if cur_page[0] == 1:
                    time.sleep(1)


if __name__ == '__main__':
    s1 = time.time()
    execute()
    s2 = time.time()
    print(s2-s1)
