import random  #Imports for the project
import time

Score1 = 0  #setting variables to be used in the code
Score2 = 0
Rounds = 0
Dice1 = 0
Dice2 = 0


def login():
    username = input(
        "Enter your username: ").strip()  #Removing extra spaces to raw text
    password = input("Enter your password: ").strip()

    with open("Logins.txt", "r") as f:  #Opening text file in read
        for line in f:
            loginInfo = line.strip().split(
                ",")  #splitting and removing the , from the text file
            if username == loginInfo[0] and password == loginInfo[
                    1]:  #checking if the password and username matches
                return True  #returning result
        return False


if login():
    input("Correct login \n Press any key to continue: ")
else:
    print("Wrong login exiting...")
    time.sleep(2)
    quit()

print("Rolling Player 1's dice...")
time.sleep(2)

while Rounds != 5:
    Rounds = Rounds + 1
    Dice1 = random.randint(1, 6)
    #Using random int for getting an int inside of a range simulating random dice roll
    Dice2 = random.randint(1, 6)
    RoundTotal = Dice1 + Dice2
    Score1 = Score1 + RoundTotal
    if Score1 % 2:  #Check if score1 is odd or even
        Score1 = Score1 + 10
    else:
        Score1 = Score1 - 5
    if Dice1 == Dice2:
        Score1 = Score1 + random.randint(1, 6)
    else:
        pass
    if Score1 < 0:
        Score1 = 0
    else:
        pass
    print(Score1)
    #Printing per dice roll score
    time.sleep(0.5)
print("Player 1 score = ", Score1)
#Printing final score for the player

Rounds = 0  #Resetting round variable for the second player

time.sleep(1)
print("Rolling player 2's dice...")
time.sleep(2)

while Rounds != 5:
    Rounds = Rounds + 1
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    RoundTotal = Dice1 + Dice2
    Score2 = Score2 + RoundTotal
    if Score2 % 2:
        Score2 = Score2 + 10
    else:
        Score2 = Score2 - 5
    if Dice1 == Dice2:
        Score2 = Score2 + random.randint(1, 6)
    else:
        pass
    if Score2 < 0:
        Score2 = 0
    else:
        pass
    print(Score2)
    time.sleep(0.5)
print("Player 2 score = ", Score2)

if Score2 > Score1:  #Printing winner
    print("Player two wins")
    WinnerScore = Score2
elif Score2 < Score1:
    print("Player one wins")
    WinnerScore = Score1
else:
    print("Rerolling for decider")
    Score1 = Score1 + random.randint(1, 6)
    #Rerolling for compensation if the score is the same
    Score2 = Score2 + random.randint(1, 6)
    if Score1 > Score2:
        print("Player 1 wins")
        WinnerScore = Score1
    else:
        print("Player 2 wins")
        WinnerScore = Score2

Results = open("Scores.txt", "w")  #Open Txt file for editing
Winner = input(
    "Winner please enter your name!"
)  #Get winner name instead of having the winner enter credentials in name due to login system
WrittenScore = "/n" + Winner + "," + str(
    WinnerScore)  #Convert the scores and text into a writeable format
Results.write("WrittenScore")  #Write to the file
