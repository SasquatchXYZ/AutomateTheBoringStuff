import random

heads = 0
tails = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    else:
        tails += 1
    if i == 500:
        print(f'Halfway done: {heads} heads and {tails} tails.')

print(f'Complete: Heads came up {heads} times - tails {tails} times.')
