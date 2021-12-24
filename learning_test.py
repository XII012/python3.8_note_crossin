import math, random, requests, time, os, sys, _thread, threading, string, re, img2pdf
from PIL import Image
from operator import *
from collections import *
from bs4 import BeautifulSoup

'''如果有png会提示存在alpha channel不能转化，还有bmp暂时也没有搞定
解决方法：转换图片为jpg（否则就算转换成pdf大小也会对不上）
'''
'''
for i in range(78, 80):
    num1 = i
    print('start %s' % num1)
    dirname = "pic\manga\%s" % num1
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)

    with open("pic\manga\驯服小姨子%02d.pdf" % num1, "wb") as f:
        f.write(img2pdf.convert(imgs))
        print('end %s' % num1)
'''



########## Monty Hall Problem ###########
############## TASK 2.2 #################
################ (a) ####################

def Monty_Hall_Problem(times: int):
    import random
    win_with_change = 0
    win_without_change = 0
    win_with_random = 0
    for i in range(0, times):
        doors = [1, 2, 3]  # 分别代表几等奖，一等奖是car，二等奖是money，三等奖是zonk
        random.shuffle(doors)
        price = doors[random.randint(0, 2)]  # 让系统随便选一个，选什么就是几等奖
        doors.remove(price)
        random_not = random.randint(0, 1)

        if 1 in doors:
            # If 1 hasn't been choosed, the mendator will remove the other wrong answer.
            # As there is no need for showing a price.
            # I can directly see the process as removing a wrong answer.
            doors = [1]
        else:
            doors.remove(random.choice((2, 3)))

        if price == 1:
            # If you choose 1 at the beginning, you can only win without changing.
            win_without_change += 1
            if random_not == 0:
                win_with_random += 1
        else:  # price==2/3
            # If you didn't choose 1 ,you can only win by changing.
            win_with_change += 1
            if random_not == 1:
                win_with_random += 1

    print("Total times: ", times)
    print("Win rate with changing: %.2f%%" % (win_with_change / times * 100))
    print("Win rate without changing: %.2f%%" % (win_without_change / times * 100))
    print("Win rate with random: %.2f%%" % (win_with_random / times * 100))


# Test the function
Monty_Hall_Problem(1000)
Monty_Hall_Problem(100000)
