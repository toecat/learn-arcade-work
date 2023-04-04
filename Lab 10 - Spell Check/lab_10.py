import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def linear_search(w,dictionary_list):
    current_list_position = 0
    while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != w.upper():
        current_list_position += 1
    if current_list_position < len(dictionary_list):
        return(current_list_position)
    else:
        return(len(dictionary_list)+1)


def binary_search(w, dictionary_list):
    lower_bound = 0
    upper_bound = len(dictionary_list)-1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        if dictionary_list[middle_pos] < w.upper():
            lower_bound = middle_pos + 1
        elif dictionary_list[middle_pos] > w.upper():
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        return(middle_pos)
    else:
        return(len(dictionary_list)+1)


def main():
    my_file = open("Lab 07 - User Control/dictionary.txt")
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    print("--- Linear Search ---")
    file = open("Lab 10 - Spell Check/AliceInWonderLand200.txt")
    line_num = 1
    for aline in file:
        word_list = split_line(aline)
        for word in word_list:
            result = linear_search(word, dictionary_list)
            if result==len(dictionary_list)+1:
                print("line ", line_num, "possible misspelled word: ", word)
        line_num+=1
    my_file.close()
    print("--- Binary Search ---")
    file = open("Lab 10 - Spell Check/AliceInWonderLand200.txt")
    line_num = 1
    for aline in file:
        word_list = split_line(aline)
        for word in word_list:
            result = binary_search(word, dictionary_list)
            if result==len(dictionary_list)+1:
                print("line ", line_num, "possible misspelled word: ", word)
        line_num+=1
    my_file.close()


main()
