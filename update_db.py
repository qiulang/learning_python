#! /usr/bin/env python
# coding:utf-8
import mysql.connector
from mysql.connector import errorcode
import os
from subprocess import Popen, PIPE, CalledProcessError

# instead of os.environ['DB_USER']
user = os.environ.get('DB_USER', 'emicall_cr_s')
password = os.environ.get('DB_PASS', 'Emiknit_e23456')
host = os.environ.get('DB_HOST', 'emicall-cr-ext.mysql.rds.aliyuncs.com')
cnx = None  # otherwise cnx is undefined when failed to connect to DB
try:
    cnx = mysql.connector.connect(user=user,
                                  password=password,
                                  host=host,
                                  database='emicall_cc_man',
                                  connect_timeout=10)
    cursor = cnx.cursor()
    sql = "select value from setting where `key`=%s"
    # To write a tuple containing a single value you have to include a comma, even though there is only one value
    cursor.execute(sql, ('cc_man_db_version',))
    record = cursor.fetchone()
    if record == None:
        print('no record for cc_man_db_version')
        exit(1)
    db_version = record[0]
    if int(db_version) < 7932:
        print('DB version is too old, just exit')
        exit(1)
    cursor.execute(sql, ('CM_Update_Procedure_r7932',))
    record = cursor.fetchone()
    if record != None:
        print('All set, just return')
        exit(0)
    print('run our update script NOW!')
    p = Popen(['php', 'artisan', 'async:pub-account-data'],
              stdout=PIPE, bufsize=1)
    with p.stdout:
        for line in iter(p.stdout.readline, b''):
            print(line.decode('utf-8'))
    p.wait()  # wait for the subprocess to exit
    if p.returncode != 0:
        print('Update script failed!')
        exit(1)
    sql = 'INSERT IGNORE INTO setting (`key`,value, description,created_at) VALUES ("CM_Update_Procedure_r7932","1", "代码数据补充", unix_timestamp(now()))'
    cursor.execute(sql)
    cnx.commit()
    # finish!!!
except mysql.connector.Error as err:
    if err.errno == errorcode.CR_CONN_HOST_ERROR or err.errno == errorcode.CR_UNKNOWN_HOST:
        print("Failed to connect to database %s" % host)
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The user name or password is incorrect")
    else:
        print(err)
    exit(1)
finally:
    if cnx != None and cnx.is_connected():
        cursor.close()
        cnx.close()
