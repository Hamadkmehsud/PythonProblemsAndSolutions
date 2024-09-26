a = 10
b = 30
print(f'before swapping value of a has: {a} and b: {b}')
a,b = b, a
print(f'After swapping value of a is: {a} and b: {b}')

x = 100
y = 99
print(f'before swapping value of x has: {x} and y: {y}')
x = x+y
y = x-y
x = x-y
print(f'After swapping value of x is: {x} and y: {y}')

