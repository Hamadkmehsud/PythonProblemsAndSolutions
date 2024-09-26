# Problem 1: write a program that can count the numbers of given string
def count_str():
    st = input("Enter a string :")
    counter = 0
    for i in st:
        if i != " ":
            counter+= 1
    print(counter)
# count_str()

#Problem 2: write a program that can count the words in given string
def count_words():
    st = input("Enter a Sentence :")
    counter = 1
    for i in st:
        if i == " ":
            counter+= 1
    print(counter)
# count_words()

#another way with split
def words_split():
    st = input("Enter a Sentence :")
    lst = st.split(' ')
    # print(a)
    counter = 0
    for i in lst:
        counter+= 1
    print(counter)
# words_split()

#Problem 3: write a program that can count the Upper case in given string
def upper_count():
    st = input("Enter a Sentence :")
    count = 0
    for i in st:
        if i.isupper():
            count += 1
    print(count)
# upper_count()

#Problem 4: write a program that can count the vowels in given string
def vowels_count():
    st = input("Enter a Sentence :")
    vowels = 'aeiou'
    count = 0
    lst = []
    for i in st:
        if i.lower() in vowels:
            lst.append(i)
            count += 1
    print(f"Vowels in Sentence : {lst}")
    print(f"Number of vowels : {count}")
# vowels_count()

#Problem 5: write a program that count occurrences of each vowel
def occ_vowels():
    st = input("Enter a Sentence :")
    counta = 0
    counte = 0
    counti = 0
    counto = 0
    countu = 0
    for i in st:
        if i.lower() == 'a':
            counta += 1
        elif i.lower() == 'e':
            counte += 1
        elif i.lower() == 'i':
            counti += 1
        elif i.lower() == 'o':
            counto += 1
        elif i.lower() == 'u':
            countu += 1
    print('a :', counta)
    print('e :', counte)
    print('i :', counti)
    print('o :', counto)
    print('u :', countu)
# occ_vowels()

#the upper code leads us to a correct result, but we don't code like this in python due to the redundancy
#now we will use dictionary
def occ_vowels_dic():
    st = input("Enter a Sentence :").lower()
    vowels = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in st:
        if i in vowels:
            # print(i)
            # print(vowels[i])
            vowels[i] += 1
    for vowel, count in vowels.items():
        print(vowel,':',count)
# occ_vowels_dic()

#another solution
def occ_dic_vow():
    st = input("Enter a Sentence :").lower()
    vowels = 'aeiou'
    d = {}.fromkeys(vowels,0)
    for i in st:
        if i in d:
            d[i]+= 1
    print(d)
# occ_dic_vow()

#Problem 6: write a program that count occurrences of unique character in a string
def unique_occ():
    st = input("Enter a Sentence :").lower()
    my_set = set()
    for i in st:
        my_set.add(i)
    dic = {}.fromkeys(st, 0)
    for i in st:
        dic[i]+=1
    print(dic)
    print(my_set)
# unique_occ()

#solution2
def unique_occ2():
    st = input("Enter a Sentence :").lower()
    lst = []
    for i in st:
        if i not in lst:
            lst.append(i)
    print(lst)
# unique_occ2()