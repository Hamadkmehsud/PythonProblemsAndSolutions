#Probblem 10: Write a program that can fetch all the special characters from a string

def special_ch():
    user_ip = input('Enter a string :')
    s_ch = """~!@#$%^&*()_+{}[];'":?/>,<.\\|"""
    print([item for item in user_ip if item in s_ch])
# special_ch()

#solution2
import string
def special_ch_2():
    user_ip = input('Enter a string :')
    s_ch = string.ascii_letters
    s_di = string.digits
    print([item for item in user_ip if item not in s_ch and item not in s_di and item != ' '])
# special_ch_2()

#Probblem 11: Write a program that can convert all the string in PascalCase
def Pascal_Case():
    user_ip = input('Enter a string :').lower()
    words = user_ip.split()
    # st = ''
    st = ''.join([i.capitalize() for i in words])
    # for i in words:
    #     st+=i.capitalize()
    print(st)
# Pascal_Case()

#Probblem 12: Write a program that revers string

def reverse_string():
    user_ip = input('Enter a string :').lower()

    reverse = reversed(user_ip)
    rev_st = ''.join(reverse)
    print(rev_st)
# reverse_string()

#Solution2
def reverse_st():
    user_ip = input('Enter a string :').lower()
    reverse = user_ip[::-1]
    print(reverse)
# reverse_st()
#Solution 3
def rev_st():
    user_ip = input('Enter a string :').lower()
    empty_st = ''
    for i in user_ip:
        empty_st = i+ empty_st
    print(empty_st)
# rev_st()

#Probblem 13: Write a program that convert a string into snake_case
def snake_case_convert():
    st = input("Enter a string: ")
    print(st.replace(' ', '_'))
# snake_case_convert()

#Solution2
def snake_case():
    st = input("Enter a string: ")
    str_s = '_'.join(st.split())
    print(str_s)
# snake_case_convert()
#Solution3 without default functions
def snake_c():
    st = input("Enter a string: ")
    empty_string = ''
    for i in st:
        if i == ' ':
            empty_string+='_'
        else:
            empty_string+=i
    print('string:',empty_string)
# snake_c()

#Probblem 13: Write a program to sort given string in a asc order
def string_order_asc():
    input_io = input("Enter a string: ")
    a = ''.join(sorted(input_io))
    print(a)
# string_order_asc()

#Probblem 13: Write a program to sort given string in a dec order
def string_order_dec():
    input_io = input("Enter a string: ")
    a = ''.join(sorted(input_io, reverse=True))
    # dec_order = a[::-1]
    print(a)
# string_order_dec()

#Probblem 14: Write a program to sort given words in given string
def string_order_words():
    input_io = input("Enter a string: ")
    order = input_io.split()
    print(' '.join(sorted(order)))
# string_order_words()
#Solution2
def string_order_words2():
    input_io = input("Enter a string: ")
    st = ''
    for i in input_io.split():
        st = i + ' '+st
    print(st)
# string_order_words2()

#Problem 15: Write a program to swap cases in a given string
def swap_case():
    user_ip  = input('Enter a string: ')
    print(user_ip.swapcase())
# swap_case()

#Solution2
def swap_case2():
    user_ip  = input('Enter a string: ')
    swap = ''
    for i in user_ip:
        if i.isupper():
            swap = swap + i.lower()
        else:
            swap =swap +i.upper()
    print(swap)
swap_case2()