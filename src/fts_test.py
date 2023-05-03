#! /usr/bin/env python3
# coding:utf-8
# https://stackoverflow.com/questions/41680533/is-coding-utf-8-also-a-comment-in-python
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error
import random
import datetime

op = ("登出系统管理页面","登录企业管理页面","坐席状态切换","手动签入","话后处理","通话发起",'自动接听'
      "自动签入","登出坐席页面","登录坐席页面",'坐席签出','坐席呼出','坐席状态切换',"工单","通话结束"
      "挂断电话","通话转子流程","登出企业管理页面",'登录系统管理页面',"通话保持","坐席转接")

au = ('邱朗','余齐','春燕','杨毅','李恺','少峰','李樊','周强','晓韬','杨成','张丰峰','王鹏')

tit = ('系统管理页面','企业管理页面','坐席状态','通话','迁入迁出')

try:
    cnx = mysql.connector.connect(user='emicall_cr_s',
                                  password='Emiknit_e23456',
                                  host='emicall-cr-ext.mysql.rds.aliyuncs.com',
                                  database='emicall_cc_man')
    # cnx = mysql.connector.connect(user='root',
    #                             password='qwerty',
    #                             host='10.0.0.32',
    #                             database='mysql')
    if cnx.is_connected():
        db_Info = cnx.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    else:
        print('Failed to connect the DB')
        exit(0)
    cursor = cnx.cursor()
    # count = cursor.execute("select count(*) from opening_lines4")
    # print(f"count {count}")
    add_line = ("INSERT INTO opening_lines4 "
              "(opening_line, author, title) "
              "VALUES (%(opening_line)s, %(author)s, %(title)s)")
    print(datetime.datetime.now())
    for _ in range(1):
        for _ in range(100):
            data_line = {
                "opening_line":op[random.randint(0,len(op)-1)],
                "author":au[random.randint(0,len(au)-1)],
                "title":tit[random.randint(0,len(tit)-1)]
            }
            cursor.execute(add_line, data_line)
        cnx.commit()
    print(datetime.datetime.now())
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if cnx != None and cnx.is_connected():
        cursor.close()
        cnx.close()