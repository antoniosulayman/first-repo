import asyncio
import aiohttp
import time

async def fetch(session, num):
    print("Requesting", num, "...")
    async with session.get("https://httpbin.org/delay/2") as resp:
        await resp.text()   
    print("Got response", num)

async def main():
    async with aiohttp.ClientSession() as session:

        await asyncio.gather(*(fetch(session, i + 1) for i in range(10)))

start = time.time()
asyncio.run(main())
print(f"Asyncio: {time.time() - start:.2f} sec")
