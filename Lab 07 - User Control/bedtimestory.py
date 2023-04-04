animal_list = ["sloth", "dolphin", "turtle"]

def story(animal_list,x,y):
    print("The", animal_list[x], "is sleepy so it slept in the", animal_list[y],"bed")
    x+=1
    y+=1
    print(x)
    print(y)
story(animal_list, 0, 1)

