import pygame
from Algorithms import *



# main game loop
def main():
    not_finished = True
    run = True
    while run:
        screen.fill((white)) 
        while not_finished:

            array= CreateUnsortArray()
            array2= numpy.copy(array)
            bubble_sort(array)
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




if __name__ == "__main__":
    main()





