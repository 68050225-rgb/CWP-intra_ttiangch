#!/usr/bin/env python3

n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))
a = n1*n2
if a > 0:
    print("The result is positive.")
elif a < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
    
print(n1,'x',n2,'=',a)