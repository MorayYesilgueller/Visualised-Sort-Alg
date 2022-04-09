import pygame

#pygame init
pygame.font.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Sorting Visualizer")
width = 650
length = 900
font = pygame.font.SysFont("comicsans",20)

#colors
black= pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
