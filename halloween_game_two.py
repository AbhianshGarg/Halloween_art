# imports
import turtle as trtl
import random as r

t = trtl.Turtle()
counter = trtl.Turtle()
timekeeper = trtl.Turtle()

# variables and other
t.speed(10)
t.penup()

score = 0
font_setup = ("Arial", 20, "normal")
timer = 30 
counter_interval = 1000   
timer_up = False
play = True

#Screen Setup
wn = trtl.Screen()
wn.setup(892, 505)
wn.bgpic('background.png')


#List
gifs = ["candy.gif", "ghost.gif", "pumpkin.gif", "witch_hat.gif", "bat.gif"]

# score writer
counter.penup()
counter.hideturtle()
counter.goto(-400, 185)

# time keeper
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-250, 185)

# functions
def move():
    randX = r.randint(-446, 446) 
    randY = r.randint(-252, 252) 
    t.goto(randX, randY)


def update_score_one(x,y):
    global score 
    global play
    if play == True:
        score += 1
        counter.clear()
        counter.write("Score: " + str(score),font=font_setup)
        move()


def time_limit():
  global timer, timer_up
  global play
  timekeeper.clear()
  timekeeper.hideturtle()
  if timer <= 0:
    timekeeper.write("Time's Up", font=font_setup)
    timer_up = True
    play = False
  else:
    timekeeper.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    timekeeper.getscreen().ontimer(time_limit, counter_interval)

# gameplay
time_limit()

while play == True:




wn.mainloop()