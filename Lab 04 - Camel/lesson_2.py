for x in range(10):
    print("*", end=" ")

print()
for i in range(5):
    print("*", end=" ")
print()
for j in range(20):
    print("*", end=" ")

for x in range(10):
    print()
    for i in range(10):
        print("*", end=" ")
for x in range(10):
    print()
    for i in range(5):
        print("*", end=" ")
for x in range(5):
    print()
    for i in range(20):
        print("*", end=" ")
for row in range(10):
    for column in range(10):
        print(column, end=" ")
    print()
for row in range(10):
    for column in range(10):
        print(row, end=" ")
    print()
for row in range(10):
    for coulmn in range(row+1):
        print(coulmn, end=" ")
    print()
for row in range(10):
    for j in range(row):
        print(" ", end=" ")
    for j in range(10 - row):
        print(j, end=" ")
    print()
for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(" ", end="")
        print(i * j, end=" ")
    print()
for i in range(10):
    
    for j in range(10 - i):
        print (" ", end=" ")
    
    for j in range(1, i + 1):
        print (j, end=" ")
    
    for j in range(i - 1, 0, -1):
        print (j, end=" ")
    
    print()
for i in range(10):
    
    for j in range(10 - i):
        print (" ", end=" ")
    
    for j in range(1, i + 1):
        print (j, end=" ")
    
    for j in range(i - 1, 0, -1):
        print (j, end=" ")
    
    print()
for row in range(10):
    for j in range(row):
        print(" ", end=" ")
    for j in range(10 - row):
        print(j, end=" ")
    print()
for i in range(10):
    
    for j in range(10 - i):
        print (" ", end=" ")
    
    for j in range(1, i + 1):
        print (j, end=" ")
    
    for j in range(i - 1, 0, -1):
        print (j, end=" ")
    
    print()
for i in range(10):
   
    for j in range(i + 2):
        print(" ", end=" ")
   
    for j in range(1, 9 - i):
        print(j, end=" ")
    
    for j in range(7 - i, 0, -1):
        print(j, end=" ")
    print()

