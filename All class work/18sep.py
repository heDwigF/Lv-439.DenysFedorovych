# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# nums = []
# k=int(input("Please enter the count of the elements of sequence: "))
# for i in range(k):
#      n = int(input("Please enter the element: "))
#      nums.append(n)
# print(nums)
# max = nums[0]
# min = nums[0]
# for i in range(k):
#     if nums[i] > max:
#         max = nums[i]
#     if nums[i] < min:
#         min = nums[i]
# print("Maximum number = {}. Minimum number = {}.".format(max, min))



# # task2   В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

# for x in range (1, 11):
#     if x % 2 == 0:
#         print (x, "is even multiple of 2")
#     elif x % 3 == 0:
#         print(x, "is an odd multiple of 3")
#     else:
#         print(x, "not divisible by 2 and 3")       





# task3 Написати програму, яка обчислює факторіал числа, 
# яке користувач вводить.(не використовувати рекурсивного виклику функції)

a =int(input('Enter a number '))
factorial = 1
for i in range(1, a+1):
    factorial = factorial*i
print(factorial)


'''import math
def fac(n):
    fac = 1 
    i = 0 
    while i < n:
        i += 1
        fac = fac * i
    return fac'''



# task4 Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

# log = 'First'
# login = ""
# while log != login:
#     login = input('Enter your login: ')
#     if log != login:
#         print('Entrence error: User is not found. Please, try again.')
# print('You are welcome!')