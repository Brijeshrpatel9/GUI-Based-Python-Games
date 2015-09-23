# implementation of Memory card game
import simplegui
import random

card_list1 = range(0,8)
card_list2 = range(0,8)
card_list = card_list1 + card_list2
random.shuffle(card_list)
exposed = [False]*16 
state = 0
a = b = i = 0
turns = 0

#function to initialize globals
def new_game():
    global exposed, state, card_list1, card_list2, card_list, turns
    exposed = [False] * 16
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    card_list1 = range(0,8)
    card_list2 = range(0,8)
    card_list = card_list1 + card_list2
    random.shuffle(card_list)
      
     
# define event handlers
def mouseclick(pos):
    
     global state, a, b, turns
        
     cards_pos=pos
     i = pos[0]//50
     if exposed[i] == True:
            return
     else:
            if state == 0:
                cards_pos=pos
                a = pos[0]//50
                exposed[a] = True
                turns = turns + 1
                state = 1
        
            elif state == 1:
                cards_pos=pos
                b = pos[0]//50
                exposed[b] = True
                #turns = turns + 1
                state = 2
            
            else:
                if card_list[a] == card_list[b]:
                        exposed[a] = True
                        exposed[b] = True
                        state = 0
                        
                else:
                        exposed[a] = False
                        exposed[b] = False
                        
                cards_pos=pos
                a = pos[0]//50
                exposed[a] = True
                turns = turns + 1
                state = 1
            
            label.set_text("Turns = " + str(turns))
            
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pos = [12, 65]
    
    for card in range(16):
        if exposed[card] == True:
            canvas.draw_text(str(card_list[card]), pos, 50, 'White')
        else:
            canvas.draw_polygon([[card*50,0],[card*50+50,0],[card*50+50,100],[card*50,100]], 1, "Black", 'Green')
        pos[0] += 50
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
