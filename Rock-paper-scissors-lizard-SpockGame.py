# Rock-paper-scissors-lizard-Spock game

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid thing"
    
    # convert name to number using if/elif/else
    # don't forget to return the result!

def number_to_name(number):
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
   
    print "Player chooses", player_choice  
    player_number = name_to_number(player_choice)
        
    import random
    comp_number = random.randint(0, 4)
    
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    
    compare = (comp_number - player_number) % 5
    
    if compare == 1:
        print "Computer wins!"
    elif compare == 2:
      print "Computer wins!"
    elif compare == 3:
        print "Player wins!"
    elif compare == 4:
        print "Player wins!"
    else:
        print "Player and Computer tie!"
   
        
    print ""

# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
