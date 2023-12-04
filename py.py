'''
a = int(input("первая цыфра: "))
c = int(input("вторая цыфра: "))

while True:
    b = input("математическое операция ")

    if b == "+":
        print(a + c)
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        print(a / c)
'''




'''123 = 6'''
# a = input('>>> ')
# b = 0
# for i in range(len(a)):
#     b = b + int(a[i])
#
# print(b)


'''
1
12
123
'''
# a = input(">>> ")
#
# for i in range(len(a)):
#     b = ''
#     for j in range(i+1):
#         b = b + str(j+1)
#
#     print(b)


''' n = 11 [1, 2, 3, 5, 7, 11] '''

# n = int(input(">>> "))
# lst = []
# k = 0
#
# for i in range(2, n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             k = k + 1
#     if k == 0:
#         lst.append(i)
#     else:
#         k = 0
# print(lst)


'''tub/tub emas'''
# num = int(input(">>> "))
# b = 0
#
# for i in range(1, num+1):
#     if num % i == 0:
#         b += 1
#
# if b == 2:
#     print("tub")
# else:
#     print("tub son emas")
#


'''Exceptions'''

# try:
#     a = int(input(">>> "))
#     b = int(input(">>> "))
#
#     print(a + b)
# except ValueError:
#     print("Son kiriting")


# try:
#     num1 = int( input(">>> "))
#     num2 = int( input(">>> "))
#     print(num1 / num2)
#
# except ZeroDivisionError:
#     print("0-ga bolinmaydi")

# try:
#     print(a)
# except NameError:
#     print("Ozgaruvchi mavjut emas")
#


# try:
#     print("123" + 123)
# except TypeError:
#     print("TypeError")




















