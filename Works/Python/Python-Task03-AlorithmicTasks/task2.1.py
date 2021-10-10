# 1. Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə
# bölək, əgər təkdirsə ona 1 əlavə edək. Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq.
# Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik
# etmək lazımdır.
# Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.

num = int(input('Enter a number: '))
count = 0


def f(x):
    x = int(x)
    if x % 2 == 0:
        x = x/2
    else:
        x = x+1
    return x


while num != 1:
    num = f(num)
    count = count+1

print(count)
