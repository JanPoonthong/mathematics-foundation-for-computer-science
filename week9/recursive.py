def f(n):
    if n == 1:
        return 3
    else:
        return f(n - 1) + 2


for each in range(1, 51):
    print(f"f({each}) = {f(each)}")
