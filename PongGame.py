# Pong Game with Color Ball (Ball Color changes when it touches Paddle)

I have impelmented "Pong Game" in Python using Code Skulptor Tool. When Ball touches one of the paddle, it changes color. When ball misses the paddle touch, score is incremented by 1.

This is "2 Player" game.

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [0,0]
ball_vel = [0,0]

paddle1_vel = 0
paddle2_vel = 0

paddle1_pos = 200
paddle2_pos = 200

score1 = 0
score2 = 0

ball_col = "Red"
color = ["Red", "Green", "Blue", "Brown", "Yellow", "Aqua","Crimson", "DarkMagenta" ,"DeepPink" ,"LightSeaGreen" , "BurlyWood" ]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    ball_vel[0] = random.randrange(120, 240)/60
    ball_vel[1] = random.randrange(60, 180)/60
    
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    elif direction == RIGHT:
        ball_vel[1] = - ball_vel[1]
                

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = paddle2_pos = 200
    paddle1_vel = paddle2_vel = score1 = score2 = 0
    
    spawn_ball(random.choice([LEFT,RIGHT]))
    
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, ball_col
    global paddle1_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")   #Mid Line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
        
    # update ball
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
  
        if paddle1_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            pass
            #ball_vel[0] = ball_vel[0]
        else:
            score2 = score2 + 1
            spawn_ball(RIGHT)

        
    if ball_pos[0] >= (WIDTH -1) - PAD_WIDTH - BALL_RADIUS:
        
        if paddle2_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            pass
            #ball_vel[0] = ball_vel[0]      
        else:
            score1 = score1 + 1
            spawn_ball(LEFT)    


         
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_vel[0] =  - ball_vel[0]
        ball_vel[0] = 1.2 * ball_vel[0]
        ball_col = random.choice(color)
    elif ball_pos[0] >= (WIDTH -1) - BALL_RADIUS - PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] = 1.2 * ball_vel[0]
        ball_col = random.choice(color)        
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT -1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, ball_col, ball_col)
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= (HEIGHT -1) - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= (HEIGHT -1) - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel


    # draw paddles

    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                 [HALF_PAD_WIDTH , paddle1_pos + HALF_PAD_HEIGHT], 
                 PAD_WIDTH, 
                 "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH , paddle2_pos - HALF_PAD_HEIGHT], 
                 [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                 PAD_WIDTH, 
                 "White")
  
    
    # draw scores
    
    canvas.draw_text(str(score1), [180,65], 50, "White")
    canvas.draw_text(str(score2), [380,65], 50, "White")
    

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
    
    acc = 6 
        
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        
     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
         
      
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()

'''
# Black and White Pong
# Implementation of classic arcade game Pong
import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = 200
paddle2_pos = 200
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    ball_vel[0] = random.randrange(120, 240)/60
    ball_vel[1] = random.randrange(60, 180)/60
    
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    elif direction == RIGHT:
        ball_vel[1] = - ball_vel[1]
                
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = paddle2_pos = 200
    paddle1_vel = paddle2_vel = score1 = score2 = 0
    
    spawn_ball(random.choice([LEFT,RIGHT]))
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
        
    # update ball
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
  
        if paddle1_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = ball_vel[0]
        else:
            score2 = score2 + 1
            #print hi
            spawn_ball(RIGHT)
        
    if ball_pos[0] >= (WIDTH -1) - PAD_WIDTH - BALL_RADIUS:
        #print hi
        if paddle2_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = ball_vel[0]      
        else:
            score1 = score1 + 1
            spawn_ball(LEFT)    
         
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_vel[0] =  - ball_vel[0]
    elif ball_pos[0] >= (WIDTH -1) - BALL_RADIUS - PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT -1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= (HEIGHT -1) - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= (HEIGHT -1) - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                 [HALF_PAD_WIDTH , paddle1_pos + HALF_PAD_HEIGHT], 
                 PAD_WIDTH, 
                 "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH , paddle2_pos - HALF_PAD_HEIGHT], 
                 [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                 PAD_WIDTH, 
                 "White")
  
    
    # draw scores
    
    canvas.draw_text(str(score1), [180,65], 50, "White")
    canvas.draw_text(str(score2), [380,65], 50, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
    
    acc = 4 
        
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        
     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
         
      
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
# start frame
new_game()
frame.start()
