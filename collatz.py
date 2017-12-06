#!/usr/bin/python3

number = int(input("Enter number to calculate its Collatz conjecture series: "))
iterator = 0

def collatz(n):
    while n > 1:
        if n % 2 == 0:
            new_n = n/2
            print(new_n)
            global iterator
            iterator = iterator + 1
            collatz(new_n)
        else:
            new_n = (n*3) + 1
            print(new_n)
            #global iterator
            iterator = iterator + 1
            collatz(new_n)
        break
    
collatz(number)
print(f"It took {str(iterator)} sequences to reach 1.")
    
