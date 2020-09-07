#!/usr/bin/expect
set timeout 10
spawn npm login
expect "Username:"
send "qiulang2000\r"
expect "Password:"
send "tongtongjiajia\r"
expect "Email:"
send "qiulang@gmail.com\r"
expect "Logged in as"
interact
