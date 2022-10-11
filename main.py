
# ******************************
# Make your Code
# ******************************
# Sarah Castorena
# SID 2028049
import random
numbers = []
count = 0
while count < 10:
    random.seed()
    randNum = random.randint(1,100)
    numbers.append(randNum)
    count = count + 1
minNum = min(numbers)  
minIndex = numbers.index(minNum)  
print(minNum)
print(minIndex)