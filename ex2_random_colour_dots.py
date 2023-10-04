import turtle
import random

#you can change the colours in the list
all_colours = ['coral', 'light salmon', 'sienna', 'dark sea green', 'blanched almond']

world = turtle.Screen()
world.setup(width=400, height=400)
world.setworldcoordinates(0,0,400,400)
world.colormode(255)


tula = turtle.Turtle()
tula.width(5)


#instructions to draw a dot on screen
user_x = random.randint(0,400)
tula.up()
tula.goto(user_x, 200)
tula.down()

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

colour = (red,green,blue)
tula.color(colour)

diameter = random.randint(1,200)
tula.dot(diameter)

#2

user_x = random.randint(0,400)
tula.up()
tula.goto(user_x, 200)
tula.down()

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

colour = (red,green,blue)
tula.color(colour)

diameter = random.randint(1,200)
tula.dot(diameter)

#3

user_x = random.randint(0,400)
tula.up()
tula.goto(user_x, 200)
tula.down()

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

colour = (red,green,blue)
tula.color(colour)

diameter = random.randint(1,200)
tula.dot(diameter)

#4
user_x = random.randint(0,400)
tula.up()
tula.goto(user_x, 200)
tula.down()

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

colour = (red,green,blue)
tula.color(colour)

diameter = random.randint(1,200)
tula.dot(diameter)

#5
user_x = random.randint(0,400)
tula.up()
tula.goto(user_x, 200)
tula.down()

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

colour = (red,green,blue)
tula.color(colour)

diameter = random.randint(1,200)
tula.dot(diameter)




