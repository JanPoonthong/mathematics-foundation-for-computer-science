def main(a):
    if a == 1:
        return 3
    else:
        return main(a-1) + 2 


for i in range(1, 501):
    print(f"{i} {main(i)}")
