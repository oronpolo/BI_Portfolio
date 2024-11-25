#   This program will find the word that appears the most in Alice's Adventures in Wonderland
from useful_func import *

def clean_Alice(txt:str):
       text = ToLower(txt)
       text_index = 1
       #while(text_index != -1):
       #      text = text.replace("  ", " ")
       #      text_index = text.find("  ")
       #Clean_text ="".join(c for c in text if c == " " elif c.isalpha())
       #txt ="".join(c for c in txt if c.isalpha())
       #return Clean_text
        #clean_a()
        #clean_b()

def count_words_in_Alice():
        print('count Alice')
    
   

#print(read_Alice_text("D:/OneDrive/studies/Bar-Ilan/pyton/BI-Python/alice_in_wonderland.txt"))



Alice_Path = 'D:\\OneDrive\\studies\\Bar-Ilan\\pyton\\BI-Python\\alice_in_wonderland.txt'

def main_count_Alice():
    Alice_text = read_txt_file_content(Alice_Path)
    #Alice_words = clean_Alice(Alice_text)
    #(words_dict, max_word_count) = count_words_in_Alice(Alice_words)
    print(Alice_text)
    Alice_text = Alice_text.split
    print(Alice_text)

#main_count_Alice()


print(clean_Alice("@!A  bCd   Ef      G$%^"))
txt = "@!A  bCd   Ef      G$%^".split()
#txt = str(txt)
print(type(txt))


    





