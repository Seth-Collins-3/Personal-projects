import random

string = "did you just flash kick?"
result = ""
for i in range(len(string)):
    rand = random.randint(1,2)
    if rand == 1:
        result = result + string[i].lower()
    else:
        result = result + string[i].upper()

print(result)
