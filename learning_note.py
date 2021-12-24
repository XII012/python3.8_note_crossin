# 5 变量
import re
import random
from random import choice
from random import randint
import sys

a = True
a1 = 1 > 2
print(str(a) + str(a1))
print(a, a1, '2')

# 6 bool（布尔值）(T和F)
# 比较运算符
# <;>;<=;>=;==;!=
# not;or;and

# 7 if语句(勿忘冒号)
if a is True:
    print(1)

# 8 while语句(勿忘冒号)
while a:
    a = False

# 9 random 引入随机数模块
# from 模块名 import 方法名

# 产生随机整数[1,10]
num = randint(1, 10)

# 10 变量2
# 第一个字符必须是字母或者下划线_；之后可加个数字
# 变量名称对大小写敏感

# 12 for循环(勿忘冒号)
# 对i赋值[0,1)，总共循环10次
a2 = 1
for i in range(0, 10):
    a2 += 1
print(a2)

# 13-14，16 字符串(str)及其格式化
# ''和""均可
# 三引号最方便，适用最广
# \'→'，\"→"，\\→\;\t→tab,\n→enter回车
# str()传化成字符串
# %可用来字符串中进行替换；%d整数；%f小数；%.2f限定位数的小数；%s字符串
# (88,f,'\nover'))这种用()表示的一组数据在python中被称为元组（tuple），是python的一种基本数据结构
print(str(1 > 2) + ' + ' + str(1)
      + '\'same line\'\n' + '\tanother line\\')
f = 88.8888
print('''%d
oh%.3f
oh%s''' % (88, f, '\nover'))
# str的访问.str[a:b],区间范围为[a,b);zxc[::±d],±表从顺/逆序的第1位开始读取，d表步伐step
zxc = 'abcdefg'
print(zxc[0], zxc[1:-1], zxc[0:7], zxc[-2:], zxc[::-1], zxc[::-2])
if 'a' in zxc:
    print('a')
zxc += 'fedcba'
print(zxc)

# 15 循环的嵌套
# end 参数的作用是指定 print 结束之后的字符，默认是回车。
for i in range(0, 5):
    print('*', end='')
print()
for i in range(0, 5):
    for j in range(0, i + 1):
        print('*', end='')
        print(' ', end='')
    print()

# 17-18 类型转换
# python的几种最基本的数据类型的转换：
# int(x)     #把x转换成整数
# float(x)  #把x转换成浮点数
# str(x)     #把x转换成字符串
# bool(x)   #把x转换成bool值
print(
    type(f), type(1), type('1'), type(
        1 > 2), type(()), type(
        (1, a1, 6, '1', 1 > 2)), type(None))
print('hello' + '123',
      '\thello%d' % int('123'))
# bool的转换，以下数值会被认为是F，其他均为T：
# 为0的数字，包括0，0.0
# 空字符串，包括''，""
# 表示空值的 None
# 空集合，包括()，[]，{}
print(bool(False), bool(-0), bool(''), bool(None), bool(()),
      bool('abc'), bool('False'), bool(-123))
# 在 if、while 等条件判断语句里，判断条件会自动进行一次bool的转换，所以aa和aa!=''是常用写法
aa = 123
if aa:
    print(123)
if aa != '':
    print(123)
if aa:
    print(123)


# 20200321
# 19，21-22 函数
def sayhello():
    print('hello', end='')


sayhello(), sayhello(), sayhello(), print()


def plus(num1, num2):
    print(num1 + num2)


plus(2, 5)
# 看猜数字小游戏(函数版)

# 23 if,else,elif
# elif 意为 else if，含义就是：“否则如果”条件满足，就做yyy。
# if, elif, else 可组成一个整体的条件语句。
# 1、if 是必须有的；
# 2、elif 可以没有，也可以有很多个，每个elif条件不满足时会进入下一个elif判断；一旦满足，执行完就结束整个条件语句；
# 3、else 可以没有，如果有的话只能有一个，必须在条件语句的最后。

num = randint(1, 10)


def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    elif num1 > num2:
        print('too big')
        return False
    else:
        print('bingo!!')
        return True


bingo = True
while bingo == False:
    answer = int(input())
    bingo = isEqual(answer, num)

# 25-27 list
l = range(1, 10)
print(l[5], end=' '), print(l[1:5])
for i in l:
    print(i, end='')
# 定义用[]
ll = [1, 3.1415, 'a', True]
# 添加append,删除del,改变直接用等号
ll.append(21), ll.append(55)
del ll[5]
ll[4] = 12
# 访问，索引(index，[0])和切片(slice[:])
print('\n', ll, ll[:3], ll[3:], ll[1:-1],
      ll[:], ll[::-1], ll[::2], ll[0], ll[-1])
# 罚点球小游戏

direction = ['left', 'center', 'right']
score = [0, 0]


def game():
    print('=========== You Kick!!===========')
    print('''please choose the direction from 'left','right' and 'center' to make a shoot''')
    you = input()
    com = choice(direction)
    print('computer saved ' + com)
    if you != com:
        score[0] += 1
        print('goal!!')
    else:
        score[1] += 1
        print('oops..')
    print('you:computer=%d:%d' % (score[0], score[1]))

    print('=========== You Save!!===========')
    print('''please choose the direction from 'left','right' and 'center' to save''')
    you = input()
    com = choice(direction)
    print('computer shot ' + com)
    if you == com:
        score[0] += 1
        print('saved!!')
    else:
        score[1] += 1
        print('oops..')
    print('you:computer=%d:%d' % (score[0], score[1]))


ball_game = False
if ball_game:
    for i in range(0, 5):
        print('=========== Round%d ===========' % (i + 1))
        game()
    while score[0] == score[1]:
        i += 1
        print('=========== Round%d ===========' % (i + 1))
        game()
    print('=========== Game Over ===========')
    result = score[0] > score[1]
    if result:
        print('you win!!!')
    else:
        print('you lose.')

# 28-29 split字符切割str为list；join字符连接list为str
# split可将str切割成list；默认分割符号为空白符号，包括空格、\n、\t；也可以输入参数制定分割符号(但参数会被消去)
# split以str为对象，以分割符号为参数，输出list
sentence = 'Hi. I am a boy. Bye.'
aaa = 'aaa'
l1 = sentence.split()
l2 = sentence.split('.')
l3 = sentence.split('a')
l4 = aaa.split('a')
print(l1, l2, l3, '\n', l4)
print(l1 + l2 + l3 + l4)
# join以分割符号为对象，以list为参数，输出str
sen1 = ' '.join(l1)
sen2 = '.'.join(l2)
sen3 = 'a'.join(l4)
print(sen1, '\n' + sen2, sen3)

# 30 str和list的相似之处
# 遍历
for i in sentence:
    print(i, end='')
for i in l1:
    print(i, end=' ')
# 索引index和切片slice
print('\n', sentence[:-1], '\n', sentence[0], l1[:-1])
# join方法也可以对字符串使用，作用就是用连接符把字符串中的每个字符重新连接成一个新字符串。
sen4 = ' '.join(sen1)
print(sen4)

# 31 读文件
# 相对路径→默认path下的路径；绝对路径→所有路径
# f.read/readline/readlines，读取全部/一行为str/多行为list
# p.s.一次读完后，继续读也只能得到空集''；这个行为在定义变量时即生效
# r,read;w,write;r+,read&write;a,append
# i.strip()字符的作用为为删去\n;类似于end=''
f = open('test.txt', 'r')
data_f1 = f.readline()
data_f2 = f.readlines()
data_f = f.read()
print(data_f1, data_f1, data_f2, data_f)
f.close()
with open('test.txt', 'r+') as f:
    for i in f:
        print(i.strip())
20200330
# 32 写文件
# write接受一个str
with open('test.txt', 'r+') as f:
    f.write('change test1\n')
# writelines接受一个list
with open('test1.txt', 'w') as f:
    f.writelines(['change test1\n','test over'])


# 20200322
# 33 处理文件中的数据
# 编码ASCII:最一开始用，只包含英文数字部分字符
# 编码gbk：简体中文国标
# 编码Unicode：全世界语言都在里面，适用范围最广，运行时用之
# 编码UTF-8：能把unicode字符进行字节数调整，减少占用，存储或传输时用，
# write(string);writelines(list)
eg33 = True
if eg33:
    with open('scores.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    print(data)
    results = []
    for i in data:
        sum1 = 0
        data_s = i.split()
        scores = data_s[1:]
        for j in scores:
            sum1 += int(j)
        result = '%s\t:%d\n' % (data_s[0], sum1)
        results.append(result)
        print(result, end='')
    print(results)
    with open('output.txt', 'w') as f:
        f.writelines(results)

# 34-35 break%continue 语句
# break→彻底地跳出循环；continue→略过本次循环的余下内容，直接进入下一次循环。
# continue表示剩下无意义；break跳出循环得到结果。同时满足i>3且a3>1
for i in range(10):
    a3 = randint(0, 4)
    if i <= 3:
        continue
    if a3 > 1:
        print(i, a3)
        break

# 36 异常处理 try...except语句
eg36 = False
if eg36:
    try:
        print(int(input()))
    except BaseException:
        print('error!')
    print('done.', end='')

# 37 字典dictionary
# d（key是键，value是值） = {key1 : value1, key2 : value2}
# key是唯一的，value可重复
# key不能是list(可作value)，只能是简单对象，如字符串、整数、浮点数、bool值。
# 和list与tuple相比dict没有顺序，只能通过key读取value
# dict的新建，增加，修改，删除，遍历
d = {}
d[1] = 2
d[2.3] = 's'
d['a'] = 1 > 2
# key和value对3>99会转化为False保存读取
d[3 > 99] = [1, 2, 3, 6]
print(d)
d = {1: 2, 2.3: 's', 'a': False, False: [1, 2, 3, 6]}
print(d)
del d[1]
d[2.3] = 4
for i in d:
    print(i, ':', d[i])
# dict.get会输出None，而非报错
print(d.get(2.3), d.get(1))

# 39-41 对猜数字小游戏添加成绩的显示和记录功能
eg39 = False
if eg39:
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
    while bingo is False:
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


# 20200324
#  42 函数的默认参数
def hello(name1='world'):
    print('hello ' + name1)


hello()
hello('python')


# 当函数有多个参数，又只想提供默认参数时，默认参数应在最后
def plus(a, b=5):
    print(a + b)


plus(4)
plus(3, 9)

# 43-45 查天气
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
        {"data": {"yesterday": {"date": "23日星期一",
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
         "desc": "OK"}
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

# 20200325
# 46-49 面向对象
# 还有一种程序设计的方法，把数据和对数据的操作用一种叫做“对象”的东西包裹起来。这种被成为“面向对象”的编程。这种方法更适合较大型的程序开发。
# 面向对象编程最主要的两个概念就是：类（class）和对象（object）
# 类是一种抽象的类型，而对象是这种类型的实例(instance)。
# 类的属性包括方法(即类中的函数)和域(即类中的变量)
eg46 = False
if eg46:
    # 用pass语句，表示一个空的代码块。
    class MyClass:
        pass


    mc = MyClass()
    print(mc)


    class MyClass:
        name = 'sam'

        # 类的方法（函数）的第一个形参(parameter)最好是self，其表示类本身

        def sayHi(self):
            print('Hello %s' % self.name)


    # 类的实例化：此处对象mc指向MyClass()，为类的实例(instance)
    # 调用类变量要用对象.变量名
    mc = MyClass()
    print(mc.name, mc)
    mc.name = 'Lily'
    mc.sayHi()


    # 使用类：计算不同speed车子对不同distance的time

    class Car:
        speed = 0

        def drive(self, distance):
            time = distance / self.speed
            print(time)


    car = Car()
    car.speed = 60
    car.drive(100)
    car.drive(200)

    car.speed = 150
    car.drive(100)
    car.drive(200)


    # 基本类/超类(共有的属性)和子类/导出类(添加各自的属性)
    # __init__函数会在类被创建的时候自动调用，用来初始化类。它的参数，要在创建类的时候提供。于是我们通过提供一个数值来初始化speed的值。

    class Vehicle:
        # 令类变量sp为__init__中的输入值s
        def __init__(self, s):
            self.sp = s

        # 在方法中调用类变量用self.sp(对象.变量名)
        def drive(self, distance):
            print('need %f hor(s)' % (distance / self.sp))


    class Bike(Vehicle):
        pass


    class Car(Vehicle):
        def __init__(self, speed, fuel):
            Vehicle.__init__(self, speed)
            self.fuel = fuel

        def drive(self, distance):
            Vehicle.drive(self, distance)
            print('need %f fuels' % (distance * self.fuel))


    b = Bike(15)
    c = Car(80, 0.012)
    b.drive(100)
    c.drive(100)

# 50 and_or技巧
# 在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b。
b1 = randint(-1, 0)
if b1 >= 0:
    print('big')
else:
    print('small')
print((b1 >= 0) and 'big' or 'small')

# 20200327
# 51 元祖
# 元组中的元素在创建之后就不能被修改。
# 它有和list同样的索引index、切片slice、遍历等操作
post = (1, 2)
geeks = ('s', 'l', 'a', 's', 'h')
print(post[1])
for i in geeks:
    print(i, end='')
print(geeks[1:-1])
# ('Mike', 23)就是一个元组。这是元组最常见的用处。
print('%s is %d years old' % ('Mike', 23))


# 函数返回值元祖
def get_pos(n):
    return n + 1, n + 2


# ①根据返回值元祖中元素个数提供变量
x, y = get_pos(50)
print(x, y)
# ②用变量记录返回的元祖
pos50 = get_pos(50)
print(pos50[:])

# 52 数学运算
eg52 = False
if eg52:
    # python的数学运算模块叫做math，再用之前，你需要
    import math

    # math包里有两个常量：
    math.pi  # 圆周率π：3.141592...
    math.e  # 自然常数：2.718281...

    # 数值运算：
    math.ceil(x)
    # 对x向上取整，比如x=1.2，返回2.0（py3返回2）
    math.floor(x)
    # 对x向下取整，比如x=1.2，返回1.0（py3返回1）
    math.pow(x, y)
    # 指数运算，得到x的y次方
    math.log(x)
    # 对数，默认基底为e。可以使用第二个参数，来改变对数的基底。比如math.log(100, 10)
    math.sqrt(x)
    # 平方根(square root)
    math.fabs(x)
    # 绝对值(absolute)

    # 三角函数:
    math.sin(x)
    math.cos(x)
    math.tan(x)
    math.asin(x)
    math.acos(x)
    math.atan(x)
    # 注意：这里的x是以弧度为单位，所以计算角度的话，需要先换算

    # 角度和弧度互换:
    math.degrees(x)
    # 弧度转角度
    math.radians(x)


    # 角度转弧度
    # 一元二次方程的平方根公式

    def root1(a, b, c):
        sqrt1 = math.sqrt(b * b - 4 * a * c)
        x1 = (- b + sqrt1) / 2 * a
        x2 = (- b - sqrt1) / 2 * a
        print('x1=%.2f\tx2=%.2f' % (x1, x2))


    root1(5, 37, 13)


# 20200328
# 54-58 正则表达式(regular expression,RE,re)
# 正则表达式就是记录文本规则的代码。
# 默认情况下re是完全匹配，然后严格区分大小写的
# re是模块。findall是其中一个方法，用来按照提供的正则表达式，去匹配文本中的所有符合条件的字符串。返回结果是一个包含所有匹配的list。


def match1(x):
    text1 = "Hi, I am Shirley Hilton. I am his wife."
    m = re.findall(x, text1)
    if m:
        print(m)
    else:
        print('not match')


# r'hi'中的r表示raw，表示python对字符串不转义(python中用\进行转义,与re规则冲突)(\b会转义为backspace删除键，与re冲突)
# “\b”在re中表示单词的开头或结尾，空格、标点、换行都算是单词的分割。而“\b”自身又不会匹配任何字符，它代表的只是一个位置。
match1(r'hi')
match1(r'\bHi\b')
print('abc\b123')
# []表示满足括号中任一字符。比如“[hi]”，它就不是匹配“hi”了，而是匹配“h”或者“i”。“[Hh]i”，可以既匹配“Hi”，又匹配“hi”。
match1(r'[Hh]i')
# “.”在正则表达式中表示除换行符以外的任意字符。
match1(r'i.')
match1(r'.')
# “\S”，它表示的是任意不是空白符的字符。
match1(r'\Si')
# 在很多搜索中，会用“?”表示任意一个字符，“*”表示任意数量连续字符，这种被称为通配符。
# 但在re中，任意字符是用“.”表示。
# 而“*”则不是表示字符，而是表示数量：它表示前面的字符可以重复任意多次（包括0次），只要满足这条件，都会被匹配上。
# “*”在匹配时，会匹配尽可能长的结果———贪婪匹配
# “*?”在匹配时，会匹配尽可能短的结果———懒惰匹配
match1(r'I.*e')
match1(r'I.*?e')
# 匹配出所有s开头，e结尾的单词。
text2 = 'site sea sue sweet see case sse ssee loses'
ma = re.findall(r'\bs\S*?e\b', text2)
print(ma)
# [0-9]——表连续字符；类似的[a-z][A-Z]
# \d——表任一数字
# +——表重复1次以上(*是0次以上)
# {}——表限定长度(具体重复几次)
# 如找手机号码(一串11位，以1开头的数字。)
# 应用r'1\d{10}' or r'1[0-9]{10}'

# 我们已经了解了正则表达式中的一些特殊符号，如\b、\d、.、\S等等。这些具有特殊意义的专用字符被称作“元字符”。
# 常用的元字符还有：
# .——表\n外任意字符
# \b——表单词分割(即单词的开头或结尾)(空白符，标点)
# \s——匹配任意的空白符
# []——表括号中任意字符，如'Hh'I，则'Hi'或hi''
# [0-9]——表连续字符；类似的[a-z][A-Z]
# \d——表任一数字
# \w——匹配字母或数字或下划线或汉字（我试验下了，发现python 3.x版本可以匹配汉字，但2.x版本不可以）
# ^——匹配字符串的开始
# $——匹配字符串的结束
# |——表or，注意条件顺序。匹配时从左往右，一旦成功就停止。

# 反义：
# \S——\s的反义,任意不是空白符的字符。
# \W——\w的反义,匹配任意不是字母，数字，下划线，汉字的字符
# \D——\d的反义,匹配任意非数字的字符
# \B——\b的反义,匹配不是单词开头或结束的位置
# [a]的反义是[^a]，表示除a以外的任意字符。
# [^abcd]就是除abcd以外的任意字符。

# 重复：
# 之前我们用过*、+、{}来表示字符的重复。其他重复的方式还有：
# *——表前面的字符可重复任意次数(0-n次)；匹配时尽可能长的结果(贪婪匹配)
# *?——表前面的字符可重复任意次数(0-n次)；匹配时尽可能短的结果(懒惰匹配)
# +——表重复1次以上(*是0次以上)
# {}——表限定长度(具体重复几次)；{10}10位，{3,5}3-5位
# ?——重复零次或一次
# {n,}——重复n次或更多次
# {n,m}——重复n到m次

# re也被用来判断输入的文本是否符合规范，或进行分类。来点例子看看：
# ^\w{4,12}$
# 这个表示一段4到12位的字符，包括字母或数字或下划线或汉字，可以用来作为用户注册时检测用户名的规则。（但汉字在python2.x里面可能会有问题）
# \d{15,18}
# 表示15到18位的数字，可以用来检测身份证号码
# ^1\d*x?
# 以1开头的一串数字，数字结尾有字母x，也可以没有。有的话就带上x。

# 20200330
# 59 随机数
# 生成[a,b]整数;ab均为整数，b>=a
zz0 = randint(1, 2)
# 生成随机的float[0.0, 1.0)；无参数
zz1 = random.random()
# 生成a、b之间的随机浮点数;无需考虑ab大小
zz2 = random.uniform(1.51, 1.5)
print(zz0, '\t', zz1, '\t', zz2)
# random.choice(seq)；seq为序列；如list，str，tuple，
zz3 = random.choice([1, 4, 'hello', (1, 2, 3)])
zz4 = random.choice('asd123')
zz5 = random.choice((1, 5, 'zxc123'))
print(zz3, '\t', zz4, '\t', zz5)
# random.randrange(start, stop, step)；以step为间隔，生成[start,stop)间的随机数
# 默认start=0,step=1，必须设stop；1、stop 2、start，stop 3、start,stop,step
# 等同于random.choice(range(start,stop,step))
zz6 = random.randrange(1, 5, 2)
zz6_1 = random.choice(range(1, 5, 2))
zz7 = random.randrange(3)
zz8 = random.randrange(4, 6)
print(zz6, '\t', zz6_1, '\t', zz7, '\t', zz8)
# random.sample(population, k);从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。
pop = [1, 5, 's2', (1, 2, 3)]
for i in range(0, 5):
    zz9 = random.sample(pop, 2)
    print(zz9)
# random.shuffle(x);把序列x中的元素顺序打乱。shuffle直接改变原有的序列。
random.shuffle(pop)
z10 = pop
print(pop)

# 60 计时(time模块)
# epoch，它表示的时间是1970-01-01 00:00:00 UTC。
# time.time();返回的就是从epoch到当前的秒数（不考虑闰秒）。这个值被称为unix时间戳。
eg60 = False
if eg60:
    import time

    starttime = time.time()
    print('start:%f' % starttime)
    for i in range(100):
        print(i, end='')
    endtime = time.time()
    print('\nend:%f' % endtime)
    print('total time:%f' % (endtime - starttime))
    # 顺便再说下time中的另一个很有用的方法：time.sleep(secs)
    # 它可以让程序暂停secs秒。在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率。
    print(1)
    time.sleep(2)
    print(2)

# 20200401
# 64 列表解析（List Comprehension）
# 一般方法，通过遍历选取合适的元素创造一个新的列表
list1 = [1, 2, 3, 6, 8, 11, 16]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
print(list2)
# 列表解析
list3 = [i for i in list1]
list4 = [i for i in list1 if i % 2 == 0]
list5 = [i / 2 for i in list1 if i % 2 == 0]
print(list3, list4, list5)
# 用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
list6 = [i for i in range(1, 100) if i % 30 == 0]
print(list6)
print(';'.join([str(i) for i in range(1, 101) if i % 30 == 0]))

# 20200402
# 68 lambda表达式
# lambda 表达式的语法格式：lambda 参数列表: 表达式
# 定义 lambda 表达式时，参数列表周围没有括号，返回值前没有 return 关键字，也没有函数名称。
sum = lambda a, b, c: a + b + c
print(sum(1, 3, 6))
# 下式中，a = lambda y: 2 + y即2+y；a(3)=2+3
def fn(x):
    return lambda y: x + y
a = fn(2)
print(a(3))

# 69 变量的作用域
# 函数内的变量为形参，其作用域只在函数内，与函数外变量无关(即使同名)，即局部变量
# 若想改变则可用return，或用global x令x为全局变量

# 70 map函数
# map(function, iterable, ...)
# function——函数；iterable(可迭代对象)——1/多个序列；返回一个tuple，可用list()改为list
# map是内置函数，它的作用是把列表中的每一项作为函数输入进行计算，再返回迭代器iterator。
# 多个序列运算时，以少的为准
lst_1 = [1,2,3,4,5,6]
def double_func(x):
    return x * 2
lst_2 = map(double_func, lst_1)
lst_3 = map(lambda x, y: x + y, lst_1, [1, 2, 3, 4])
print(lst_2, list(lst_2), list(lst_3))

# 71 reduce函数
# reduce(function, iterable[, initializer]);有一个可选参数，是初始值。
# reduce(f, [x1, x2,..., xn]) = f(f(f(x1, x2),...), xn)
# map 可以看作是把一个序列根据某种规则，映射到另一个序列。
# reduce做的事情就是把一个序列根据某种规则，归纳为一个输出。
eg71 = True
if eg71:
    from functools import reduce
    print (reduce(lambda x, y: x+ y, range(1, 101)))

