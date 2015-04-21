
I have impelmented "Space Ship" game in Python using Code Skulptor Tool.

It's more fun to play with your friends.

Spaceship should behave as follows: • The left and right arrows should control the orientation of your spaceship. While the left arrow is held down, your spaceship should turn counter-clockwise. While the right arrow is down, your spaceship should turn clockwise. When neither key is down, your ship should maintain its orientation. You will need to pick some reasonable angular velocity at which your ship should turn. • The up arrow should control the thrusters of your spaceship. The thrusters should be on when the up arrow is down and off when it is up. When the thrusters are on, you should draw the ship with thrust flames. When the thrusters are off, you should draw the ship without thrust flames. • When thrusting, the ship should accelerate in the direction of its forward vector. This vector can be computed from the orientation/angle of the ship using the provided helper function angle_to_vector. You will need to experiment with scaling each component of this acceleration vector to generate a reasonable acceleration. • Remember that while the ship accelerates in its forward direction, but the ship always moves in the direction of its velocity vector. Being able to accelerate in a direction different than the direction that you are moving is a hallmark of Asteroids. • Your ship should always experience some amount of friction. (Yeah, we know, "Why is there friction in the vacuum of space?". Just trust us there is in this game.) This choice means that the velocity should always be multiplied by a constant factor less than one to slow the ship down. 
It will then come to a stop eventually after you stop the thrusters.
# program template for RiceRocks
import simplegui
import math
import random

# globals for user interface
WIDTH = 800 # please do not go below '400'
HEIGHT = WIDTH / 8 * 6
FONT_SIZE = HEIGHT * 0.05
high_score, score = 0, 0
difficulty = 1500.0
lives = 3
time = 0.5
started = False
paused = False

#ImageInfo class
class ImageInfo:
    def __init__(self, centre, size, radius = 0, lifespan = None, animated = False):
        self.centre = centre
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_centre(self):
        return self.centre

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")
# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")
# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
#splash_blank = simplegui.load_image("https://i.imgur.com/0Kd8pyg.png")
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 70)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")
# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image_orange = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
explosion_image_alpha =  simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image_blue =   simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")



# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrusting = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_centre = info.get_centre()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
        
    def draw(self,canvas):
#        canvas.draw_circle(self.pos, self.radius * 4, 1, "White", "White")
        if self.thrusting:
            canvas.draw_image(self.image, [self.image_centre[0] + self.image_size[0], self.image_centre[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_centre, self.image_size, self.pos, self.image_size, self.angle)

    def increase_angle_vel(self):
        self.angle_vel += .08
        
    def decrease_angle_vel(self):
        self.angle_vel -= .08
        
    def thrust(self, state):
        self.thrusting = state
        
        if self.thrusting:
            ship_thrust_sound.play()
            pass
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            
    def shoot(self):
        front = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * front[0], self.pos[1] + self.radius * front[1]]
        missile_vel = [self.vel[0] + front[0] * 4, self.vel[1] + front[1] * 4]
        missile_group.append(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))
#        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)

    def update(self):
        if self.thrusting:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .17
            self.vel[1] += acc[1] * .17
         
        self.vel[0] *= .983 # friction update
        self.vel[1] *= .983 # # 'Acceleration & Friction' Lecture

        self.angle += self.angle_vel
        if -.16 <= self.vel[0] < 0.16 and self.thrusting == False:
            self.vel[0] += 0.16
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_centre = info.get_centre()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        else:
            return False

    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, [self.image_centre[0] + self.image_size[0] * self.age, self.image_centre[1]], self.image_size, self.pos, self.image_size, self.angle)
        else: canvas.draw_image(self.image, self.image_centre, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age < self.lifespan:
            return True
        
    
        
# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
     return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(canvas, group):
    for sprite in group:
        if not sprite.update():
            group.remove(sprite)
        sprite.draw(canvas)

def group_collide(other_object, group):
    for sprite in group:
        if sprite.collide(other_object):
            group.remove(sprite)
            explosion_group.append(Sprite(other_object.get_position(), [0,0], 0, 0, 
                                          explosion_image_alpha, explosion_info, explosion_sound))
            return True

def group_group_collide(group, other_group):
    for sprite in group:
        for other_sprite in other_group:
            if sprite.collide(other_sprite):
                other_group.remove(other_sprite)
                group.remove(sprite)
                explosion_group.append(Sprite(sprite.get_position(), [0,0], 0, 0, 
                                          explosion_image_orange, explosion_info, explosion_sound))
                return True
         
def draw(canvas):
    global time, started, lives, score, high_score, rock_timer, rock_interval
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    centre = debris_info.get_centre()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_centre(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, centre, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, centre, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    if paused or not started:
        canvas.draw_image(splash_image, splash_info.get_centre(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], splash_info.get_size())
    if started and not paused:
        process_sprite_group(canvas, rock_group)
        process_sprite_group(canvas, missile_group)
        process_sprite_group(canvas, explosion_group)
        my_ship.draw(canvas)
        my_ship.update()
        
    if group_collide(my_ship, rock_group):
        lives -= 1
        if lives <= 0: 
            if score > high_score: high_score = score
            reset_game()
            
        for sprite in rock_group:
            if dist(sprite.pos, [WIDTH / 2, HEIGHT / 2]) <= my_ship.radius * 4:
                rock_group.remove(sprite) # remove all rocks near the ship upon respawn           
        my_ship.vel = [0, 0]
        my_ship.pos = [WIDTH / 2, HEIGHT / 2]
        
    if group_group_collide(missile_group, rock_group):
        score += 1   
        rock_interval = difficulty - score * 15.0
        if rock_interval < 250.0: rock_interval = 250.0
        print "rock_interval:", rock_interval
        
    # draw text
    for remaining in range(lives):
        icon_pos = [WIDTH * 0.01 + (remaining * my_ship.image_size[1] / 2 + my_ship.radius / 2), HEIGHT * 0.01 + ((my_ship.image_size[0] - my_ship.radius) / 2)]
        canvas.draw_image(ship_image, ship_info.get_centre(), ship_info.get_size(), icon_pos,
                          [my_ship.image_size[1] / 2, my_ship.image_size[0] / 2], math.radians(270))
        #    canvas.draw_text('Lives: '+ str(lives), [WIDTH * 0.01, HEIGHT * 0.01 + FONT_SIZE], FONT_SIZE, "White", 'sans-serif')
        
    text_width = frame.get_canvas_textwidth('Score: '+ str(score), FONT_SIZE, 'sans-serif')
    canvas.draw_text('Score: '+ str(score), [WIDTH - text_width - WIDTH * 0.01, HEIGHT * 0.01 + FONT_SIZE], FONT_SIZE, "White", 'sans-serif')
    text_width = frame.get_canvas_textwidth('High Score: '+ str(high_score), FONT_SIZE / 2, 'sans-serif')
    canvas.draw_text('High Score: '+ str(high_score), [WIDTH / 2 - text_width / 2, HEIGHT * 0.01 + FONT_SIZE / 2], FONT_SIZE / 2, "White", "sans-serif")
        #    canvas.draw_text('High Score: '+ str(high_score), [WIDTH / 2 - text_width / 2, HEIGHT * 0.01 + FONT_SIZE], FONT_SIZE, "White", "sans-serif")
        #    canvas.draw_text('High Score: '+ str(high_score), [WIDTH - text_width - WIDTH * 0.01, HEIGHT * 0.01 + FONT_SIZE * 1.5], FONT_SIZE / 2, "White", "sans-serif")

def mouseclick(pos):
    global started, score, lives
    if not started:
        lives = 3
        score = 0
        started = True
        soundtrack.rewind()
        soundtrack.play()
        rock_timer.start()

def keydown(key):
    global paused
    if key == simplegui.KEY_MAP["p"]:
        paused = not paused
    if started:
        if key==simplegui.KEY_MAP["right"]:
            my_ship.increase_angle_vel()
        if key==simplegui.KEY_MAP["left"]:
            my_ship.decrease_angle_vel()
        if key==simplegui.KEY_MAP["up"]:
            my_ship.thrust(True)
        if key==simplegui.KEY_MAP["space"]:
    #        shoot_timer.start()
            my_ship.shoot()	
        
def keyup(key):
    if started:
        if key==simplegui.KEY_MAP["up"]:
            my_ship.thrust(False)
        if key==simplegui.KEY_MAP["right"]:
            my_ship.decrease_angle_vel()
        if key==simplegui.KEY_MAP["left"]:
            my_ship.increase_angle_vel()
    #    if key==simplegui.KEY_MAP["space"]:
    #        shoot_timer.stop()
    
    
# timer handler that spawns a rock    
def rock_spawner():
    global rock_timer
    if len(rock_group) <= 12 and started == True:
#    if len(rock_group) <= score and started == True:
        asteroid_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        asteroid_ang_vel = (random.randint(1, 5)) / 100.0
        asteroid_vel = [random.random(), random.random()]
        if random.randint(0, 1): asteroid_ang_vel *= -1        # randomly makes the asteroid's rotation 'negetive'
        if random.randint(0, 1): asteroid_vel[0] *= -1 
        if random.randint(0, 1): asteroid_vel[1] *= -1
        if dist(asteroid_pos, my_ship.get_position()) > my_ship.radius * 4:
            rock_group.append(Sprite(asteroid_pos, asteroid_vel, 0, asteroid_ang_vel, asteroid_image, asteroid_info))
            rock_timer.stop(); rock_timer = simplegui.create_timer(rock_interval, rock_spawner)
            rock_timer.start()
        else: rock_spawner()
            
def reset_game():
    global started, rock_group, missile_group, explosion_group, my_ship, rock_interval
    started = False
    rock_group = []
    missile_group = []
    explosion_group = []
    rock_interval = difficulty
    my_ship.thrust(False); my_ship.pos = [WIDTH / 2, HEIGHT / 2]
    my_ship.angle_vel = 0; my_ship.vel = [0, 0]
    
def set_volume(volume):
    volume = int(volume)
    if volume > 10: volume = 10
    if volume < 0: volume = 0
    soundtrack.set_volume(volume / 10.0)
    explosion_sound.set_volume(volume / 10.0)
    ship_thrust_sound.set_volume(volume / 10.0)
    missile_sound.set_volume((volume / 10.0) / 2)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprite
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = []
missile_group = []
explosion_group = []
rock_interval = difficulty
soundtrack.rewind()
soundtrack.play()

# register handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset Game", reset_game)
volume = frame.add_input("Game Volume (0 - 10):", set_volume, 185)
rock_timer = simplegui.create_timer(rock_interval, rock_spawner)

# get things rolling
set_volume(6) 
soundtrack.rewind()
soundtrack.play()
frame.start()
