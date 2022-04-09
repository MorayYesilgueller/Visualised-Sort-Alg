import pygame
from Algorythms import *










not_finished = True
run = True
# main game loop
while run:
    screen.fill((white)) 
    while not_finished:

        array= CreateUnsortArray()
        array2= numpy.copy(array)
        BumbleSortus(array)
        screen.fill(white)
        draw_all(array2)
        merge_sort(array2)
        not_finished= False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run= False
      
pygame.quit()





