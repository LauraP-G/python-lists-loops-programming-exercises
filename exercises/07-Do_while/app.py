# Your code here
number = 20

while number >= 0:
    if (number == 0):
        print('LIFTOFF')
        number-=1

    elif(number % 5 ==0):
        print(f'{number}!')
        number-=1
        
    else:
        print(number)
        number-=1