import random
for i in range(50):
    x = random.randrange(0, 100)
    heads = 0
    tails = 0
    if x> 50:
        heads=+1
    if x<50:
        tails=+1
if heads>tails:
    print("Heads won")
if tails>heads:
    print("Tails won")        