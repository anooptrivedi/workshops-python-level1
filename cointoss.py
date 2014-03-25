import random

heads = 0
tails = 0

for i in range(0, 100):
    result = random.randint(1,2)
    if (result == 1):
        heads +=1
    else:
        tails +=1

print('Head came up:', heads, 'times')
print('Tail came up:', tails, 'times')
