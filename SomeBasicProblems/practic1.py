# def Pascal_Case():
#     user_ip = input('Enter a string :').lower()
#     words = user_ip.split()
#     st = ''
#     # st = ''.join([i.capitalize() for i in words])
#     for i in words:
#         print(i)
#         st+=i.capitalize()
#     print(st)
# Pascal_Case()

# input_io = input("Enter a string: ")
# st = ''
# print(input_io.split())
# celsius = 45.899
# # print(f'{round(celsius, 2)}')
#
# def num_neg_pos():
#     while True:
#         number = int(input('Enter a number: '))
#         if number > 0:
#             print(f'{number} is Positive')
#             if number > 100:
#                 print(f'{number} has 3 digits')
#         elif number < 0:
#             print(f'{number} is Negative')
#         else:
#             print(f'{number} is Zero')
# num_neg_pos()
#
# def fetch_vowels():
#     user_ip = input('Enter a string: ')  # hello hamad khan
#     vowels_string = ''
#     for item in user_ip:
#         if item in 'aeiouAEIOU':
#             vowels_string = vowels_string +', ' +item # e o a
#     print(vowels_string)
# fetch_vowels()

#Palindrome
# madam , mom , dad , sis , boob ,tit

# def check_word():
#     user_input = input("enter a string: ") # kiss sis hammad lol boob
#     split_string = user_input.split()
#     lst = []
#     for word in split_string:
#         if word == word[::-1]:
#             lst.append(word)
#     print(lst)
# check_word()

# string1 = ' ***@#$%^&*()hello hamad^^$# kesay &^^$%ho *** '
# special_chr = '@#%$^&*()_+'
# str = ''
# for i in string1:
#     if i not in special_chr:
#         str += i
# print(str)
# num = int(input('write a number upto: '))
# def natural(num):
#     if num == 30:
#         return 1
#     else:
#         print(num)
#         return natural(num+1) + 8 # natural(5-1) natural(4-1) natural(3-1) natural(2-1) natural(1-1)
# print(natural(num))
# num = 11
# for i in range(2, (num // 2) + 1 ):
#     if 11 % 6 == 0:
#         pass# print('false')
#     else:
#         print('num is prime')
# print('down', (num // 2)  )
# print('up', int(num**0.5)+1)

# start = int(input("Enter first number: "))
# stop = int(input('Enter final number:'))
# def isArmstrong(n):
#   str_n = str(n)
#   count = len(str_n)
#   armstrong = 0
#   for j in str_n:
#     armstrong += int(j)**count
#   if armstrong == n:
#     return n
# for i in range(start, stop+1):
#   if isArmstrong(i):
#     print(i, end = " ")

# class Student():
#   def __init__(self,name,phy,computer,english):
#     self.name = name
#     self.phy = phy
#     self.comp = computer
#     self.eng = english
#
#   def avg(self):
#     average = (self.eng+self.comp+self.phy)/3
#     return average
#
# st1 = Student('hamad',44,85,88)
# print(st1.avg())

# def pin():
#   try:
#     user_input = int(input('Enter Computer marks 0-100:'))
#     user_input2 = int(input('Enter English marks 0-100: '))
#     user_input3 = int(input('Enter Physics marks 0-100: '))
#     average = (user_input+user_input2+user_input3)/3
#     return average
#   except (TypeError, ValueError):
#     print('this is not possible you are adding string to integer')
#
# print(pin())
# lst = []
# lst.append()

# class Bank:
#   def __init__(self,acc_num):
#     self.acc_num = acc_num
#     self.__acc_bal = 0
#
#   def credit(self,amount):
#     self.__acc_bal -= amount
#
#   def debit(self,amount):
#     self.__acc_bal += amount
#
#   def get_balance(self):
#     return self.__acc_bal
#
# b1 =  Bank(80755,)
#
# b1.debit(900)
# b1.credit(500)
# print(b1.get_balance())

# class ABC:
#     names = 'Khan11'
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def change(cls,names):
#         cls.names = names
#     @staticmethod
#     def welcome():
#         print('welcome to the world')
#
# s1 = ABC('hamad')
# s1.name = 'khan'
# print(s1.name)
# s1.names = 'king'
# print((s1.names))

# class Student():
#     def __init__(self,phy,comp,eng):
#         self.phy = phy
#         self.comp = comp
#         self.eng = eng
#         # self.per = (phy+eng+comp)/3
#
#     @property
#     def percentage(self):
#         return str((self.phy+self.eng+self.comp)/3) + '%'
#
# st = Student(66,88,99)
# print(st.percentage)
# st.phy = 78
# print(st.percentage)
# # print(st.percentage())

# define a Employee class with attributes role, department and salary and also show detail method

# class Employee:
#     def __init__(self, role, dep, salary):
#         self.role = role
#         self.dep = dep
#         self.salary = salary
#
# class Engineer(Employee):
#     def __init__(self,name,age,role, dep, salary):
#         self.name = name
#         self.age = age
#         super().__init__(role,dep,salary)
#
#     def show_details(self):
#         return f' name = {self.name}, age = {self.age}, role = {self.role}, department = {self.dep}, salary = {self.salary}'
#
# clas = Engineer('hammad','26','Software Engineer', 'Computer Science', 60000)
# print(clas.show_details())

class Order:
    def __init__(self,item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        if self.price > other.price:
            return f'{self.item} is Expensive then {other.item} '
        elif other.price > self.price:
            return f'{other.item} is Expensive than {self.item}'

apple16 = Order('16pro max', 400000)
samsung22 = Order('s22 Ultra', 980000)

print(apple16 < samsung22)