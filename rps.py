import random
import os
from termcolor import colored
from pyfiglet import Figlet
os.system("cls")
f = Figlet(font="slant")
print(colored(f.renderText("RPS GAME"),"green")) 
score=0
compscore=0
list1=["rock","paper","scissor"]
computer=random.choice(list1)
while True:
    computer=random.choice(list1)
    user = str(input("enter your choice(rock,paper,scissor):"))
    print("you choice :",user)
    print("computer choice:",computer)
    if user == computer:
        print("tie")
    elif user == 'rock':
        if computer == "scissor":
            print("you win")
            score += 1   
            compscore -= 0.25 
        else:
            print("you lose")
            score -=0.25
            compscore += 1
    elif user == "scissor":
        if computer == "paper":
            print("you win")
            score += 1
            compscore -= 0.25
        else:
            print("you lose")
            score -= 0.25 
            compscore += 1
    elif user == "paper":
        if computer == "rock":
            print("you win")
            score += 1
            compscore -= 0.25
        else:
            print("you lose")
            score -= 0.25
            compscore += 1
    elif user == "exit":
        print("have a good day ma'am/sir")
        print(score)
        print(compscore) 
        break
    else :
        print("wrong input please try again")
    print("your score =",score)
    print("computer score =",compscore)                                  
