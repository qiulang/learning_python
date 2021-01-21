import asyncio


async def hello(i):
    print(f"hello {i} started")
    await asyncio.sleep(4)
    print(f"hello {i} done")


async def main():
    # returns immediately, the task is created
    task1 = asyncio.create_task(hello(1))
    print('prepare to sleep 3 seconds')
    await asyncio.sleep(3)
    print('sleep 3 seconds')
    task2 = asyncio.create_task(hello(2))
    print('now await task 1&2')
    await task1
    await task2

asyncio.run(main())  # main loop
