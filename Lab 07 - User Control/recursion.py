import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def linear_search(w,dictionary_list):
    key = w.upper()

    current_list_position = 0

    while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:

        current_list_position += 1

    if current_list_position < len(dictionary_list):
        return

def main():
 
    my_file = open("Lab 07 - User Control/dictionary.txt")
    
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    file = open("Lab 07 - User Control/AliceInWonderLand200.txt")
    
    
    for aline in file:


        word_list = split_line(aline)
        for word in word_list:
            linear_search(word, dictionary_list)
            print(word)                        

   
    my_file.close()



  




main()