def fact(n):
    a = 1
    result = 1
    while a <= n:
        result = result*a
        a = a+1
    return result


print(fact(5))


def facto(n):
    if n == 0:
        return 1
    return n * fact(n-1)


print(fact(5))
