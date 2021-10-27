# - Importing Libraries
import turtle as t
import random as rnd
wn = t.Screen()

#Create Game lists

gifs = ('candy.gif', 'candycorn.gif', 'ghost.gif', 'pumpkin.gif', 'witch.gif')
poss_angles = (0, 45, 90, 135, 180, 225, 270, 315)

#Creating Game Functions

def rand_coords():
  xcor = rnd.randint(-200, 200)
  ycor = rnd.randint(-200, 200)
  return xcor, ycor

def pick_angle(poss_angles):
  angle_index = rnd.randint(0, len(poss_angles) - 1)
  angle = poss_angles[angle_index]
  return angle

def choose_image(gifs):
  gif_index = rnd.randint(0, len(gifs) - 1)
  image = poss_angles[gif_index]
  return image

def change_pos(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

def increments(angle, x, y):
  if angle == 0:
    x += 1
    y += 0
  elif angle == 45:
    x += 1
    y += 1
  elif angle == 90:
    x += 0
    y += 1
  elif angle == 135:
    x -= 1
    y += 1
  elif angle == 180:
    x -= 1
    y += 0
  elif angle == 225:
    x -= 1
    y -= 1
  elif angle == 270:
    x += 0
    y -= 1
  elif angle == 315:
    x += 1
    y -= 1
  


def move_gif(gifs, poss_angles):
  image = choose_image(gifs)
  wn.addshape(image)
  gif = t.turtle(shape = image)

  angle = pick_angle(poss_angles)
  
  x, y = rand_coords()
  change_pos(x, y)

  curr_xcor = t.xcor()
  curr_ycor = t.ycor()

  while -400 <= curr_xcor <= 400 and -400 <= curr_ycor <= 400:
    curr_xcor = t.xcor()
    curr_ycor = t.ycor()
    t.setheading(angle)
    t.stamp
    increments(angle, x, y)

move_gif(gifs, poss_angles)



