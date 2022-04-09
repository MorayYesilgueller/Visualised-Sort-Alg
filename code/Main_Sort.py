import random
import pygame
import numpy





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

def draw_all(array):
    for i in range(len(array)):
        pygame.draw.line(screen,white,(50+2*(array[i,1]),10),(50+2*(array[i,1]),1000))
        pygame.draw.line(screen,black,(50+2*(array[i,1]),10),(50+2*(array[i,1]),array[i,0]))
        pygame.display.update()


#what in gods name is wrong
def draw_single(array,i,j):
    pygame.draw.line(screen,white,(50+2*i,10),(50+2*i,1000))
    pygame.draw.line(screen,white,(50+2*(j),10),(50+2*(j),1000))
    pygame.draw.line(screen,black,(50+2*(j),10),(50+2*(j),array[i+1]))
    pygame.draw.line(screen,black,(50+2*i,10),(50+2*i,array[i]))
    pygame.display.update()


#Bubble sort algorythm
def BumbleSortus(array):
    length = len(array)
    draw_all(array)

    for i in range(length):
        is_sorted = True


        for j in range(length-i-1):
            if array[j]> array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                draw_single(array,j,(j+1))
                is_sorted = False
        
            if array[j] == array [j+1]:
                is_sorted = False
        if is_sorted:
            break
    return(array)
    


#merging of two arrays using 2d arrays now 
def merger(lhalf,rhalf):

    arrayus= numpy.array([[0,0]])
    il = ir= 0
    row_track= lhalf[0,1]
    counter = 1

    while numpy.size(arrayus)-2 < numpy.size(lhalf) + numpy.size(rhalf):

        if int(lhalf[il,0]) <= int(rhalf[ir,0]):
            arrayus=numpy.append(arrayus,[lhalf[il]],axis=0)
            arrayus[counter,1] = row_track
            row_track += 1
            counter += 1
            il += 1

        else:
            arrayus= numpy.append(arrayus,[rhalf[ir]],axis=0)
            arrayus[counter,1] = row_track
            row_track += 1
            counter += 1
            ir += 1

        if ir == len(rhalf):
            for i in range(len(lhalf)-il):
                arrayus=numpy.append(arrayus,[lhalf[il+i]],axis=0)
            while counter!= len(arrayus):
                arrayus[counter,1] =row_track
                row_track += 1
                counter += 1
            break

        if il == len(lhalf):
            for i in range(len(rhalf)-ir):
                arrayus=numpy.append(arrayus,[rhalf[ir+i]],axis=0)
            while counter!= len(arrayus):
                arrayus[counter,1] =row_track
                row_track += 1
                counter += 1
            break
    
    #print(arrayus)
    arrayus= numpy.delete(arrayus,0,axis=0)
    #print(arrayus)
    draw_all(arrayus)
    return arrayus

#make merge sort it should work recursively
def merge_sort(array):
    if len(array) < 2:
        draw_all(array)
        return array

    half = len(array) // 2
    #draw_all(array)
    return merger(lhalf= (merge_sort(array[:half])),rhalf=(merge_sort(array[half:])))


#create array with arrays in it to keep track of position
def CreateUnsortArray():
    array= numpy.array([[random.randrange(1,500), i]for i in range(300)], dtype=int)
    print(array)
    return array














not_finished = True
run = True
# main game loop
while run:
    screen.fill((white)) 
    while not_finished:

        array= CreateUnsortArray()
        array=merge_sort(array)
        draw_all(array)
        not_finished= False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run= False
      
pygame.quit()





