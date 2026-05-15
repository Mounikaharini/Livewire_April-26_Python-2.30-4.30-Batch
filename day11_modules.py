'''
import random as r
print(r.random())
print(r.randint(1,10))
print(r.randrange(1,10,1))

import sys as s
a=dir(s)
print(a)
print(s.path)
print("---------------------------------------")
print(s.version)

import socket
host=socket.gethostname()
print(host)

import pywhatkit
a=input("Enter a search content :")
pywhatkit.search(a)

import webbrowser as w
w.open_new_tab("https://www.zomato.com/salem/dindigul-thalappakatti-since-1957-seelanaickenpatti/info")

import calendar as c
print(c.month(2023,8))
print(c.isleap(2023))
print(c.calendar(2025))

import time
print(time.ctime())
print("hii")
time.sleep(5)
print("hello")
for i in range(1,6,1):
    print(i)
    time.sleep(1)

import turtle
star = turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(0) # 0 is the fastest drawing speed
turtle.colormode(255)

# Define a palette of colors
colors = [
    (255, 0, 0), (255, 127, 0), (255, 255, 0), 
    (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
]

# Draw the pattern
for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()

import turtle

t = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
turtle.bgcolor('black')
t.speed(0)  # Fastest speed

for x in range(200):
    t.pencolor(colors[x % 6])  # Cycle through colors
    t.width(x / 100 + 1)       # Gradually increase pen thickness
    t.forward(x)               # Move forward by an increasing amount
    t.left(59)                 # Turn slightly less than 60 degrees for a spiral effect

turtle.done()
'''
def image_display(value):
    import os
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    import pygame
    icon = pygame.image.load(r"C:\Users\R.GOKULAKSHMI\Downloads\img1.jpg")
    pygame.display.set_icon(icon)
    pygame.init()
    image = pygame.image.load(value)
    screen = pygame.display.set_mode(image.get_size())
    screen = pygame.display.set_mode((284,178))
    screen.blit(image,(0,0))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()


image_display(r"C:\Users\R.GOKULAKSHMI\Downloads\img1.jpg")
image_display(r"C:\Users\R.GOKULAKSHMI\Downloads\img2.jpg")
image_display(r"C:\Users\R.GOKULAKSHMI\Downloads\img3.jpg")
image_display(r"C:\Users\R.GOKULAKSHMI\Downloads\img4.jpg")







