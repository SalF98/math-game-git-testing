from basicGame import *
from easyGame import *

# Display a welcome message and prompt the user to select a difficulty level
print("Welcome to the Math Game!")
print("Please select the difficulty level:")
print("1. Basic")
print("2. Easy")
print("3. Medium")
print("4. Hard")

# Prompt the user to select a difficulty level and validate the input

choice = int(input("Enter the number corresponding to your choice (1-4): "))
if choice == 1:
    math_Game_B()
if choice == 2:
    math_Game_E()
