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

answer = int(input("How old is Tovah? "))
if answer == 14:
    print("Correct")
    correct +=1
    print(correct)
else:
    print("No")
    print(correct)
print()

answer = str(input("Which football team is my favorite? "))
if answer.lower() == "packers":
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()

answer = str(input("Who won the superbowl? "))
if answer.lower() == "chiefs":
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()

answer = int(input("How many points did the Chiefs win by? "))
if answer == 3:
    print("Correct")
    correct += 1
    print(correct)
else:
    print("No")
    print(correct)
print()

total = (correct/5)*100
print("You got", total, "% of the questions correct, good job!")
