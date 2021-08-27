import math
print('\n')
num = int(input('Please enter the number you want to check the range up to: '))
print('\n')
for x in range(2 , num+1) :
    for i in range (2 , int(math.sqrt(x)+1)) :
       if x % i == 0 :
           break
    else :
        if num % x == 0 :
            print(f'{x} is one of our prime divisors ^-^\n')
