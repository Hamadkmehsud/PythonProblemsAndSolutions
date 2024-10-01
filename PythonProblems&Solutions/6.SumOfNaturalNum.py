def sum_natural_num():
    natural_num = int(input('Enter natural numbers upto: '))
    summ = 0
    for numb in range(1,natural_num+1):
        summ = summ + numb
    print(sum)
# sum_natural_num()

#Solution 2
number = int(input('Enter a number upto: '))
sum = 0
while number > 0:
    sum+= number
    number-=1
print(sum)


#Solution 3
num = int(input('Enter a number upto: '))
def sum_natural(num):
    if num == 1:
        return 1
    else:
        return num + sum_natural(num-1)
print(sum_natural(num))
