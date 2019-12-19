#! /usr/bin/env python3
import re
output = 'Successfully built qiulang'
group = re.search('Successfully built (.*)', output)
image_id = group[1]
print(image_id)
