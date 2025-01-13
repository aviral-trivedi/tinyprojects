import random
import json
import os 

os.system('cls' if os.name == 'nt' else 'clear')

def set_x(n):
    if n > 0:
        return "." * n
    else:
        return "Invalid input"
    

#Initialisng Variables
strike=0

#Storing The JSON
with open("/home/cleon/Local-Files/Old-Backup/Code Files/VS Code/Learning/ProjectH3ll/words.json", "r") as f:
    words = json.load(f)

#Getting all the list of all the keys in JSON. Then selecting a random index value from it 
genre = list(words.keys())[random.randrange(0, len(words.keys()))]

#Selecting Word From genre
word = words[genre][random.randrange(0, len(genre))]

#More Setup
wordl = len(word)

#UI
flag = int(input("""Welcome User To Hangman
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
|
|_____          
                   
Press 1 to Start
Press 2 to Exit
"""))

os.system('cls' if os.name == 'nt' else 'clear')
dash = set_x(wordl-2)
temp = str(word[0]+dash+word[-1])
hidden = list(temp)
guessed = []


while flag == 1 and strike < wordl+2:

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Your word's genre is {genre}")
    print(f"Total Strikes Availabe {(wordl+2)-strike}")

    for i in hidden: print(i,end="",sep="")
    print()

    print("\nAlready Guessed:",end="",sep="")
    for i in guessed: print(i,end="",sep="")
    
    guess_word = input("\nEnter Guess ")

    if guess_word not in word:
        guess = False
        guessed.append(guess_word)
        print(f"INCORRECT! Strikes: {strike}")
    else:
        guess = True
        for i in range(len(word)):
            if word[i].lower() == guess_word.lower():
                hidden[i] = guess_word
        
    if guess:
        pass
    else:
        strike+=1
    
    if hidden == list(word):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("WIN WIN WIN")
        print(word)
        break


#To Do-
#The rules are simple; a player writes down the first and last letters of a word and another player guesses the letters in between
#Bag of Words |DONE|
#Selected At random |DONE|
#Displays category as well |DONE| 
#Chances - word length +2 |DONE|
#Check if guess correct |DONE|
#If guess correct don't give strike |DONE|
#If guess correct update the visible word |DONE|
