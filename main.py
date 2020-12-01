# This program takes a string of text and analyzes the frequency of each letter and plots a chart of it. This is
# entirely for fun!

#This is the text we will be analyzing; as per user input
print("Please type in the text you would like to have analyzed. ")
text = input()

#Dictionary to hold the letters and their respective frequency
letter_count = {}

#for loop to iterate through each character. The letter is not an empty text like I might expect in Java. The keyword
# letter itself tells python to iterate through each letter; no actual definition is not needed. It can be thought of
# as the iterator "i" in a traditional for loop in Java.
for letter in text:
       #for each lower case letter
       letter_count[letter.lower()] = letter_count.get(letter,0) +1

#import packages for graphing
import matplotlib.pyplot as plt

#print
#print(letter_count)
#Separate into two separate items from dictionary and couple them into two variables
#a,b = zip(*letter_count.items())

#plot data and show results
#plt.bar(a,b)
#plt.show()

##A cleaner version of the code is below

#Initialize an empty dictionary
letterCountClean = {}

for k,v in letter_count.items():
       if k.isalpha():
              letterCountClean[k] = v

a,b = zip(*letterCountClean.items())

plt.bar(a,b)
plt.show()


