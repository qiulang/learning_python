#! /usr/bin/expect
set timeout 10
spawn ssh qiulang@10.0.0.32
expect "password:"
# using double quote! single quote won't work
send "123456\r"
interact