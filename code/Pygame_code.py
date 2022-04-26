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








#draws all lines in given array
def draw_all(array):
    for i in range(len(array)):
        pygame.draw.line(screen,white,(50+2*(array[i,1]),10),(50+2*(array[i,1]),1000))
        pygame.draw.line(screen,black,(50+2*(array[i,1]),10),(50+2*(array[i,1]),50+array[i,0]))
        pygame.display.update()


#draws two lines from given array
def draw_double(array,i,j):
    pygame.draw.line(screen,white,(50+2*i,10),(50+2*i,1000))
    pygame.draw.line(screen,white,(50+2*(j),10),(50+2*(j),1000))
    pygame.draw.line(screen,black,(50+2*(j),10),(50+2*(j),50+array[j,0]))
    pygame.draw.line(screen,black,(50+2*i,10),(50+2*i,50+array[i,0]))
    pygame.display.update()

def draw_single(array,i):
    pygame.draw.line(screen,white,(50+2*i,10),(50+2*i,1000))
    pygame.draw.line(screen,black,(50+2*i,10),(50+2*i,50+array[i,0]))
    pygame.display.update()