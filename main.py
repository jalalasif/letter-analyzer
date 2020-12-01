# This program takes a string of text and analyzes the frequency of each letter and plots a chart of it. This is
# entirely for fun!

#This is the text we will be analyzing
text = "“The biggest component in any human, filling 61 percent of available space, is oxygen. It may seem a " \
       "touch counterintuitive that we are almost two-thirds composed of an odorless gas. The reason we are not " \
       "light and bouncy like a balloon is that the oxygen is mostly bound up with hydrogen (which accounts for " \
       "another 10 percent of you) to make water—and water, as you will know if you have ever tried to move a " \
       "wading pool or just walked around in really wet clothes, is surprisingly heavy. It is a little ironic " \
       "that two of the lightest things in nature, oxygen and hydrogen, when combined form one of the heaviest, " \
       "but that’s nature for you. Oxygen and hydrogen are also two of the cheaper elements within you. All " \
       "your oxygen will set you back just $14 and your hydrogen a little over $26 (assuming you are about the " \
       "size of Benedict Cumberbatch). Your nitrogen (2.6 percent of you) is a better value still at just forty " \
       "cents for a body’s worth. But after that it gets pretty expensive."

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
print(letter_count)
#Separate into two separate items from dictionary and couple them into two variables
a,b = zip(*letter_count.items())

#plot data and show results
plt.bar(a,b)
plt.show()

##A cleaner version of the code is below

#Initialize an empty dictionary
letterCountClean = {}


