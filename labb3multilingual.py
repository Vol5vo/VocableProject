#double words, one meaning? like "bye bye" for english and yet theres a space in between


#a way to make it ignore special letters? can we write hejdå as hejda isntead and its a valid answer? 
#teacher said make a dictionary and check for every letter of a word with a for statement and then add the letters to the
#newly made word (like newWord += letter) going from Å -> A, and Ä -> A etc,
# # but to make it from A -> Ä or A -> Å
#she said to compare the input with the answer key (?) 
#idk if this means also making a dictionary where every weird letter gets converted ("snälla":"snalla") or what...
#she also said to use this for my final assignment because she liked the idea :D
#
# howd it work with russian? привет as privet? make letters equal eachother?


#categories before starting the quiz?
#lowercase and strip for inputs
# 
#
#


import random
Filepath = "C:\Users\molov\OneDrive\Documents\DEV\pythonprog\vocables.txt"

def read_from_file(filename, index): #add another thingie for the index
    dict_vocables = {}
    with open(filename, "r", encoding="utf-8") as infile:
        for row in infile: #how to ignore faulty lines?//lines where i write comments in the dictionary
            main_vocable, translated_vocable = row.split("," , 1)
            dict_vocables[main_vocable.strip()] = translated_vocable.strip()
    return dict_vocables
            
def start_quiz(dict_vocables, amount_choice_):
    correct_score = 0
    word_list = dict_vocables.keys()
   
    for i in range(amount_choice_):
        language_index = random.randint(0,4)
        print(f"{word_list[i]}")



def main():
    print("""
<<<<<Time for your vocable quiz!>>>>>

What language do you wanna be tested in?
1. English 
2. Svenska
3. Türkçe
4. Русский
5. Français
6. Arabi
7. Fully randomized
""")
    language_choice = input("Choice: ")

    print("""
How many words do you wanna be quizzed in? 
1
5
10
20
All
""")
    amount_choice = input("Choice: ")

    dict_vocabs_ = read_from_file(Filepath, language_choice)

main()
