# Defender X
# By Robert Miller
# Using Turtle Module

import turtle
import random

wn = turtle.Screen()
wn.setup(1200, 800)
wn.bgcolor("black")
wn.title("Defender X Game by Robert Miller")


class Sprite():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        # self.dx = 0
        # self.dy = 0
        # self.speed = 0
        # self.unit = unit
        # self.active = True

    def render(self):
        # if self.unit == 'defender-weapon':
        #     Sprite.pen.shapesize(0.2, 0.2, 0)
        # else:
        #     Sprite.pen.shapesize(1, 1, 0)
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()

sprites = []

# defenders = []
# defender_weapons = []
#
# attackers = []
# attacker_weapons = []

# Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "circle", "blue"))

# Attackers
for _ in range(10):
    x = random.randint(-300, 500)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "circle", "red"))


# Main game loop
while True:
    for sprite in sprites:
        sprite.render()

wn.mainloop()