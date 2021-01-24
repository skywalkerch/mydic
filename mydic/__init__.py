import hashlib
import http
import random
import json
import urllib
import pymysql
import pandas as pd
from plotly import figure_factory  as FF
from plotly.offline import plot
from aip import AipSpeech
from playsound import playsound

def audio_output(word):
    """ 你的 APPID AK SK """
    APP_ID = '17311850'
    API_KEY = '4uY0GkFIXXE7vDY0jBKDT44n'
    SECRET_KEY = 'PNwRoSMswRzuKpEFjvGBpjelINT8FY49'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(word, 'zh', 1, {'vol': 9, 'spd': 5, 'pit': 5, 'per': 1})
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    playsound('audio.mp3')
class BaiduTranslator():
    def result(self, q):
        appid = '20210125000680464'  # 填写你的appid
        secretKey = 'gCxiZER_Z0qKqiAbqh86'  # 填写你的密钥
        httpClient = None
        myurl = '/api/trans/vip/translate'
        fromLang = 'auto'  # 原文语种
        toLang = 'zh'  # 译文语种
        salt = random.randint(32768, 65536)
        q = q
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            return result

            DataBase.dbconnecting(q, result['trans_result'][0]['dst'])
        except Exception as e:
            print("你的网络连接出现了问题或者是你的查询有问题")
        finally:
            if httpClient:
                httpClient.close()
class DataBase():
    def __init__(self):
        self.user = 'skywalker'
        self.host = '81.70.22.137'
        self.passwd = '123'
        self.database = 'word_list'
        print("请稍等，正在连接数据库")
        self.db = pymysql.connect(user=self.user, password=self.passwd, host=self.host, database=self.database)
        print("数据库连接成功")

    def dbconnecting(self, src, dst):
        cursor = self.db.cursor()
        sql = 'insert into mydic_table (src,dst) values(%s,%s)'
        cursor.execute(sql, (src, dst))
        self.db.commit()

    def database_table_output(self):
        cursor = self.db.cursor()
        sql = 'select * from mydic_table ;'
        cursor.execute(sql)
        lines = cursor.fetchall()
        form = []
        for les in lines:
            form.append(list(les))
        data = pd.DataFrame(form, columns=("单词", "中文"))
        table = FF.create_table(data)
        plot(table, show_link=True)
        print("所有的数据已导出到网页")

    def dbclose(self):
        self.db.close
def menu():
    pass