import asyncio

async def process_task(name, delay):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} completed")

async def main():
    await asyncio.gather(
        process_task("Image Analysis", 3),
        process_task("PDF Summary", 2),
        process_task("AI Chat Response", 4)
    )

asyncio.run(main())