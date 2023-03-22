# -- Put your definition for linear_search right below:
def linear_search():
    
# -- Now if the function works, all these tests should pass:
my_list = [4, 3, 2, 1, 5, 7, 6]
r = linear_search(my_list, 3)
if r == 1:
    print("Test A passed")
else:
    print("Test A failed. Expected 1 and got", r)
r = linear_search(my_list, 2)
if r == 2:
    print("Test B passed")
else:
    print("Test B failed. Expected 2 and got", r)
r = linear_search(my_list, 10)
if r == -1:
    print("Test C passed")
else:
    print("Test C failed. Expected - 1 and got", r)
