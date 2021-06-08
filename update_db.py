#! /usr/bin/env python3
# coding:utf-8
import mysql.connector
from mysql.connector import errorcode
import os
import time
import argparse

# instead of os.environ['DB_USER']
user = os.environ.get('DB_USER', 'sql6417424')
password = os.environ.get('DB_PASS', 'U8PpVbYjhp')
host = os.environ.get('DB_HOST', 'sql6.freemysqlhosting.net')
cnx = None  # otherwise cnx is undefined when failed to connect to DB
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--crash", default=0, type=int,
                    help="Whether to exit before finishing")
args = parser.parse_args()
try:
    cnx = mysql.connector.connect(user=user,
                                  password=password,
                                  host=host,
                                  database='sql6417424')
    if cnx.is_connected():
        db_Info = cnx.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    else:
        print('Failed to connect the DB')
        exit(0)
    cursor = cnx.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from users where user_id = 1 for update"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update users set username = 'qiulang' where user_id = 1"""
    cursor.execute(sql_update_query)
    print('I am about to sleep in 30 seconds')
    time.sleep(30)
    if args.crash == 1:
        print('OK let us crash')
        # exit(1)
        print(args.c)
    else:
        print('OK let us continue to run instead of crashing')
    cnx.commit()
    print("Record Updated successfully ")
    # Timer(30, lambda: print('.')).start()

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # cursor = cnx.cursor()
    # sql = "select value from setting where `key`=%s"
    # # To write a tuple containing a single value you have to include a comma, even though there is only one value
    # cursor.execute(sql, ('cc_man_db_version',))
    # record = cursor.fetchone()
    # if record == None:
    #     print('no record for cc_man_db_version')
    #     exit(1)
    # db_version = record[0]
    # if int(db_version) < 7932:
    #     print('DB version is too old, just exit')
    #     exit(1)
    # cursor.execute(sql, ('CM_Update_Procedure_r7932',))
    # record = cursor.fetchone()
    # if record != None:
    #     print('All set, just return')
    #     exit(0)
    # print('run our update script NOW!')
    # p = Popen(['php', 'artisan', 'async:pub-account-data'],
    #           stdout=PIPE, bufsize=1)
    # with p.stdout:
    #     for line in iter(p.stdout.readline, b''):
    #         print(line.decode('utf-8'))
    # p.wait()  # wait for the subprocess to exit
    # if p.returncode != 0:
    #     print('Update script failed!')
    #     exit(1)
    # sql = 'INSERT IGNORE INTO setting (`key`,value, description,created_at) VALUES ("CM_Update_Procedure_r7932","1", "代码数据补充", unix_timestamp(now()))'
    # cursor.execute(sql)
    # cnx.commit()
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
    print(f'here:{args.crash}')
    if args.crash == 1:
        exit(0)
    if cnx != None and cnx.is_connected():
        print('Will I run?')
        cursor.close()
        cnx.close()
