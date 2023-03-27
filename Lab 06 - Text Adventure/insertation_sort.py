def insertion_sort(my_list):
 
    for key_pos in range(1, len(my_list)):

        key_value = my_list[key_pos]

        scan_pos = key_pos - 1

        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        my_list[scan_pos + 1] = key_value
        print_list(my_list)

def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end="")
    print()
my_list = [74,92,18,47,40,58,0,36,29,25]

insertion_sort(my_list)
print_list(my_list)