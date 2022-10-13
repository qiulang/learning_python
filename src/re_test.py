#! /usr/bin/env python3
import re
output = 'Successfully built qiulang'
group = re.search('Successfully built (.*)', output)
image_id = group[1]
print(image_id)

c = """
This is a longer string that 
spans multiple lines
"""
l = c.count('\n')
print(l)
