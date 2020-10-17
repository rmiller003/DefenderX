# Defender X
# By Robert Miller
# Using Turtle Module
# Python 3.7

import turtle
import random
import pygame
import math
import time


from pygame import mixer

wn = turtle.Screen()
wn.setup(1200, 800)
wn.bgcolor("black")
wn.title("Mass Attack1 Game by Robert Miller")
wn.tracer(0)

pygame.init()

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
        self.heading = 0
        self.speed = 0
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.active = True
        self.heading = 0
        self.health = 10

    def render(self):
            Sprite.pen.shapesize(1, 1, 0)

            Sprite.pen.goto(self.x, self.y)
            Sprite.pen.shape(self.shape)
            Sprite.pen.color(self.color)
            Sprite.pen.stamp()


    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_collision(self, other, tolerance):
        d = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if d < tolerance:
            return True
        else:
            return False

# Background Sound
mixer.music.load('bensound-evolution.mp3')
mixer.music.play(-1)


class Defender(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

    def render(self):
        Sprite.pen.shapesize(1, 1, 0)

        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()


class DefenderWeapon(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

    def render(self):
        Sprite.pen.shapesize(0.2, 0.2, 0)

        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > 390 or self.y < -390:
            self.dy *= -1


class Attacker(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

    def render(self):
        Sprite.pen.shapesize(1, 1, 0)

        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.colour(self.color)
        Sprite.pen.stamp()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Boarder checks
        if self.unit == "defender-weapon" and self.x > 600:
            self.x = -1000
            self.active = False

        if self.unit == "attacker":
            if self.y > 300 or self.y < -300:
                self.dy *= -1

sprites = []

defenders = []
defender_weapons = []

attackers = []
attacker_weapons = []

# Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    defenders.append(Sprite(x, y, "circle", "blue"))

# Attackers
for _ in range(100):
    x = random.randint(300, 500)
    y = random.randint(-300, 300)
    attackers.append(Defender(x, y, "triangle", "red",))
    attackers[-1].heading = 180 #left

# Weapons
for _ in range(50):
    x = -1000
    y = -1000
    defender_weapons.append(DefenderWeapon(x, y, "circle", "lightblue"))
    defender_weapons[-1].active = False
    defender_weapons[-1].dy = random.randint(-10, 10) / 20.0

def add_defender(x, y):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    defenders.append(Sprite(x, y, "circle", "blue",))
    defender_weapons.append(())

# Main game loop
while True:
    # Assign weapon to sprite
    for defender in defenders:
            for weapon in defender_weapons:
                if weapon.active == False and random.randint(0, 100) > 95:
                    weapon.x = defender.x
                    weapon.y = defender.y
                    weapon.dx = 10
                    weapon.active = True
                    break

# Check for collisions between enemy & weapons
    for weapon in defender_weapons:
        if weapon.active == True:
            for attacker in attackers:
                if attacker.is_collision(weapon, 12):
                    attacker.x += 1200
                    attacker.y = random.randint(-300, 300)
                    weapon.x = -1000
                    weapon.active = False
                    weapon.dx = 0
                    break

    # Move
    for sprite in defenders:
        sprite.move()
        sprite.render()

    for sprite in defender_weapons:
        sprite.move()
        sprite.render()

    for sprite in attackers:
        sprite.move()
        sprite.render()

    # Update screen
    wn.update()

    # Check for a win
    if len(attackers) == 0:
        print("The Defenders win.")
        time.sleep(3)
        exit()

    if len(defenders) == 0:
        print("The Attackers win.")
        time.sleep(3)
        exit()

    # Clear screen
    Sprite.pen.clear()

