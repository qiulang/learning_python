#!/usr/bin/env python3

import pexpect
import sys
child = pexpect.spawn('ssh qiulang@10.0.0.32')
child.logfile_read = sys.stdout.buffer
child.expect('password:')
child.sendline('123456')
# child.expect('Last login')
child.logfile_read = None
child.interact()
