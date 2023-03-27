import random
my_list = [97,74,8,98,47,62,12,11,0,60]
def selection_sort(my_list):

    for cur_pos in range(len(my_list)):

        min_pos = cur_pos

        for scan_pos in range(cur_pos + 1, len(my_list)):

            if my_list[scan_pos] < my_list[min_pos]:

                min_pos = scan_pos
        print_list(my_list)
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end="")
    print()

my_list = [97,74,8,98,47,62,12,11,0,60]
print_list(my_list)
selection_sort(my_list)
print_list(my_list)
