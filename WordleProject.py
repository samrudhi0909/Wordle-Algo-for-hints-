#!/usr/bin/env python
# coding: utf-8

# In[36]:


import itertools    #requried for iterating dictonary
frequency = {}
with open("H:\\MyProjectWork\\NLP\\Wordle-Project\\All-5-Letter-Words.txt") as file :
          words = file.readlines()
        
words = [x.strip() for x in words] #remove newline character from each element of word-list

for word in words : #each letter occurs in how many words
    for letter in word :
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
            
frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1],reverse = True)}#sort 

word_score = {}

#key - word , value - word with not repeating letters
non_repeat = {}
for word in words:
    temp = ""
    for letter in word:
            if not letter in temp:
                temp  += letter
    non_repeat[word] = temp
        
#calculate word score of each word
#word _score = sum of frequencies of each non-repeating letter in word
for word in words:
    for letter in non_repeat[word]:
        if word in word_score:
            word_score[word] += frequency[letter]
        else:
            word_score[word] = frequency[letter]
            
#word_score in descending order
word_score = {k: v for k, v in sorted(word_score.items(), key = lambda item : item[1],reverse = True)}
        
#calulate the percentage probability of each word
for word in words :
    word_score[word] = "{:.1f}".format((word_score[word] / 12215) * 100)


#print("% probability of each word in descending order: ")
#for keys,values in word_score.items():
    #print(str(keys) + ": " + str(values) + "%")
flag = 0
common = input("Enter common letters to get possible words: ")
not_in = input("Enter letters which are not present: ")
hint_list = {}
for word in words: 
    for each_letter in common:
        if (each_letter in word):
            flag = 1
            continue
        else : 
            flag = 0
            break
    if flag == 1:
        for w in word:
            if w in not_in:
                flag = 0
                break
    if flag == 1:
        hint_list[word] = word_score[word]
    flag = 0

hint_list = {k: v for k, v in sorted(hint_list.items(), key = lambda item : item[1],reverse = True)}  
hints = input("How many hints do you want? ")
print("\n>>This is the hint list with highest possibility at top: ")
if(hints.lower() == "all"):
    for keys,values in hint_list.items():
        print(str(keys) + ": " + str(values))
else:
    x = itertools.islice(hint_list.items(), 0, int(hints))
    for keys,values in x :
        print(str(keys) + ": " + str(values))






