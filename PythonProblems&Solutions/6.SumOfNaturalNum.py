def sum_natural_num():
    natural_num = int(input('Enter natural numbers upto: '))
    sum = 0
    for num in range(1,natural_num+1):
        print(num)
        sum = sum + num
    print(sum)
# sum_natural_num()

number = int(input('Enter a number upto: '))
sum = 0
while number > 0:
    sum+= number
    number-=1
print(sum)
