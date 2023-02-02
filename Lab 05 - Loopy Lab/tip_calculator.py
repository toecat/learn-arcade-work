def tip_calculator():
    cost = int(input("What is the cost of your meal? "))
    tip = int(input("What is the tip percentage that you would like? "))
    print("The total cost of your meal will be", "$",((tip / 100) * cost) + cost)

tip_calculator()
