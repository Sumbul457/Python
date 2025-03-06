import random

"""
1 is for rock 
-1 is for scissor
0 is for paper
"""

while True:
 computer = random.choice([1,0,-1])
 youstr = input("Enter your choice: ")
 youDict = {
    "rock" : 1,
    "scissor" : -1,
    "paper" : 0
}
 reverseDict = {
   1: "rock",
  -1 : "scissor",
   0 : "paper"
}

 you = youDict[youstr] # make this to match it

 print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

 if(computer == you):
    print("It's  a draw")

 else:
   if(computer == -1 and you == 1):
    print("You win!")

   elif(computer == -1 and you == 0):
     print("You lose!")

   elif(computer == 1 and you == -1):
    print("You lose!")  

   elif(computer == 1 and you == 0):
    print("You win!")

   elif(computer == 0 and you == -1):
    print("You win!")

   elif(computer == 0 and you == 1):
    print("You lose!")

   else:
    print("something went wrong")

    
    





