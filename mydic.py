import os
import sys
from mydic import *

database = DataBase()
bt = BaiduTranslator()

while True:
    bo = input("是否要导出数据库(y:是 enter:跳过):")
    if bo == 'y':
        database.database_table_output()
    try:
        word = input("请输入你要查询的单词:")
        dst = bt.result(word)
        zh = dst['trans_result'][0]['dst']
        print("单词:" + word + "中文:" + zh)


        audio_output(word)
        os.remove('audio.mp3')
        try:
            database.dbconnecting(word, zh)
            print("数据库写入成功")
        except Exception:
            pass
    except Exception:
        print("不能输入空值!")
    exit1 = input("输入exit退出程序,enter继续:")

    if exit1 == 'exit':
        database.dbclose()
        try:
            os.remove('temp-plot.html')
        except:
            pass
        sys.exit()
    elif exit1 != 'exit':
        i = os.system('cls')
