# My favorite things in life don't cost any money. It's really clear that the most precious resource 
# we all have is time. So let's make it precise counter.

# I have impelmented "Stopwatch" game in Python using Code Skulptor Tool.


# define global variables

import simplegui
import math

t = 0
x = 0
y = 0
counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t //600
    b = ((t % 600) / 10) // 10
    c = ((t % 600) / 10) % 10
    d = (t % 600) % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    global t, x, y
    if timer.is_running() == True:
        if(t % 10 == 0):
            x += 1
            y += 1
        else:
            y += 1
        
    timer.stop()
    

def reset():
     global t, x, y
     t = x = y = 0
     timer.stop()

    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1
    global counter
    counter += 1
       


# define draw handler
def draw(canvas):
    global t, st
    global x, y
    canvas.draw_text(format(t), [55,110] , 40, "White")
    canvas.draw_text(str(x)+ "/" + str(y), [135,35], 32, "Red")
    
    
# create frame

frame = simplegui.create_frame("Stop Watch", 200, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame

frame.start()
