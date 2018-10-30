#coding=gbk

##����˵sqlite3�ڲ����õ���utf-8�ı��룬���ǣ��������ݿ�����ӵ�ʱ���õ�Ҳ��Unicode string��û��
##�����utf-8����ȡ��ʱ�򣬻�����Unicode ��%uni_result������û��ʲô���󰡡�

import sqlite3
import sys
import os
import urllib
import json


#############################################################################################################
def get_city_from_user():
    provience=raw_input(r"���������ʡ��/ֱϽ�У� ")
    city=raw_input(r"��������ĳ���/���� ")
    country=raw_input(r"�����������/���� ")

    result = provience+city+country
    uni_result = result.decode(sys.stdin.encoding) ##��sys.stdin.encoding.���õ���׼����ı��뷽ʽ
                                                   ## ���߻���localeģ��� getpreferredencoding(True)
    return uni_result


def give_city_id(sql_cursor,city):
    query = u'''SELECT * FROM weather_id WHERE city_name == "%s"''' %city

        ##query Ҫ��u,����ʵUnicode string��"%s" ������һ��Ҫ�� ���ţ����ţ����ţ�����

    sql_cursor.execute(query)

    sql_id = sql_cursor.fetchone()
    if sql_id == None : ##���û�з��������ļ�¼��sqlite3�᷵��Noneֵ��
        print u"              ##�Բ��������������󣡣���"
        return None       ##������ͷ���һ�����⣬��û���ҵ���¼�ǣ�Ӧ���˳���ǰ��ѭ����������һ��ѭ������ʱ��ʱ��������ĺ��������У�
    else:                 ##continue���޷���while��֪�����Ծ�һ���ķ���Ԥ���ĳ���ֵ��ͻȻ����ˣ�C�е�longjump()���������ã�������
        return sql_id[1]


def print_weather(city_id):
    if city_id:
        #url = u"http://www.weather.com.cn/data/sk/%s.html" %city_id
        url = u"http://www.weather.com.cn/data/cityinfo/%s.html" %city_id
        url_content = urllib.urlopen(url).read().decode("utf-8")
        python_content = json.loads(url_content)
        for key in python_content["weatherinfo"].keys():
            to_print = '''\t %10s  :  %-20s'''  %(key,python_content["weatherinfo"][key])
            print to_print
    else:
        return False
####################################################################################################################

myconnect = sqlite3.connect(u".\sqlite3_cityID/weather.db")
mycursor = myconnect.cursor()

while raw_input(u"�˳��밴���ո����/�������������ѯ����").decode(sys.stdin.encoding) != u" ":
    if not print_weather(give_city_id(mycursor,get_city_from_user())):
        continue
    
myconnect.close()
