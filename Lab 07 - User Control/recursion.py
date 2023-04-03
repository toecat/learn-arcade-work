import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)



def main():
 
    my_file = open("Lab 07 - User Control/dictionary.txt")

    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    #print (dictionary_list)
    list_position = linear_search(my_file)

    if list_position < len(word_list):
        print("The name", my_file, "is at position", list_position)
    else:
        print("The name", my_file, "was not in the list.")

    my_file.close()



    file = open("Lab 07 - User Control/AliceInWonderLand200.txt")
    for aline in file:


        word_list = split_line(aline)
        for word in word_list:



                def linear_search():
                    current_list_position = 0

                    while current_list_position < len(word) and dictionary_list[current_list_position] != word:
                        current_list_position += 1

                        return current_list_position
                    print (dictionary_list[current_list_position], " " , word)
                    current_list_position += 1
                    if current_list_position < len(word_list):
                        current_list_position += 1
                    else:
                        print("The name was not in the list, ", word)





main()