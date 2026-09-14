# name = 9
# text = f"Hello {name}"
# # text= "Hello, " + str(name)
# print(text)
# import asyncio
# s
# set
# from Main import main
#
# asyncio.run(main())
import time

def make_tea():
    print("Ставлю чайник...")
    time.sleep(2)
    print("Чай готовий")

def toast_bread():
    print("Кладу хліб у тостер...")
    time.sleep(2)
    print("Тост готовий")

start = time.perf_counter()
make_tea()
toast_bread()
print(f"Разом: {time.perf_counter() - start:.1f} с")