# Function of program: To cheese the NYTimes spelling bee puzzle
# https://www.nytimes.com/puzzles/spelling-bee
# Date: 4/14/2022


with open("dictionary.txt", "r") as f:
   words = f.readlines()

def wordFinder(letterList):  
   
   potentialWords = []
   
   
   for word in words:
      word = word.rstrip()
      
      if len(word) < 4:
         continue
         
      # Checks if specified letters are in the word
      contains = 0
      for letter in list(word):
         if letter in letterList:
            contains += 1
            

      if (contains == len(word)) and (letterList[0] in word):
         potentialWords.append(word)

   return potentialWords



# Input

x = input("Input given letters, with the required letter being first: ").lower()
wordList = wordFinder(x)

print()
print(str(len(wordList)) + " satisfactory words found.")
print(wordList)


exit = input("\n\n[Enter] to exit.")