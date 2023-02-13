correct = 0
print("Take my quiz")
print()
answer = str(input('What is my name? '))
if answer.lower() == "tovah":
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()
answer = int(input("How many states are there in the U.S.? "))
if answer == 50:
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()
answer = str(input("Which state has the largest population? "))
if answer.lower() == "california":
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()
answer = int(input("How old am I? "))
if answer == 14:
    print("Correct")
    correct +=1
    print(correct)
else:
    print("No")
    print(correct)
print()
answer = str(input("What is the best season? "))
if answer.lower() == "summer" or answer.lower() == "spring" or answer.lower() == "fall":
    print("Yes")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()
total = correct/5*100
print("You got", total, "% of the questions correct, good job!")