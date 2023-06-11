#Student number: 19036837
#Student: Kaja Drozd
#Last modification: 14th of April 2021

import turtle
import random

p1_loc= 1   #Declaring the position of player as globals to
p2_loc= 1   #facilitate the access to them in every part of the code 

def draw_board():
    turtle.pencolor("red")
    turtle.width(3)
    
    for i in range(6): #drawing vertical lines of the board
        turtle.penup()
        turtle.goto(-300+120*i, 300)
        turtle.pendown()
        turtle.goto(-300+120*i,-300)
        
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    
    for i in range(1,7): #drawing horizontal lines of the board
        turtle.forward(5*120)
        turtle.penup()
        turtle.goto(-300,-300+i*120)
        turtle.pendown()

    turtle.penup()
    turtle.goto(-200, -200)

    turtle.pencolor("purple")
    
    for i in range(1, 26):  #on some special squares there is a need for
        turtle.write(i)     #change of direction of drawing
        if (i == 5 or i == 15):
            turtle.left(90)
            turtle.forward(120)
            turtle.left(90)
        elif (i==10 or i==20):
            turtle.right(90)
            turtle.forward(120)
            turtle.right(90)
        else:
            turtle.forward(120)

def add_snakes():
#snake1
    turtle.addshape("snake.gif")
    s1 = turtle.Turtle()
    s1.shape("snake.gif")
    s1.penup()
    s1.goto(120, 120)
#snake2
    turtle.addshape("snake2.gif")
    s1 = turtle.Turtle()
    s1.shape("snake2.gif")
    s1.penup()
    s1.goto(0, -150)
#snake3
    turtle.addshape("snake3.gif")
    s3 = turtle.Turtle()
    s3.shape("snake3.gif")
    s3.penup()
    s3.goto(-240, -60)
    
def add_ladders():
#ladder1
    turtle.addshape("ladder.gif")
    l1 = turtle.Turtle()
    l1.shape("ladder.gif")
    l1.penup()
    l1.goto(-120, -60)
#ladder2
    turtle.addshape("ladder2.gif")
    l2 = turtle.Turtle()
    l2.shape("ladder2.gif")
    l2.penup()
    l2.goto(0, 190)
#ladder3
    turtle.addshape("ladder3.gif")
    l3 = turtle.Turtle()
    l3.shape("ladder3.gif")
    l3.penup()
    l3.goto(250, -120)

#rolling dice and adding the shape to present the outcome of rolling the dice
def rolling_dice(x):

    turtle.addshape("dice1.gif")
    turtle.addshape("dice2.gif")
    turtle.addshape("dice3.gif")
    turtle.addshape("dice4.gif")
    turtle.addshape("dice5.gif")
    turtle.addshape("dice6.gif")

 
    switcher = {
        1: "dice1.gif",
        2: "dice2.gif",
        3: "dice3.gif",
        4: "dice4.gif",
        5: "dice5.gif",
        6: "dice6.gif",}
    return switcher[x]

def move_player(dice_num, player, player_loc): #function to move players according to the dice
    
#stretch : when the dice number presents greater number than number of squares
#required for player to finish game, turtle change direction and the player is
#moving backwards - to help accomplish that we create variable player_return
#which is initially False but when reaching 25 becomes True


    player_return = False
        
    for i in range (dice_num):
        if (player_loc == 5 or player_loc == 15):  #on special squares there is
            player.left(90)                        #need for change of direction of player's movement
            player.forward(120)
            player.left(90)
        elif(player_loc==10 or player_loc==20):
            player.right(90)
            player.forward(120)
            player.right(90)
        elif (player_loc == 25 or player_return == True): #updating status to precise if is going back or not
            player_return = True
            player.right(180)
            player.forward(120)
            player_loc = player_loc - 2 #substracting 2 because at the end we add 1
            player.left(180)
        else:
            player.forward(120)
        player_loc = player_loc + 1

    return player_loc

def ladders_n_snakes(player, player_loc):
#reaction of players when encountering ladders or snakes
# + defining players' location
#LADDERS:
    if (player_loc == 5):
        player.left(90)
        player.forward(2*120)
        player.right(90)
        player_loc=15
        
    if (player_loc == 9 or player_loc ==18):
        player.right(90)
        player.forward(120)
        player.right(90)
        if (player_loc == 9):
            player_loc = 12
        if (player_loc == 18):
            player_loc = 23         
#SNAKES:
    if (player_loc == 8):
        player.left(90)
        player.forward(120)
        player.left(90)
        player_loc = 3
        
    if (player_loc == 20):
        player.left(90)
        player.forward(3*120)
        player.left(90)
        player_loc = 1
        
    if (player_loc == 24):
        player.right(90)
        player.forward(2*120)
        player.left(90)
        player_loc = 14

    return player_loc

def winner(p1_loc, p2_loc):
# when position of a player is eaxctly 25 the game is ended & the winner is announced
    turtle.addshape("win.gif")
    turtle.penup()
    turtle.goto(0,0)
    turtle.shape("win.gif")
    turtle.st()
    if (p1_loc == 25):
        print("Player 1 - Bull - won")
    elif (p2_loc == 25):
        print("Player 2 - Cow - won")

    print("To exit game type \"E\" ", end="")
    stopper = input()   #controller to let user decide to restart the game or not
    if (stopper == "E"):
        exit()
    else:
        turtle.ht()
        print("\n")
        
def main():
    turtle.speed(7)
    turtle.bgcolor("yellow")
    turtle.title("Snakes and Ladders")
    turtle.setup(800,700, 400, -100)
    
    draw_board()

    add_ladders()
    add_snakes()

    while(True):     
        #adding player 1 & its shape
        p1 = turtle.Turtle()#player1
        turtle.addshape("bull.gif")
        p1.shape("bull.gif")
        p1.penup()
        p1.goto(-270,-270)
       
        #adding player 2 & its shape
        p2 = turtle.Turtle()#player2
        turtle.addshape("cow.gif")
        p2.shape("cow.gif")
        p2.penup()
        p2.goto(-270,-210)

        #adding dice
        dice = turtle.Turtle()
        dice.penup()
        dice.goto(-350,0)

        global p1_loc
        global p2_loc
        
        p1_loc=1  #setting initial positions
        p2_loc=1

        print("NEW GAME!") #START OF A NEW GAME

        while (p1_loc<=25 and p2_loc<=25):
            enter = input("Bull's turn : Press enter to roll the dice")
            dice_roll= random.randint(1,6) #randomly choosing between 1 - 6 (idea pf throwing dice)
            print("Dice:", dice_roll)
            dice.shape(rolling_dice(dice_roll))

            p1_loc = move_player(dice_roll,p1,p1_loc)
            p1_loc = ladders_n_snakes(p1,p1_loc)
            print("Player 1 is now on square", p1_loc, "\n")

            if (p1_loc == 25):           #presenting winner & asking user whether
                winner(p1_loc, p2_loc)   #to starta new game or not
                break
            
            enter = input("Cow's turn : Press enter to roll the dice")
            dice_roll= random.randint(1,6) #randomly choosing between 1 - 6 (idea pf throwing dice)
            print("Dice:", dice_roll)
            dice.shape(rolling_dice(dice_roll))

            p2_loc = move_player(dice_roll,p2,p2_loc)
            p2_loc = ladders_n_snakes(p2,p2_loc)
            print("Player 2 is now on square", p2_loc, "\n")
            
            if (p2_loc == 25):
                winner(p1_loc, p2_loc) #presenting winner & asking user whether 
                break                  #to starta new game or not
                                       #(for second time in case the player 2 is a winner)
main()          
