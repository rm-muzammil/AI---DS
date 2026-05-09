# import asyncio

# async def hello():
#     print("Hello")

#     await asyncio.sleep(5)

#     print("Done")

# asyncio.run(hello())

# import time

# def task(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")

# task("A")
# task("B")

import asyncio

async def task(name):
    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )

asyncio.run(main())