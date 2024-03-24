import random
import time
from threading import *

class Timer(Thread):
    def __init__(self, timer):
        self.timer = timer

    def run(self):
        while self.timer != 0:
            time.sleep(1)
            self.timer -= 1
        
timer = 10
score = 0

tf = Timer()
tf.start(timer) # how to make this run parallel to the block of code below???

while score != 10 and timer != 0:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = input(f"What is {num1} + {num2}: ")
    try: # for exception handling
        int(answer)
    except:
        print("Wrong Input!") 
        print(f"Score: {score}") 
    else: 
        if int(answer) == num1 + num2:
            score += 1
        print(f"Score: {score}")
        
    
print("Success!!")
    
