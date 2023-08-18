import random



def p_choice():
    choice = int(input("ENTER YOUR CHOICE"))

    if choice==1 or choice==2 or choice==3:
        return choice
    else:
        print("INVALID CHOICE, CHOOSE AGAIN\n")
        p_choice()


def start():
    round=0
    player_score=0
    comp_score=0

    while round<12:
        print("Enter:\t1 for ROCK\t2 for PAPER\t3for SCISSOR")
        print("Round:",round)
        choice=p_choice()
        comp = random.randint(1, 3)


        if choice==comp:
            print("YOU BOTH SELECTED ROCK\n\n")
        elif (choice==1 and comp==2) or (choice==2 and comp==3)or (choice==3 and comp==1):
            comp_score=comp_score+1
            print("YOU: ROCK\nCOMP: PAPER\nCOMP WON THE ROUND\n\n")
        elif (choice==1 and comp==3)or(choice==2 and comp==1) or (choice==3 and comp==2):
            player_score=player_score+1
            print("YOU: ROCK\nCOMP: SCISSOR\nYOU WON THE ROUND\n\n")
        round+=1

    if player_score>comp_score:
        print("HURREY YOU WON THE GAME\nYOUR SCORE:",player_score,"COMP SCORE",comp_score)
    elif comp_score>player_score:
        print("BETTER LUCK NEXT TIME\nYOUR SCORE",player_score,"COMP SCORE",comp_score)
    elif comp_score==player_score:
        print("THE GAME WAS DRAW\nYOUR SCORE",player_score,"COMP SCORE",comp_score)

    print("DO YOU WANT TO PLAY AGAIN?(Y/N)")
    x=input()
    if x=="Y" or x=="y":
        start()
    else:
        print("OK.. THANKS FOR PLAYING")


def game():
    name=input("Your Name?")
    
    print("Welcome ,",name, "To our rock paper scissor. Do you want to play?(Y/N)?\n")
    answer=input()
    if answer=="Y" or answer=="y":
        print(
            "so the rules of the game are like this \n1)There will be 12 rounds \n2)The one to score the most will win\n3)"
            "ROCK--beats-->SCISSOR\nSCISSOR--beats-->PAPER\nPAPAER--beats-->ROCK\nSCISSOR--beats--PAPER\n\n")
        start()
    else:
        print("IF YOU WANT TO PLAY YOU CAN COME ANYTIME, BYE!")

game()
