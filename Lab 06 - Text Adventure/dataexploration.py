my_list = [-2, 3, -4, -6]
def detect_positive(list):
    for element in list:
        if element > 0:
            return True
    return False

R = detect_positive(my_list)
print(R)