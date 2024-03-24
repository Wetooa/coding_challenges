import random

print("WELCOME TO MATH TESTER! COMPLETE THE TEST BY REACHING THE REQUIRED SCORE! GETTING A WRONG ANSWER RESETS THE SCORE COUNT AND ADDS ONE ERROR COUNTER! 3 ERROR COUNTERS = FAIL!")
print("CHOOSE AN OPERATOR!")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
score = 0
error = 0
operator = int(input().strip())
print("-----------------------------")
if operator == 1:
    print("MATH TEST (ADDITION)")
    while score < 20:
        if score < 5:
            diff_multiplier = 1
        elif score < 10:
            diff_multiplier = 2
        elif score < 15:
            diff_multiplier = 3
        else:
            diff_multiplier = 4
        num1 = random.randint(1 * diff_multiplier, 20 * diff_multiplier)
        num2 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        answer = input(f"What is {num1} + {num2}: ")
        if int(answer) == num1 + num2:
            score += 1
            print(f"Score: {score}")
        else:
            print("Wrong Answer! Score Resets! Error + 1")
            error += 1
            score = 0
        if error == 3:
            print("TEST FAILED")
            quit()
        print("---------------")
elif operator == 2:
    print("MATH TEST (SUBTRACTION)")
    while score < 20:
        if score < 5:
            diff_multiplier = 1
        elif score < 10:
            diff_multiplier = 2
        elif score < 15:
            diff_multiplier = 3
        else:
            diff_multiplier = 4
        num1 = random.randint(1 * diff_multiplier, 20 * diff_multiplier)
        num2 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        answer = input(f"What is {num1 + num2} - {num2}: ")
        if int(answer) == (num1 + num2) - num2:
            score += 1
            print(f"Score: {score}")
        else:
            print("Wrong Answer! Score Resets! Error + 1")
            error += 1
            score = 0
        if error == 3:
            print("TEST FAILED")
            quit()
        print("---------------")
elif operator == 3:
    print("MATH TEST (MULTIPLICATION)")
    while score < 10:
        if score < 5:
            diff_multiplier = 1
        elif score < 10:
            diff_multiplier = 2
        num1 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        num2 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        answer = input(f"What is {num1} x {num2}: ")
        if int(answer) == num1 * num2:
            score += 1
            print(f"Score: {score}")
        else:
            print("Wrong Answer! Score Resets! Error + 1")
            error += 1
            score = 0
        if error == 3:
            print("TEST FAILED")
            quit()
        print("---------------")
else:
    print("MATH TEST (DIVISION)")
    while score < 10:
        if score < 5:
            diff_multiplier = 1
        elif score < 10:
            diff_multiplier = 2
        num1 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        num2 = random.randint(1 * diff_multiplier, 10 * diff_multiplier)
        answer = input(f"What is {num1 * num2} / {num2}: ")
        if int(answer) == (num1 * num2) / num2:
            score += 1
            print(f"Score: {score}")
        else:
            print("Wrong Answer! Score Resets! Error + 1")
            error += 1
            score = 0
        if error == 3:
            print("TEST FAILED")
            quit()
        print("---------------")
print("THANKS FOR PLAYING!")
print("-----------------------------")