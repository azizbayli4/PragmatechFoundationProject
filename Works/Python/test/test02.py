# def SumOfElements(myList):
#     sum = 0
#     for x in myList:
#         sum = sum + x

#     return sum


# print(SumOfElements([1, 3, 5, 7, 6]))
# ededler = '0123456789'
# a = input('Eded daxil edin: ')
# total = 0
# for x in a:  # 255.5
#     if x in ededler:
#         total = total + int(x)
#     # else:
#     #     break

# print(total)

x = input('eded: ')
# x = str(x)

for i in range(len(x)):
    print(x[i])
    if x[i] == '.':
        noqte_index = i+1

cem = 0

for j in x[noqte_index:]:
    cem += int(j)

print('cem:', cem)


# a='baku'
# print(a[1:])
