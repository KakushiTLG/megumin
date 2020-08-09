import math
import random
import pymysql
import pymysql.cursors

def dogs(dog):
    if dog == 0:
        item = "Отсутствует"
        desc = ""
    elif dog == 1:
        item = "Чарли"
        desc = "С Чарли вы сможете покупать предметы в магазине дешевле"
    elif dog == 2:
        item = "Джек"
        desc = "Джек поможет вам в битве своей силой атаки"
    elif dog == 3:
        item = "Джеймс"
        desc = "С Джеймсом ваша выносливость будет больше"
    elif dog == 4:
        item = "Эндрю"
        desc = "Эндрю - тот талисман, о котором мечтает каждый боец. Благодаря его помощи, увеличивается шанс на критический урон."
    return item, desc