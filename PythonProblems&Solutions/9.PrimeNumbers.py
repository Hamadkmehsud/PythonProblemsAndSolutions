def isprime(num):
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_numbers(start, stop):
    for number in range(start, stop + 1):  # 3  9
        if isprime(number):
            print(number)

start_num = int(input('Enter a starting number: '))
stop_num = int(input('Enter a stopping number: '))
prime_numbers(start_num,stop_num)
