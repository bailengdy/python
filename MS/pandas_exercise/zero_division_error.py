try:
    x = 1 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("always run")