names = ["Chloe", "Kate", "Sloane", "Max", "Grace"]

for item in names:
    print(item)

for name in names:
    print("Hello,", name, "you have been invited to my dinner party")    
print()
names.append("Elvis")
names.append("George Washingtion")
names.append("Thomas Eddison")
for x in names:
    print("Hello,", x, "you have been invited to my dinner party.")
popped_dinner = names.pop()
print(popped_dinner)
names.insert(3, "Albert Einstein")
for name in names:
    print("Hello,", name, "you have been invited to my dinner party") 

print()
names.insert(0,"Grandpa")
names.insert(5,"Grandma")
names.append("Dog")
for name in names:
    print("Hello,", name, "you have been invited to my dinner party")

print("My new dinner table wont arrive in time so I can only invite 2 of you.")
#print(names)
x = len(names)
#print(x)
while x > 2:
    popped_dinner=names.pop()
    print("Sorry,", popped_dinner,"I ran out of room for you at my party.")
    x-=1
for name in names:
    print("Hello,", name, "you have still been invited to my dinner party.")
del(names)