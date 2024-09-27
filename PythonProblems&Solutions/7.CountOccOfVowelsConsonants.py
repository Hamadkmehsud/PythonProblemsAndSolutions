def counter():
    string = input('Enter a string: ')
    vowels_counter = 0
    consonants_counter = 0
    vowels = 'aeiouAEIOU'
    consonants = 'qwrtypsdfghjklmnbvcxzZXCVBNMLKJHGFDSQWRTYP'
    for i in string:
        if i in vowels:
            vowels_counter += 1
        elif i in consonants:
            consonants_counter += 1
    print('Total Vowels in a string: ',vowels_counter)
    print('Total Consonants in a string: ', consonants_counter)
counter()