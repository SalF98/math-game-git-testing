import random


# Randomly select an operator and a random number between 1 and 100
def math_Basic_Generator():
    operators = ['+', '-']
    operator = random.choice(operators)

    num1 = random.randint(1, 30)
    num2 = random.randint(1, num1) if operator == '-' else random.randint(1,30)

    return num1, num2, operator


# Calculate the correct answer based on the operator
def math_Basic_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2


def math_Game_B():
    print("Welcome to the math game at the easy difficulty level. You will be presented with questions involving addition and subtraction, which may include negative number results.")
    points = 0

    while True:
        num1, num2, operator = math_Basic_Generator()
        correct_answer = math_Basic_answer(num1, num2, operator)

        print(f"What is {num1} {operator} {num2}?")
        user_answer = int(input("Answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            points += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            break

    print(f"You scored {points} points.")
