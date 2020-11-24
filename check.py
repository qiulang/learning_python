subtree = {'wsserver': ('ws_redis',), 'wsclient': ('bs-front',),
           'ccfront': ('cc-frontend',), 'jssip': ('jssipwrap', 'emickf')}
for key in subtree:
    sub = subtree[key]
    if len(sub) == 2:
        print(sub[1])
    else:
        print(f'{key} does not have server folder,just {sub[0]}')
