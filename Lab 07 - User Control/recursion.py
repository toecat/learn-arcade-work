import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
 
    my_file = open("Lab 07 - User Control/dictionary.txt")

    dictionary_list = []
    for line in dictionary_list:
        line = line.strip()
        dictionary_list.append(line)

    my_file.close()


main()