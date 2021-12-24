import math
import random
import requests
import time
import os
import _thread
import threading
import string
from operator import *
from collections import *
from bs4 import BeautifulSoup
# 20200319
# 猜数字小游戏
zxc = True
if not zxc:
    from random import randint
    num = randint(1, 2)
    qwe = 0
    print('what is the number?')
while not zxc:
    qwe += 1
    asd = int(input())
    if asd > num:
        print('too big')
    if asd < num:
        print('too small')
    if asd == num:
        print('bingo!')
        print(str(qwe) + ' times')
        zxc = True

# 计算a到b所有数字的和
abc = False
if abc:
    a = int(input())
    b = int(input())
    c = 0
    for i in range(a, b + 1):
        c += i
        print(c)

# 等比数列
aq = False
if aq:
    a1 = int(input())
    q = int(input())
    for i in range(1, 11):
        print(a1)
        a1 = a1 * q

# 斐波那契数列(n>=3)
eg1 = False
if eg1:
    n = int(input())
    n1 = 1
    n2 = 1
    print('''1
1''')
    for i in range(1, n - 1):
        print(n1 + n2)
        n2 = n1 + n2
        n1 = n2 - n1

# 输出边长为n的等边三角形
eg2 = False
if eg2:
    n = int(input())
    for i in range(0, n):
        for a in range(0, n - 1 - i):
            print(' ', end='')
        for b in range(0, i + 1):
            print('*', end=' ')
        for c in range(0, n - 1 - i):
            print(' ', end='')
        print()

# 输出乘法口诀表(直角左下的三角形)
# %2d表示两位数，靠右排列
eg3 = False
if eg3:
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%2d' % (i, j, i * j), end=' ')
        print()

# 猜数字小游戏(函数版本)
eg4 = False


def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('bingo!!')
        return True


if eg4:
    from random import randint
    num = randint(1, 10)
    bingo = False
    while bingo == False:
        answer = int(input())
        bingo = isEqual(answer, num)

# 输入3个数，输出最大数
eg5 = False
if eg5:
    a1 = float(input())
    a2 = float(input())
    a3 = float(input())
    if a2 > a1 and a2 > a3:
        print(a2)
    elif a3 > a1 and a3 > a2:
        print(a3)
    else:
        print(a1)
eg6 = False
if eg6:
    a1 = float(input())
    a2 = float(input())
    a3 = float(input())
    print(max(a1, a2, a3))

# 输出从1000以内，用3、5、7去除，余数均为2的正整数。
eg7 = False
if eg7:
    for i in range(0, 100):
        x = 3 * 5 * 7 * i + 2
        if x <= 1000:
            print(x)

# 求所有不超过200的N值，N的平方是具有对称性质的回文数。所谓回文数就是将一个数从左向右与从右向左读是一样的，例如34543和1234321都是回文数。
eg8 = False
if eg8:
    for i in range(1, 201):
        x = i * i
        y = str(x)
        z = y[::-1]
        if z == y:
            print(i)

# 对猜数字小游戏添加成绩的显示和记录功能
eg9 = False
if eg9:
    # open
    with open('game_scores.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    # print(data)
    results = {}
    for i in data:
        a = i.split()
        results[a[0]] = a[1:]
    # print(results)
    # game
    print('请输入姓名')
    name = input()
    score = results.get(name)
    if score is None:
        score = [0, 0, 0]
    # print(score)
    game = int(score[0])
    win = int(score[1])
    total = int(score[2])
    if int(game) > 0:
        avg = total / game
    else:
        avg = 0
    print('%s，你总共玩了%s局，赢了%s局，平均每局花了%.2f轮' % (name, game, win, avg))
    print('what is the number?')
    game += 1
    from random import randint
    com = randint(1, 10)
    bingo = False
    while bingo == False:
        you = int(input())
        total += 1
        if you > com:
            print('too big')
        elif you < com:
            print('too small')
        else:
            print('bingo!!')
            win += 1
            bingo = True
    score = [str(game), str(win), str(total)]
    results[name] = score
    print(score, '\t', results)
    # write
    result = ''
    for i in results:
        result += i + ' ' + ' '.join(results.get(i)) + '\n'
    # print(result)
    with open('game_scores.txt', 'w', encoding='utf-8') as f:
        f.write(result)

# 43 查询天气(修改版)
# if后为True→执行语句；if not city中，not city为True时，即city为False时，执行语句
# python3中input输出为str;if not city中，city为str，当且仅当输入回车时，city==''→False，执行语句break
eg43 = False
if eg43:
    import requests
    while True:
        city = input('请输入城市，回车退出\n')
        if not city:
            print('已退出')
            break
        req = requests.get(
            'http://wthrcdn.etouch.cn/weather_mini?city=%s' %
            city)
        # 对req得到的数据进行.text处理，得到一个str，内容满足json格式
        # print(req.text)
        '''{"data": {"yesterday": {"date": "23日星期一",
                                "high": "高温 23℃",
                                "fx": "东南风",
                                "low": "低温 6℃",
                                "fl": "<![CDATA[3-4级]]>",
                                "type": "晴"},
                  "city": "北京",
                  "forecast": [{"date": "24日星期二",
                                "high": "高温 17℃",
                                "fengli": "<![CDATA[<3级]]>",
                                "low": "低温 5℃",
                                "fengxiang": "南风",
                                "type": "多云"},
                               {"date": "25日星期三",
                                "high": "高温 22℃",
                                "fengli": "<![CDATA[<3级]]>",
                                "low": "低温 9℃",
                                "fengxiang": "东南风",
                                "type": "多云"},
                               {"date": "26日星期四",
                                "high": "高温 10℃",
                                "fengli": "<![CDATA[4-5级]]>",
                                "low": "低温 4℃",
                                "fengxiang": "北风",
                                "type": "小雨"},
                               {"date": "27日星期五",
                                "high": "高温 13℃",
                                "fengli": "<![CDATA[3-4级]]>",
                                "low": "低温 2℃",
                                "fengxiang": "西北风",
                                "type": "晴"},
                               {"date": "28日星期六",
                                "high": "高温 14℃",
                                "fengli": "<![CDATA[<3级]]>",
                                "low": "低温 2℃",
                                "fengxiang": "南风",
                                "type": "晴"}],
                  "ganmao": "相对于今天将会出现大幅度降温，易发生感冒，请注意适当增加衣服，加强自我防护避免感冒。",
                  "wendu": "17"},
            "status": 1000,
            "desc": "OK"}'''
        # 传化成dict
        dict_city = req.json()
        # print(dict_city)
        city_data = dict_city.get('data')
        # print(city_data)
        if city_data:
            forecast_data = city_data.get('forecast')[0]
            # print(forecast_data)
            print(forecast_data.get('date'))
            print(forecast_data.get('high'))
            print(forecast_data.get('low'))
            print(forecast_data.get('fengxiang'))
            print(forecast_data.get('type'))
            break
        else:
            print('获取失败，请重试')

# 46 面向对象-计算不同speed车子对不同distance的time
eg46 = False
if eg46:
    class Vehicle:
        def __init__(self, speed):
            self.speed = speed

        def drive(self, distance):
            print('need %f hour(s)' % (distance / self.speed))

    class Bike(Vehicle):
        pass

    class Car(Vehicle):
        def __init__(self, speed, fuel):
            Vehicle.__init__(self, speed)
            self.fuel = fuel

        def drive(self, distance):
            Vehicle.drive(self, distance)
            print('expend %f litre(s)' % (distance / self.fuel))

    b = Bike(15)
    c = Car(80, 0.012)
    b.drive(100)
    c.drive(100)

# 每日一坑：替换文件中的敏感信息 -
# 假设我们有一份文件，文件中包含了很多个人信息。现在需要一份去除其中敏感信息的版本，将文件中所有手机号的4~7位和身份证号的6~15位用 *
# 替换。
eg50 = False
if eg50:
    with open('敏感文件.txt', 'r', encoding='utf-8') as f:
        data1 = f.readlines()
        print(data1)
    IDnum = 0
    Phonenum = 0
    for i in data1:
        if '身份证号' in i:
            i = i[:10] + '**********' + i[20:]
            data1[IDnum] = i
        IDnum += 1

    for i in data1:
        if '手机号' in i:
            i = i[:7] + '****' + i[11:]
            data1[Phonenum] = i
        Phonenum += 1
    data2 = ''
    for i in data1:
        data2 += i
    print(data2)
    with open('敏感文件_输出.txt', 'w', encoding='utf-8') as f:
        f.write(data2)

# 入门课程7-17 生成优惠券 - 26位英文字母大小写随机生成200个8位优惠券
eg10 = False
if eg10:
    results = []
    for i in range(20):
        str1 = ''.join(random.sample(string.ascii_letters, 8))
        results.append(str1)
    print(results)

# 入门课程7-18. 编程实例 - 三人斗地主手牌生成
eg11 = False
if eg11:
    jokers = ['red joker', 'black joker']
    suit = ['S', 'H', 'D', 'C']
    num = [i for i in range(1, 14)]
    card1 = [i + str(k) for i in suit for k in num]
    card1 += jokers
    random.shuffle(card1)
    print('player1:', card1[0:17], sep='')
    print('player2:', card1[17:34], sep='')
    print('player3:', card1[34:51], sep='')
    print('remain:', card1[51:], sep='')

# 入门课程8-11 屏蔽词替换
eg12 = False
if eg12:
    def get_blockwords(filename):
        with open(filename, encoding='utf-8') as f:
            f1 = [i.strip() for i in f.readlines() if i]
        return f1

    def replace_words(text, block, symbol='*'):
        for i in block:
            if i in text:
                text = text.replace(i, symbol * len(i))
        return text

    filename1 = 'blockwords.txt'
    block_list = get_blockwords(filename1)
    print(block_list)
    in1 = input()
    result = replace_words(in1, block_list)
    print(result)

# 入门课程8-12 查找文件
eg13 = True
if eg13:
    def find_key(keyword, path='.'):
        dirs = os.listdir(path)
        file_li = []
        for file in dirs:
            fullname = path + '/' + file
            print(fullname)
            if keyword in file:
                file_li.append(file)
            else:
                try:
                    with open(fullname, encoding='utf-8') as f:
                        for i in f:
                            if keyword in i:
                                file_li.append(file)
                                break
                except BaseException:
                    pass
        return file_li
    keyword = input('请输入关键字：')
    path = input('请输入路径(不填则默认为当前目录)：')
    if not path:
        path = '.'
    result = find_key(keyword, path)
    print(result)

# 入门课程8-12 查找文件-附加题(包括子目录)
# 在相对路径不能用(有不能解析的文件)，需要另外弄个文件，里面放文件夹和文本文件后再运行
eg14 = False
if eg14:
    def find_key(keyword, path):
        result = []
        for dir_i in os.walk(path):
            for dir_name in dir_i[1]:
                if keyword in dir_name:
                    result.append(dir_name)
            for file_name in dir_i[2]:
                full_name = dir_i[0] + '/' + file_name
                if keyword in file_name:
                    result.append(file_name)
                else:
                    with open(full_name, encoding='utf-8') as f:
                        for f1 in f:
                            if keyword in f1:
                                result.append(file_name)
        return result
    keyword = input('请输入关键字：')
    path = input('请输入路径(不填则默认为当前目录)：')
    if not path:
        path = '.'
    result = find_key(keyword, path)
    print(result)

# 入门课程9-3. 期中项目 - 统计成绩
# 读取raw成绩
eg15 = False
if eg15:
    with open('report.txt', encoding='utf-8') as f:
        score_rawli1 = f.readlines()
    print(score_rawli1)
    # 统计总分、平均分，并从高到低进行排序
    score_finli = [score_rawli1[0].split()]
    for i in score_rawli1[1:]:
        sum1 = 0
        score_personli = i.split()
        for j in score_personli[1:]:
            sum1 += int(j)
        avg1 = round(sum1 / 9, 1)
        score_personli.append(str(sum1))
        score_personli.append(str(avg1))
        score_finli.append(score_personli)
    score_finli = sorted(score_finli, key=lambda a: a[-1], reverse=True)
    print(score_finli)
    # 汇总每一科目的平均分和总平均分
    score_avgli = ['平均']
    sum3 = 0
    for i in range(len(score_finli[1]) - 3):
        avg2 = 0
        for j in score_finli[1:]:
            avg2 += int(j[i + 1])
        avg2 //= len(score_finli[1:])
        sum3 += avg2
        score_avgli.append(str(avg2))
    avg3 = round(sum3 / 9, 1)
    score_avgli.append(str(sum3))
    score_avgli.append(str(avg3))
    score_finli.insert(1, score_avgli)
    # 添加名次，替换不及格（平均分不替换）
    score_finli[0].insert(0, '名次')
    ranking = 0
    for i in score_finli[1:]:
        for j in range(1, 10):
            if float(i[j]) < 60:
                i[j] = '不及格'
        i.insert(0, str(ranking))
        ranking += 1
    # 存为一个新文件(result.txt)
    score_finli = [' '.join(i) + '\n' for i in score_finli]
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.writelines(score_finli)

# 入门课程12-1. 期末项目 - 高级猜数字
# 找成绩记录文件并提取数据
eg16 = False
if eg16:
    try:
        with open('game_scores.txt', 'r+', encoding='utf-8') as f:
            raw_data = f.readlines()
    except BaseException:
        with open('game_scores.txt', 'w', encoding='utf-8') as f:
            raw_data = f.readlines()
    # 建立dict，并提示即将开始game
    result = {}
    for i in raw_data:
        a = i.split()
        result[a[0]] = a[1:]
    print(result)
    name = input('请输入你的名字：')
    try:
        record = [int(i) for i in result.get(name)]
        avg = record[2] / record[0]
    except BaseException:
        record = [0, 0, 0]
        avg = 0.00
    print('%s，你已经玩了%s次，最少%s轮猜出答案，平均%.2f轮猜出答案，开始游戏！' %
          (name, record[0], record[1], avg))
    # game过程
    game_start = True
    while game_start:
        req = requests.get('https://python666.cn/cls/number/guess/')
        num_computer = int(req.text)
        print(num_computer)
        bingo = True
        rounds = 0
        while bingo:
            try:
                num_player = int(input('请猜一个1-100的数字：'))
                rounds += 1
                if num_player > num_computer:
                    print('猜大了，再试试')
                elif num_player < num_computer:
                    print('猜小了，再试试')
                else:
                    print('猜对了，你一共猜了%d轮' % rounds)
                    bingo = False
                    game_start = False
                    # 清算本轮游戏数据
                    record[0] += 1
                    record[2] += rounds
                    if record[1] == 0:
                        record[1] = rounds
                    elif record[1] >= rounds:
                        record[1] = rounds
                    rounds = 0
                    choice = input('是否继续游戏？（输入y继续，其他退出）')
                    if choice == 'y':
                        game_start = True
                    else:
                        print('退出游戏，欢迎下次再来！\n')
            except Exception as e:
                print(e)
                print('输入错误，请输入有效值')
    # 写入成绩
    record_str = [str(i) for i in record]
    result[name] = record_str
    li_result = [' '.join([i] + j) + '\n' for i, j in result.items()]
    print(li_result)
    with open('game_scores.txt', 'w', encoding='utf-8') as f:
        f.writelines(li_result)
