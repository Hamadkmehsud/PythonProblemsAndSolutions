#Problem 7: write  a program that can fetch words with even number of character
from sqlalchemy.sql.operators import lshift
def even_words():
    input_str = input('Enter a sentence :')
    lst = input_str.split(' ')
    even_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            even_lst.append(i)
    print(even_lst)
# even_words()

def even_words2():
    input_str = input('Enter a sentence :')
    lst = input_str.split(' ')
    even_lst = [i for i in lst if len(i) % 2 == 0]
    print(even_lst)
# even_words2()

#Problem 8: write a program that can fetch words by capital letters
def fetch_by_capital():
    input_st = input('Enter a Sentence :')
    words = input_st.split()
    lst = []
    for i in words:
        print(i)
        if i[0].isupper():  #and i[0].lower() in 'aeiou':
            print(i[0])
            lst.append(i)
    print(lst)
# fetch_by_capital()

#Problem 8: write a program that can fetch words starting and ending with vowels
def start_end_vowels():
    input_st = input('Enter a Sentence :').lower()
    words = input_st.split()
    vowels = 'aeiou'
    lst = []
    for i in words:
        if i[0] in vowels and i[-1] in vowels: #not in vowels: those starting and not with vowels  #and i[0].lower() in 'aeiou':
            lst.append(i)
    print(lst)
# start_end_vowels()

#we can also do this in one line
# input_user = input('enter sentence :').lower()
# input_user.split()
# print([i for i in input_user.split() if i[0] in 'aeiou' and i[-1] in 'aeiou'])

#Problem 8: write a program that can fetch all vowels from a given string
def fetch_vowels():
    input_st = input('Enter a Sentence :').lower()
    vowels = 'aeiou'
    lst = []
    for i in input_st:
        if i in vowels:
            lst.append(i)
    print(lst)
# fetch_vowels()

#Problem 9: write a program that can fetch first character of each word in a given string
def fetch_first_ch():
    input_st = input('Enter a Sentence :').lower()
    print([i[0] for i in input_st.split()])
fetch_first_ch()