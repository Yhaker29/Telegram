import asyncio
import time

async def make_tea():
    print("Ставлю чайник...")
    await asyncio.sleep(6)
    print("Чай готовий")

async def toast_bread():
    print("Кладу хліб у тостер...")
    await asyncio.sleep(4)
    print("Тост готовий")
async def main():
    start = time.perf_counter()
    await asyncio.gather( make_tea(), toast_bread() )
    print(f"Разом: {time.perf_counter() - start:.1f} с")
asyncio.run(main())