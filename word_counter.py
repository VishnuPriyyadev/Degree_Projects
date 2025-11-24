# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 08:37:22 2025

@author: vishn
"""

    
def word_counter(file, delimiter=" "):
    """Function counts the frequency of words in the txt.file till line starts with "finish"
    
    The function opens and reads the file lines. If the first word on the line
    starts with the word finish, the file should close and return a dictionary
    that has keys of individual words with a value for the number of times the
    word appears as integers.
    
    Parameters:
        file (str): The path and text file name is used
        delimiter (str, optional): The character that separates each word in the 
                                  file (by default its a space)
        
    Returns:
        dict: A dictionary that has keys of individual words with a value for the 
              number of times the word appears as integers before the word "finish"
    """

    wordcount = {}
    
    with open(file, "r") as myfile:
        for line in myfile:
 
           words = line.strip().split(delimiter)
           
           if words and words[0] == "finish":
               break
            
           for word in words:
               if word.isalpha() and word.islower():
                    if word in wordcount:
                        wordcount[word] += 1
                    else:
                        wordcount[word] = 1
                    
    return wordcount

if __name__ == "__main__":
    result = word_counter(r"C:\Users\vishn\Downloads\CODING YR 2\word_counter task 2\words.txt")
    print(result)
        
        
 
 