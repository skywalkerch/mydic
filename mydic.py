from mydic import *

database = DataBase()
bt = BaiduTranslator()
bo = input("是否要导出数据库(y:是 enter:跳过):")
if bo == 'y':
    database.database_table_output()
while True:

    try:
        print("请输入翻译功能所对应的命令\n(eg:输入y表示翻译为英语)")
        fromto = input("y->翻译为英语\nh->翻译为汉语\nr->翻译为日语\nhan->翻译为韩语\nw->翻译为文言文\nx->翻译为西班牙语\ne->翻译为俄语\na->翻译为阿拉伯语:")
        if fromto == 'y':
            fromLang = 'en'
        elif fromto == 'h':
            fromLang = 'zh'
        elif fromto == 'r':
            fromLang = 'jp'
        elif fromto == 'han':
            fromLang = 'kor'
        elif fromto == 'w':
            fromLang = 'wyw'
        elif fromto == 'x':
            fromLang = 'spa'
        elif fromto == 'e':
            fromLang = 'ru'
        elif fromto == 'a':
            fromLang = 'ara'
        word = input("请输入你要查询的原文(自动检测):")
        dst = bt.result(word, fromLang)
        zh = dst['trans_result'][0]['dst']
        print("单词:" + word + "中文:" + zh)
        audio_output(word)
        audio_output(zh)

        try:
            database.dbconnecting(word, zh)
            print("数据库写入成功")
        except Exception:
            pass
    except UnicodeDecodeError:
        print("读音仅支持中文和英文!")
    except KeyError:
        print("不能输入空值")
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
