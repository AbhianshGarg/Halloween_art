# imports
import turtle as trtl
import random as r
import time

t = trtl.Turtle()
counter = trtl.Turtle()
timekeeper = trtl.Turtle()

#variables
t.speed(2)
t.penup()


#Screen Setup
wn = trtl.Screen()
wn.setup(892, 505)
wn.bgpic('background.png')

gifs = ["candy.gif", "ghost.gif", "pumpkin.gif", "witch_hat.gif", "bat.gif"]

image = r.choice(gifs)
wn.addshape(image)
t.shape(image)


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

def timer_setup():
    global score, font_setup, timer, counter_interval, timer_up, play
    score = 0
    font_setup = ("Arial", 20, "normal")
    timer = 15 
    counter_interval = 1000   
    timer_up = False
    play = True


def player_count():
    while True:
        p_count = input('How many players would like to play? (No more than three): ')
        try:
            p_count = int(p_count)
        except ValueError:
            print('Whole numbers only please.')
            continue
        if p_count > 3:
            print('No more than three players!')
            continue
        break
    return p_count


def move():
    randX = r.randint(-446, 446) 
    randY = r.randint(-252, 252) 
    t.goto(randX, randY)
   

def update_score(x,y):
    global score 
    global play
    if play == True:
        score += 1
        counter.clear()
        counter.write("Score: " + str(score),font=font_setup)

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

print('''
                Welcome to Ultimate CPS!
Try to click the moving image as many times as you can!
''')

score_list = []

player_count = player_count()
for i in range(player_count):
    timer_setup()
    time_limit()
    while play == True:
        move()
        t.onclick(update_score)
    else:
        score_list.append(score)
    if i + 1 < player_count:
        print('Next game starting in 5 seconds!')
        time.sleep(5)

#Get player with highest score
index = score_list.index(max(score_list)) + 1
print('Player ' + str(index) + ' is the winner with a score of ' + str(score_list[index - 1]) + '!')



wn.mainloop()
