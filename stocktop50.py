import requests
import re
import csv
import datetime
import configparser
import os

# 爬取A股每日前五十资金流入个股的数据，并生成csv格式文件保存在本地
class Stock_clawer:

    def __init__(self):
        self.BASE_DIR = os.path.split(os.path.realpath(__file__))[0]
        config = configparser.ConfigParser()
        config.read(os.path.join(self.BASE_DIR, 'config.ini'), encoding='utf-8')
        self.HEADER = config.get('CONFIG', 'HEADER')
        self.RE = re.compile(
            r'{"f2":(?P<new_pr>.*?),"f3":(?P<today_rate>.*?),"f12":"(?P<code>.*?)","f14":"(?P<name>.*?)",'
            r'"f62":(?P<main_in_num>.*?),"f66":(?P<huge_in_num>.*?),"f69":(?P<huge_in_rate>.*?),'
            r'"f72":(?P<big_in_num>.*?),"f75":(?P<big_in_rate>.*?),"f78":(?P<mid_in_num>.*?),'
            r'"f81":(?P<mid_in_rate>.*?),"f84":(?P<lil_in_num>.*?),"f87":(?P<lil_in_rate>.*?),"f124".*?'
            r'"f184":(?P<main_in_rate>.*?),"f204".*?}', re.S)
        self.TITLE = ['代码', '名称', '最新价', '今日涨跌幅', '今日主力净流入', '今日主力净占比', '今日大单净流入', '今日大单净占比',
                      '今日中单净流入', '今日中单净占比', '今日小单净流入', '今日小单净占比']
        self.DATE = datetime.date.today()

    def Clawer(self):
        # 爬取个股数据
        url = "http://push2.eastmoney.com/api/qt/clist/get"
        param = {
            'cb': 'jQuery112306770811256481346_1618137516959',
            'fid': 'f62',
            'po': '1',
            'pz': '50',
            'pn': '1',  # 修改此处可以获取第50位以后的数据，如pn： 2 可获得51-100位的数据
            'np': '1',
            'fltt': '2',
            'invt': '2',
            'fs': 'm:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2',
            'fields': 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124'
        }
        header = {
            'User-Agent': f'{self.HEADER}'
        }
        # 解析爬取到的数据
        resp = requests.get(url=url, params=param, headers=header)
        obj = self.RE
        self.RESULT = obj.finditer(resp.text)

    def Csvwriter(self):
        # 将解析完成的数据整理写入进csv文件
        with open(f"{self.DATE}个股资金流top50.csv", 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(self.TITLE)  # 先写入题头
            for result in self.RESULT:
                csvwriter.writerow(
                    result.group('code', 'name', 'new_pr', 'today_rate', 'main_in_num', 'main_in_rate', 'huge_in_num',
                                 'huge_in_rate', 'big_in_num', 'big_in_rate', 'mid_in_num', 'mid_in_rate', 'lil_in_num',
                                 'lil_in_rate'))


if __name__ == '__main__':
    clawer = Stock_clawer()
    clawer.Clawer()
    clawer.Csvwriter()
    print('over!!')
