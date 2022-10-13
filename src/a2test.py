import asyncio
from pprint import pprint

import random


async def coro(tag):
    print(">", tag)
    await asyncio.sleep(random.uniform(1, 3))
    print("<", tag)
    return tag


loop = asyncio.get_event_loop()

group1 = asyncio.gather(*[coro(f"group 1.{i}") for i in range(1, 6)])
group2 = asyncio.gather(*[coro(f"group 2.{i}") for i in range(1, 4)])
group3 = asyncio.gather(*[coro(f"group 3.{i}") for i in range(1, 10)])
print('start to gather')

all_groups = asyncio.gather(group1, group2, group3)

results = loop.run_until_complete(all_groups)

loop.close()

print('loop close')

pprint(results)
