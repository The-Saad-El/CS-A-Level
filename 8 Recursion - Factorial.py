# Factorial


def factorial(num):
    if num == 0:   #base case
        return 1
    else:  
        return num * factorial(num-1)   #general case
        
num = int(input("Enter the Number: "))
print(f'The Factorial of {num} is {factorial(num)}')
