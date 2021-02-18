#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

import math
import time

counter = input("Please enter a numbrer")
float(counter) = str(counter).strip()
while True:
    print(float(counter), end =" ", flush=True)
    float(counter) = counter + counter
    # time.sleep(x) will pause the program at this point for x seconds where x is a float 
    time.sleep(0.1)
    if counter > (float(counter)*12):
       break
print("===================")