
input_user = int(input('Enter the factorial number: '))
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        # print(i)
        fact *= i
    print(fact)
# factorial(input_user)

def fact_rec(num):
    if num == 1:
        return 1
    else:
        return fact_rec(num-1) * num
# print(fact_rec(5))

def factors_num(num):
    for i in range(1, num + 1):
        print(i ,end=' * ')

factors_num(6)