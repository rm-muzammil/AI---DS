import asyncio

async def fetch_data(user_id):
    print(f"Fetching user {user_id}")

    await asyncio.sleep(5)

    return f"User {user_id} data"

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )

    print(results)

asyncio.run(main())