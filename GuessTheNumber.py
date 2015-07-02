# Code for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
range = 100
n = 0
secret_number = 0
low = 0

# helper function to start and restart the game
def new_game():
    
    global n
    n = math.ceil(math.log(range- low + 1)/math.log(2))
    n = int(n)

    print "New Game. Range is from 0 to ", range
    print "Number of remaining guesses", n
    global num_range
    num_range = random.randrange(range)
    secret_number = num_range
    print "  "
    
def range100():
   
    print " "
    global range
    range = 100
    new_game()
    
def range1000():
   
    print " "
    global range
    range = 1000
    new_game()
    
def input_guess(guess):

    player_num = float(guess)
    
    global secret_number
    global num_range
    global n
    n -=1
    print "Guess was", guess
    print "Number of remaining guesses", n
   
    if (player_num == num_range and n >= 0):
        print "Correct!"
        print " "
        print " "
        new_game()
    elif (player_num < num_range and n>0):
        print "Higher!"
    elif (player_num > num_range and n>0):
        print "Lower!"
    else:
        print "You ran out of guesses. The number is", num_range 
        print " "
        print " "
        new_game()
    
    print " "
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame

new_game()
