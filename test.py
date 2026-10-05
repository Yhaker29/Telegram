a="python"
try:
    b=int(a)/0
    print(b)
except ValueError:
    print("type a number ")
except ZeroDivisionError:
    print("i hate zero 🤬😡")