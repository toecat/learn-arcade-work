my_list = [97,74,8,98,47,62,12,11,0,60]
def selection_sort(my_list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:

                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
finish = selection_sort(my_list)
print(finish)