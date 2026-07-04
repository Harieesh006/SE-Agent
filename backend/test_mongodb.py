import asyncio

from config.mongodb import check_connection


async def main():
    await check_connection()


asyncio.run(main())