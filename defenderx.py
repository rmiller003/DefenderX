# Defender X
# By Robert Miller
# Using Turtle Module

import turtle
import random

wn = turtle.Screen()
wn.setup(1200, 800)
wn.bgcolor("black")
wn.title("Defender X Game by Robert Miller")
wn.tracer(0)


class Sprite():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    def __init__(self, x, y, shape, color, unit):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.heading = 0
        self.speed = 0
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.unit = unit
        self.active = True

    def render(self):
        if self.unit == 'defender-weapon':
            Sprite.pen.shapesize(0.2, 0.2, 0)
        else:
            Sprite.pen.shapesize(1, 1, 0)
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
    def move(self):
        self.x += self.dx

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
    sprites.append(Sprite(x, y, "circle", "blue", "defender"))

# Attackers
for _ in range(10):
    x = random.randint(300, 500)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "triangle", "red", "attacker"))
    sprites[-1].heading = 180 #left
    sprites[-1].dx = -0.2

# Weapons
for _ in range(10):
    x = -1000
    y = -1000
    sprites.append(Sprite(x, y, "circle", "lightblue", "defender-weapon"))
    sprites[-1].active = False

# Main game loop
while True:
    # Assign weapon to sprite
    for sprite in sprites:
        if sprite.unit == "defender":
            for weapon in sprites:
                if weapon.unit == "defender-weapon" and weapon.active == False:
                    weapon.x = sprite.x
                    weapon.y = sprite.y
                    weapon.dx = 1
                    weapon.active = True
                    break


    # Move
    for sprite in sprites:
        sprite.move()
    # Render
        sprite.render()

    # Update screen
    wn.update()

    # Clear screen
    Sprite.pen.clear()

