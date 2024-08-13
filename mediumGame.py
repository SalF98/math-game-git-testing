import random


# Randomly select an operator and a random number between 1 and 100
def math_Medium_Generator():
    operators = ['+', '-', '*']
    operator = random.choice(operators)

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    return num1, num2, operator


# Calculate the correct answer based on the operator
def math_Medium_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def math_Game_M():
    print("\nDifficulty: Medium\nOperators: +, - and *\nNegative results: Yes")
    points = 0

    while True:
        num1, num2, operator = math_Medium_Generator()
        correct_answer = math_Medium_answer(num1, num2, operator)

        print(f"\nWhat is {num1} {operator} {num2}?")
        user_answer = int(input("Answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            points += 1
        else:
            print(f"\nIncorrect! The correct answer is {correct_answer}.")
            break

    print(f"You scored {points} points.")
