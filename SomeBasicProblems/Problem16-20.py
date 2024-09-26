#Problem 15: Write a program to interchange key , values in a dictionary
from pickletools import uint1

from jinja2.utils import missing
from sqlalchemy.testing.suite.test_reflection import users


def interchange_key_values():
    dic = {'Name': 'Hammad', 'Username': 'Hamadkmehsud', 'Email': 'Hamadkmehsud@gmail.com'}
    for key, value in dic.items():
        print(value,':',key)
# interchange_key_values()
def inter_key_val():
    dic = {'Name': 'Hammad', 'Username': 'Hamadkmehsud', 'Email': 'Hamadkmehsud@gmail.com'}
    # print({value : key for key, value in dic.items()})
    rev_dict = {}
    for key, value in dic.items():
        rev_dict[value] = key
    print(rev_dict)
# inter_key_val()

#Problem 16: Write a program that find square of all even num in list
def square_even(l):
    e_lst = []
    for i in l:
        if i % 2 == 0:
            e_lst.append(i**2)
        else:
            e_lst.append(i)
    print(e_lst)
# square_even([3,4,5,7,23,5,6,2])
a = [3,4,5,7,23,5,6,2]
lst  = [i**2 for i in a if i%2==0]
# print(lst)

#Problem 17: Write a program that display the character repeating more numbers of times in a string
def more():
    user_ip = input('Enter a string: ')
    d = {}.fromkeys(user_ip,0)
    for i in user_ip:
        d[i]  = d[i] + 1
    print(d)
    for j in d:
        if d[j] == max(d.values()):
         print('{} is repeated {} times '.format(j,d[j]))
# more()

#Problem 18: Write a program that fetch all the palindrome words in a string
def palindrome_words():
    user_ip = input('Enter a String: ')
    split = user_ip.split()
    lst = []
    for i in split:
        if i == i[::-1]:
            lst.append(i)
    print(lst)
# palindrome_words()
lst1 = ['madam', 'hamad', 'khan', 'user', 'kala', 'lala', 'sys', 'naran']
# print([i for i in lst1 if i[::-1] == i])

#Problem 19: Write a program that reverse words in a string
def reverse_words():
    user_ip = input('Enter a String: ')
    lst11 = [i[::-1] for i in user_ip.split() ]
    print(lst11)
    # split = user_ip.split()
    # for i in split:
    #     lst11.append(i[::-1])
    # print(lst11)
# reverse_words()

#Problem 20 : Write a program to display the longest and shortest words
def long_word():
    user_ip = input('Enter a String: ').split()
    max_length = 0
    for word in user_ip:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
    for j in user_ip:
        if len(j) == max_length:
            long_w = j
    print(f'longest word is {long_w} and its length is {max_length}')
    # print(max(len(i) for i in user_ip))
# long_word()

def short_word():
    user_ip = input('Enter a String: ').split()
    min_length = len(user_ip)
    for word in user_ip:
        word_length = len(word)
        if word_length < min_length:
            min_length = word_length
    for j in user_ip:
        if len(j) == min_length:
            short_w = j
    print(f'Shortest word is {short_w} and its length is {min_length}')
# short_word()

#Problem 20 : Write a program to find an index of all occurrences of a same character
def find_index():
    user_ip = input('Enter a String: ')
    user_index = input('Enter a letter for its index : ')
    for item in range(0,len(user_ip)):
        if user_ip[item] == user_index:
            print(f'The {user_ip[item]} is on IndeX {item}')
# find_index()

#Problem 20 : Write a program to find the missing numbers in a list.
def find_missing_numbers():
    users_ip = list(map(int, input('Enter numbers (space-separated): ').split()))
    max_num = max(users_ip)
    min_num = min(users_ip)
    missing_num = [i for i in range(min_num+1,max_num) if i not in users_ip]
    print('Missing Numbers are: ', missing_num)
find_missing_numbers()


