
while True:
    x = input("Player 1 Make your choice: ")
    y = input ("Player 2 Make your choice: ")



    if(x=="rock"):
        if(y=="scissor" or y=="Scissor"):
            print("player 1 win the game")
    elif(x=="rock" or x=="Rock"):
        if(y=="paper" or y=="Paper"):
            print("player 2 win the game")
    elif(x=="paper" or x=="Paper"):
        if(y=="scissor" or y=="Scissor"):
            print("player 2 win the game")
    elif(x=="paper" or x=="Paper"):
        if(y=="rock" or y=="Rock"):
            print("player 1 win the game")
    elif(x=="scissor" or x=="Scissor"):
        if(y=="rock" or y=="Rock"):
            print("player 2 win the game")
    elif(x=="scissor" or x=="Scissor"):
        if(y=="paper" or y=="Paper"):
            print("player 1 win the game")
    
    p=input("you want to continue yes or no: ")
    if(p=="yes"):
        continue
    
    elif(p=="no"):
        break
 

    
