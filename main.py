# sys for sys.exit(), better for comprehension
import pygame,sys
# contains many constant variables that will be used (QUIT)
# also shorter calls in program
from pygame.locals import *
from time import sleep
from random import randint
from math import sqrt, pi, cos, sin


pygame.init()

WIDTH = 600
HEIGHT = 500
DELAY = 0.05

windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption('Basic Length Tie')

BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

colors = [GRAY,WHITE,RED,GREEN,BLUE]
color =  WHITE

coords = [WIDTH/2,HEIGHT/2]
#angle = randint(0,365)
angle = 360
# 0 right
# 90  down
# 180 left
# 270 up
# 360 right


def radians(angle):
  return angle * pi/180

def goal(deg, distance, coords):
  rad = radians(deg)
  #rad = deg
  radius = distance
  x = radius*cos(rad)
  y = radius*sin(rad)
  return [coords[0]+x,coords[1]+y]

# draw the black background onto the surface
windowSurface.fill(BLACK)
image = pygame.image.load('/home/runner/FirebrickIdenticalSolaris/maxresdefault-removebg-preview.png')
image.fill(color, special_flags=pygame.BLEND_ADD)
windowSurface.blit(image, (coords[0], coords[1]))
#pygame.draw.rect(windowSurface, WHITE, pygame.Rect(coords[0], coords[1], 120, 80))
pygame.display.update()

def cap(angle, coords, distance):
  coords2 = goal(angle,1,coords)
  global colors
  global color
  while coords2[0] < 0 or coords2[0]+120 > WIDTH or coords2[1] < 0 or coords2[1]+80 > HEIGHT:
    if coords2[0] < 0:
      angle = randint(-80,80)
      coords2 = goal(angle,1,coords)
      print("1\t",angle,coords2)
      # 0 right
      # 90  down
      # 180 left
      # 270 up
      # 360 right
    if (coords2[0]+120) > WIDTH:
      angle = randint(100,260)
      coords2 = goal(angle,1,coords)
      print("2\t",angle,coords2)
    if coords2[1] < 0:
      angle = randint(10,170)
      coords2 = goal(angle,1,coords)
      print("3\t",angle,coords2)
    if coords2[1]+80 > HEIGHT:
      angle = randint(190,350)
      coords2 = goal(angle,1,coords)
      print("4\t",angle,coords2)
    color = colors[randint(0,len(colors)-1)]
  return coords2, angle
      

while True:
  # check for quit event
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  windowSurface.fill(BLACK)
  coords, angle = cap(angle,coords,1)
  image.fill(color, special_flags=pygame.BLEND_ADD)
  windowSurface.blit(image, (coords[0], coords[1]))
  pygame.display.update()
  sleep(DELAY)

