# def distance():
#     x1 = float(input())
#     x2 = float(input())
#     y1 = float(input())
#     y2 = float(input())
#     print(((x1-x2)**2 + (y1-y2)**2)**0.5)
# distance()
# ===========================================02

# def power():
#     a = int(input())
#     n = int(input())
#     print(a*n)
# power()
# ===========================================03

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(1))
# ==========================================04
# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))
# =========================================05
# i = int(input('Enter year: '))
#
# def is_year_leap(i):
#     if i % 4 == 0 or i % 400 == 0:
#         print('True')
#     else:
#         print('False')
#
# is_year_leap(i)

# =========================================06
# def square(a):
#     return a*4, a**2, (2 * a**2 ) ** 0.5
# ans = square
# print(ans(int(input())))
# ========================================07
# def season():
#     num = int(input())
#     if num > 2 and num <=5:
#         print('Весна')
#     if num > 5 and num <= 8:
#         print('Лето')
#     if num > 8 and num < 12:
#         print('Осень')
#     if num > 11 or num < 3 and num < 13:
#         print('Зима')
# season()
# ========================================08

# def bank():
#     a = int(input('Enter initial payment: '))
#     year = int(input('Enter quantity year: '))
#     for i in range(year - 1):
#         a += a / 10
#         print(a)
# bank()
# ========================================09

# def date(year, month, day):
#     if year == 2023:
#         if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#             return day <= 31
#             return True
#         if month == 4 or month == 6 or month == 9 or month == 11:
#             return day <= 30
#             return True
#         if month == 2:
#             return day <= 28
#
#         else:
#             return False
#     elif year != 2023:
#         return False
# print(date(int(input()), int(input()), int(input())))
