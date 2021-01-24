import random
comp_wins=0
player_wins=0
def choose_option():
    user_choice=input("Choose Rock, Paper or Scissor: ")
    if user_choice in ["Rock","rock","r","R"]:
        user_choice="r"
    elif user_choice in ["Paper","paper","P","p"]:
        user_choice="p"
    elif user_choice in ["Scissor","scissor","s","S"]:
        user_choice="s"
    else:
        print("Try again: choose s, r or p ")
        choose_option()
    return user_choice

def computer_option():
    comp_choice =random.randint(1,3)
    if comp_choice ==1:
        comp_choice="r"
    elif comp_choice ==2:
        comp_choice="p"
    else:
        comp_choice="s"
    return comp_choice
while True:
    print("")
    user_choice=choose_option()
    comp_choice=computer_option()
    print("")

    if user_choice=="r":
        if comp_choice=="r":
            print("You chose rock!.The computer chose rock \n tie!!")
        elif comp_choice=="s":
            print("You chose rock!.The computer chose scissor \n you win!!")
            player_wins+=1
        elif comp_choice=="p":
            print("You chose rock!.The computer chose paper \n you lose!!")
            comp_wins+=1
    if user_choice=="p":
        if comp_choice=="p":
            print("You chose paper!.The computer chose paper \n tie!!")
        elif comp_choice=="s":
            print("You chose paper!.The computer chose scissor \n you lose!!")
            comp_wins+=1
        elif comp_choice=="r":
            print("You chose paper!.The computer chose rock \n you win!!")
            player_wins+=1
    if user_choice=="s":
        if comp_choice=="r":
            print("You chose scissor!.The computer chose rock \n you lose!!")
            comp_wins+=1
        elif comp_choice=="s":
            print("You chose scissor!.The computer chose scissor \n tie!!")
        elif comp_choice=="p":
            print("You chose scissor!.The computer chose paper \n you win!!")
            player_wins+=1

    print("")
    print("Player Wins: "+ str(player_wins))
    print("Computer Wins: "+ str(comp_wins))
    print("")
    
    user_choice=input("Do you want to play again? (y/n): ")
    if user_choice in ["y","yes","Yes","Y"]:
        pass
    elif user_choice in ["no","No","N","n"]:
        break
    else:
        break