import random


# Randomly select an operator and a random number between 1 and 100
def math_Easy_Generator():
    operators = ['+', '-']
    operator = random.choice(operators)

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    return num1, num2, operator


# Calculate the correct answer based on the operator
#Todo: make most of the results be close to zero.
def math_Easy_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2


def math_Game_E():
    print("\nDifficulty: Easy\nOperators: + and -\nNegative results: Yes")
    points = 0

    while True:
        num1, num2, operator = math_Easy_Generator()
        correct_answer = math_Easy_answer(num1, num2, operator)

        print(f"What is {num1} {operator} {num2}?")
        user_answer = int(input("Answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            points += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            break

    print(f"You scored {points} points.")
