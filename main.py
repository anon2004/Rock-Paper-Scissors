
player_1=input("What is Your Name?:")
player_2=input("What is Your Opponents Name?:")
print("\033[34m*********************************************\033[0m")
print("\033[33mWELCOME TO THE EPIC ROCK PAPER SCISSORS GAME\033[0m")
print("\033[31m***RULES***\033[0m")
print("Enter R for Rock, P for Paper, S for Scissors")
print("\033[34m*********************************************\033[0m")


#Here We Import Getpass To Hide THe Input
from getpass import getpass as input
play_1=input(f"{player_1} Enter Your Choice: ")
play_2=input(f"{player_2} Enter Your Choice: ")
if play_1.lower()=="r" and play_2.lower()=="s":
   print(f"{player_1} WINS")
elif play_1.lower()=="s" and play_2.lower()=="r":
   print(f"{player_2} WINS")
elif play_1.lower()=="s" and play_2.lower()=="p":
   print(f"{player_1} WINS")
elif play_1.lower()=="p" and play_2.lower()=="s":
   print(f"{player_2} WINS")
elif play_1.lower()=="r" and play_2.lower()=="p":
   print(f"{player_1} WINS")
elif play_1.lower()=="p" and play_2.lower()=="r":
   print(f"{player_2} WINS")
elif play_1.lower()==play_2.lower():
   print("Its a Tie")
else:
   print('\033[31mSOMEBODY ENTERED AN INVALID CHOICE')
condition=input("Do You Want To Play Again? (yes/no/y/n): ")
if condition.lower()=="yes" or condition.lower=="y":
   break
print("THANK YOU FOR PLAYING")

