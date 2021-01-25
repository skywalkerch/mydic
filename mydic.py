from mydic import *
database = DataBase()
bt = BaiduTranslator()
boolean = input("是否要导出数据库(y:是 enter:跳过):")
if boolean == 'y':
    database.database_table_output()
while True:
    try:
        while True:
            word = input("请输入你要查询的原文(自动检测):")
            if word!='':
                break
            else:
                print("不能输入空值")
                print("给我反思3秒!")
                time.sleep(3)
        dst = bt.result(word, menu())
        zh = dst['trans_result'][0]['dst']
        print("单词:" + word + "\n中文:" + zh)
        try:
            audio_output(word)
            audio_output(zh)
        except Exception:
            pass
        try:
            database.dbconnecting(word, zh)
            print("数据库写入成功")
        except Exception:
            pass
    except UnicodeDecodeError:
        print("读音仅支持中文和英文!")
    exit1 = input("输入exit退出程序,enter继续:")

    if exit1 == 'exit':
        database.dbclose()
        try:
            os.remove('temp-plot.html')
        except:
            pass
        sys.exit()
    elif exit1 != 'exit':
        i = os.system('clear')
