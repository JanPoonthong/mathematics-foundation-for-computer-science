def recursive_m(n):
    if n == 1:
        return 51
    else:
        return recursive_m(n - 1) + 2


def explicit_m(n):
    return 51 + 2 * (i - 1)


def iterative_m(n):
    if n == 1:
        return 51
    else:
        pre = 51
        result = 51
        for i in range(2, n + 1):
            result = pre + 2
            pre = result
    return result


print("n\tIterative\tRecursive\tExplicit Formula")
for i in range(1, 100):
    print(f"{i}\t{iterative_m(i)}\t\t{recursive_m(i)}\t\t{explicit_m(i)}")


print()
print()
print()


def recursive_p(n):
    if n == 1:
        return 32
    else:
        return recursive_p(n - 1) + 13


def iterative_p(n):
    pre = 32
    result = 32
    for i in range(2, n + 1):
        result = pre + 13
        pre = result
    return result


def explicit_p(n):
    return 32 + 13 * (n - 1)


print("n\tIterative\tRecursive\tExplicit Formula")
for i in range(1, 100):
    print(f"{i}\t{iterative_p(i)}\t\t{recursive_p(i)}\t\t{explicit_p(i)}")
