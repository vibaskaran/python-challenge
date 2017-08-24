import os
import csv
import re 

paragraph = input("Please enter the paragraph ")

#Sentences = re.split("(?&lt;=[.!?]) +", paragraph)
Sentences = paragraph.split('.')
#print(len(Sentences))
#average_sentence = sum(len(word) for word in Sentences) / len(Sentences)
average_sentence = sum(len(x.split()) for x in Sentences) / len(Sentences)
#print(average_sentence)
words = paragraph.split(' ')
#print(len(words))
average_words = sum(len(word) for word in words) / len(words)
#print(average_words)

print()
print('Paragraph Analysis')
print('------------------')
print('Approximate Word Count: '+str(len(words)))
print('Approximate Sentence Count: '+str(len(Sentences)))
print('Average Letter Count: '+str(round(average_words,2)))
print('Average Sentence Length: '+ str(round(average_sentence,2)))
print()