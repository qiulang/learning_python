#! /usr/bin/env python3

import pexpect
import sys
print('npm login')
child = pexpect.spawn('npm login', timeout=15)
child.logfile_read = sys.stdout.buffer
child.expect('Username:')
child.sendline('qiulang2000')
child.expect('Password:')
child.sendline('tongtongjiajia')
child.expect('Email:')
child.sendline('qiulang@gmail.com')
child.expect('Logged in as')
# If a logfile is specified, then the data sent and received from the child process in interact mode is duplicated to the given log.
# child.interact()
