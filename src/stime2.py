#! /usr/bin/env python3
import pathlib
import sys
import pexpect
from datetime import datetime
from termcolor import colored, cprint
# dist_dir = pathlib.Path('/Users/qiulang/Project/call_center/JsSipWrap/dist')
# for js in dist_dir.glob('./*.js'):
js = pathlib.Path.home() / 'Project/call_center/JsSipWrap/dist/phonebar.js'
info = js.stat()
mod = datetime.fromtimestamp(info.st_mtime)
now = datetime.now()
delta = now - mod
# datetime 只用秒和天
days = delta.days
# https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
hours = divmod(delta.seconds, 3600)
minutes = divmod(hours[1], 60)
# Use remainder of minutes to calc seconds
seconds = divmod(minutes[1], 1)
# 颜色分段就不能cprint
print(
    f"The file was modified {colored(days, 'red')} days " +
    f"{colored(hours[0],'red')} hours " +
    f"{colored(minutes[0],'red')} minutes ago")
if (days > 0 or hours[0] > 1):
    confirm = input(
        'Are you sure you want to push it to npm '+colored('(Y|N)?', 'red'))
    if (not confirm.startswith(('y', 'Y'))):
        sys.exit()
cprint('npm login', 'cyan')
child = pexpect.spawn('npm login', timeout=20)
child.logfile_read = sys.stdout.buffer
child.expect('Username:')
child.sendline('qiulang2000')
child.expect('Password:')
child.sendline('tongtongjiajia')
child.expect('Email:')
child.sendline('qiulang@gmail.com')
child.expect('Logged in as')
