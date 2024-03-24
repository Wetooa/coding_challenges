from threading import * # module for multi threading
import time
import random

class Timer(Thread):
    def run(self):
        timer = 10
        while timer != 0:
            time.sleep(1)
            timer -= 1
        print("\nTest is over!")
        return quit()

class Test(Thread):
    def run(self):
        score = 0
        while score != 5:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            u_answer = input(f"What is {num1} + {num2}: ")
            try: # for exception handling
                int(u_answer)
            except:
                print("Wrong Input!") 
                print(f"Score: {score}") 
            else: 
                if int(u_answer) == num1 + num2:
                    score += 1
                print(f"Score: {score}")
        print("Test is Over! You got a perfect score!")
        return quit()


test_time = Timer()
test = Test()

test_time.start() # .start is used instead of .run to use multi threading i guess
test.start()
