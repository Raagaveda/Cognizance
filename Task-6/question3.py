import string
import re
words = []
freq_word = ""
freq = 0
with open('about.txt','r') as f:
    contents =f.read()
    string = re.sub('[^a-zA-Z\d\s]', '', contents)
    words=string.split()                               
    print("The words with atleast 6 letters according to the given condition : ")
    for i in range(len(words)):                     
        if len(words[i]) >= 6:                        
            print(words[i])

''' we can also use
for i in range(0, len(words)):
    occur = 1; 
    for j in range(i+1, len(words)):
        if(words[i] == words[j]): 
            occur = occur + 1; 
    if(occur > freq):                       
        freq = occur; 
        freq_word = words[i];'''
'''print("Most repeated word: " + freq_word)
print("Frequency: " + str(freq))'''

freq_word = max(words,key=words.count)                      
print("Most frequently used word is :%s, with no of Occurences : %d"%(freq_word,words.count(freq_word)))
 

