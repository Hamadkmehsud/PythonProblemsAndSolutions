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
#
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

string1 = ' ***@#$%^&*()hello hamad^^$# kesay &^^$%ho *** '
special_chr = '@#%$^&*()_+'
str = ''
for i in string1:
    if i not in special_chr:
        str += i
print(str)












