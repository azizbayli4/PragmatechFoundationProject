# 2. n natural ədədi verilmişdir. Əgər n ədədi hər hansı bir m natural ədədinin kvadratıdırsa, onda m ədədini çap edin,
# əks halda No çap edin.
# Məsələn: User 25 daxil etsə ekrana 5 verilsin
# 27 daxil etsə, NO yazılsın

num = int(input('Enter a number: '))


def f(n):
    for x in range(0, int(n/2)):
        if x**2 == n:
            return x
    else:
        return None


print(f(num))
