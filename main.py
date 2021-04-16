import random #Imports for the project
import time
import sys


Score1 = 0 #setting variables to be used in the code
Score2 = 0
Rounds = 0
Dice1 = 0
Dice2 = 0



def Scores():
	Savedscores = open('Scores.txt', 'r')
	file_contents = Savedscores.read()
	print("\033[1;36m",file_contents)
	Savedscores.close()
	Mainmenu = input("\033[0;32mWould you like to go back to the main menu?\n Yes or no?: ")
	if Mainmenu == "Yes" or "yes" or "Y" or "y":
		menu()
	else:
		sys.exit()

def menu():
    print("\033[1;31m************Welcome to Dice Game**************")
    print()

    choice = input("""
A: Start
B: Print Scores
Q: Exit
Please enter your choice: """)

    if choice == "A" or choice =="a":
        pass
    elif choice == "B" or choice =="b":
		  	Scores()
    elif choice=="Q" or choice=="q":
        sys.exit()
    else:
        print("You must only select either A,B or Q")
        print("Please try again")
        menu()

menu()

#the program is initiated, so to speak, here

def login():
  username = input("Player 1 Enter your username: ").strip() #Removing extra spaces to raw text
  password = input("Enter your password: ").strip()

  with open("Logins.txt", "r") as f: #Opening text file in read
    for line in f:
      loginInfo = line.strip().split(",") #splitting and removing the , from the text file
      if username == loginInfo[0] and password == loginInfo[1]: #checking if the password and username matches
        return True #returning result
    return False

if login():
  input("Correct login \n Press any key to continue: ")
else:
	print("Wrong login exiting...")
	time.sleep(2)
	quit()

def login2():
  username2 = input("Player 2 Enter your username: ").strip() #Removing extra spaces to raw text
  password2 = input("Enter your password: ").strip()

  with open("Logins.txt", "r") as f: #Opening text file in read
    for line in f:
      loginInfo2 = line.strip().split(",") #splitting and removing the , from the text file
      if username2 == loginInfo2[0] and password2 == loginInfo2[1]: #checking if the password and username matches
        return True  #returning result
    return False

if login2():
  input("Correct login \n Press any key to continue: ")
else:
	print("Wrong login exiting...")
	time.sleep(2)
	quit()


print("\033[0;32mRolling Player 1's dice...")
time.sleep(2);

while Rounds != 5:
	Rounds = Rounds + 1;
	print("\033[94mRound "+str(Rounds));
	Dice1 = random.randint(1,6); #Using random int for getting an int inside of a range simulating random dice roll
	Dice2 = random.randint(1,6);
	RoundTotal = Dice1 + Dice2;
	Score1 = Score1 + RoundTotal;
	if Score1 % 2: #Check if score1 is odd or even
		Score1 = Score1 + 10;
	else:
		Score1 = Score1 - 5;
	if Dice1 == Dice2:
		Score1 = Score1 + random.randint(1,6)
	else:
		pass
	if Score1 < 0:
		Score1 = 0
	else:
		pass
	print("\033[1;31m"+str(Score1)); #Printing per dice roll score
	time.sleep(0.5)
print("\033[1;36mPlayer 1's score = ",Score1); #Printing final score for the player

Rounds = 0 #Resetting round variable for the second player

time.sleep(1)
print("\033[0;32mRolling player 2's dice...")
time.sleep(2)

while Rounds != 5:
	Rounds = Rounds + 1;
	print("\033[94mRound "+str(Rounds));
	Dice1 = random.randint(1,6);
	Dice2 = random.randint(1,6);
	RoundTotal = Dice1 + Dice2;
	Score2 = Score2 + RoundTotal;
	if Score2 % 2:
		Score2 = Score2 + 10;
	else:
		Score2 = Score2 - 5;
	if Dice1 == Dice2:
		Score2 = Score2 + random.randint(1,6)
	else:
		pass
	if Score2 < 0:
		Score2 = 0
	else:
		pass
	print("\033[1;31m"+str(Score2));
	time.sleep(0.5)
print("\033[1;36mPlayer 2 score = ",Score2);


if Score2 > Score1: #Printing winner
	print("Player two wins");
	WinnerScore = Score2
elif Score2 < Score1:
	print("Player one wins");
	WinnerScore = Score1
else:
	print("Rerolling for decider")
	Score1 = Score1 + random.randint(1,6); #Rerolling for compensation if the score is the same
	Score2 = Score2 + random.randint(1,6)
	if Score1 > Score2:
		print("Player 1 wins")
		WinnerScore = Score1
	else:
		print("Player 2 wins")
		WinnerScore = Score2


Results = open("Scores.txt","w")	#Open Txt file for editing
Winner = input("Winner please enter your name! ") #Get winner name instead of having the winner enter credentials in name due to login system
WrittenScore = "/n" + Winner + "," + str(WinnerScore) #Convert the scores and text into a writeable format
Results.write(str(WrittenScore)) #Write to the file
Results.close()
print("Printing score to winner scores file...")