from basicGame import *
from easyGame import *
from mediumGame import *

print("Welcome to the Math Game!")
print("Please select the difficulty level:")
print("1. Basic")
print("2. Easy")
print("3. Medium")
print("4. Hard")

choice = int(input("Enter the number corresponding to your choice (1-4): "))
if choice == 1:
    math_Game_B()
if choice == 2:
    math_Game_E()
if choice == 3:
    math_Game_M()
