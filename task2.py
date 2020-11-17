#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math 
number=input("Enter number")
number=float(number)
a=str(number)
if math.sqrt(number)%1==0 and round(number**(1.0/3),8)%1==0:
    
    
    print(""+a+" "+"is both a perfect square and a perfect cube.")
elif math.sqrt(number)%1==0:
    print(""+a+" "+"is only a perfect square.")
elif number**(1.0/3)%1==0:
    number=round(number,8)
    print(""+a+" "+"is only a perfect cube.")
