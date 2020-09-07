#! /usr/bin/env python3

import pexpect
print('npm login')
child = pexpect.spawn('npm login')
child.expect('Username: ')
child.sendline('qiulang2000')
child.expect('Password: ')
child.sendline('tongtongjiajia')
child.expect('Email:')
child.send('qiulang@gmail.com')
child.expect('Logged in')
# print(child.before)   # Print the result of the ls command.
child.interact()
