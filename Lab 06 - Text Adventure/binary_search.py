# -- Put your definition for binary_search right below:
# --- Binary search
def binary_search(my_list, key): 
    
    lower_bound = 0
    upper_bound = len(my_list)-1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    while lower_bound <= upper_bound and not found:

        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
            return(middle_pos)
    return(-1)


# -- Now if the function works, all these tests should pass:
my_list = [0, 3, 5, 12, 18, 50, 70, 78]
r = binary_search(my_list, 3)
if r == 1:
    print("Test A passed")
else:
    print("Test A failed. Expected 1 and got", r)
r = binary_search(my_list, 5)
if r == 2:
    print("Test B passed")
else:
    print("Test B failed. Expected 2 and got", r)
r = binary_search(my_list, 10)
if r == -1:
    print("Test C passed")
else:
    print("Test C failed. Expected - 1 and got", r)