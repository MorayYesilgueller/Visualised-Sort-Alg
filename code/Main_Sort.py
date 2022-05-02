import pygame
import random
import numpy
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox



######################################################################################
#PYGAME STUFF


#pygame init
pygame.font.init()
screen = pygame.display.set_mode((620,620))
width = screen.get_width()
height = screen.get_height()

#colors
black= pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
color_light = (170,170,170)
color_dark = (100,100,100)


#text
smallfont = pygame.font.SysFont('Corbel',25)
playall = smallfont.render('Start all' , True , black)
playbubble = smallfont.render('Start Bubble' , True , black)
playmerge = smallfont.render('Start Merge' , True , black)
playshell = smallfont.render('Start Shell' , True , black)


#slider
slider = Slider(screen, 80, 400, 500, 20, min=2, max=310, step=1)
output = TextBox(screen, 475, 450, 50, 50, fontSize=30)
output.disable()



#draws all lines in given array
def draw_all(array):
    for i in range(len(array)):
        pygame.draw.line(screen,white,(1+2*(array[i,1]),height),(1+2*(array[i,1]),1))
        pygame.draw.line(screen,black,(1+2*(array[i,1]),height),(1+2*(array[i,1]),height-50-array[i,0]))
        pygame.display.update()


#draws two lines from given array
def draw_double(array,i,j):
    pygame.draw.line(screen,white,(1+2*i,height),(1+2*i,1))
    pygame.draw.line(screen,white,(1+2*(j),height),(1+2*(j),1))
    pygame.draw.line(screen,black,(1+2*(j),height),(1+2*(j),height-50-array[j,0]))
    pygame.draw.line(screen,black,(1+2*i,height),(1+2*i,height-50-array[i,0]))
    pygame.display.update()

def draw_single(array,i):
    pygame.draw.line(screen,white,(1+2*i,height),(1+2*i,1))
    pygame.draw.line(screen,black,(1+2*i,height),(1+2*i,height-50-array[i,0]))
    pygame.display.update()






############################################
#Algorithms


#Bubble sort algorythm simply compares next element in array ad moves the bigger one up until sorted
def bubble_sort(array):
    length = len(array)
    draw_all(array)

    for i in range(length):
        is_sorted = True


        for j in range(length-i-1):
            if array[j,0]> array[j+1,0]:
                array[j,0],array[j+1,0] = array[j+1,0], array[j,0]
                draw_double(array,array[j,1],array[j+1,1])
                is_sorted = False
        
            if array[j,0] == array [j+1,0]:
                is_sorted = False
        if is_sorted:
            break
    return(array)
    



#merge sort splits array in two and calls itself again until smallest possible array
#the small arrays then get sorted and merged together again
def merge_sort(array):
    if len(array) < 2:
        draw_all(array)
        return array

    #split array recursively
    half = len(array) // 2
    return merger(lhalf= (merge_sort(array[:half])),rhalf=(merge_sort(array[half:])))


#function that sorts and merges 2 arrays
def merger(lhalf,rhalf):

    array= numpy.array([[0,0]])
    il = ir= 0
    row_track= lhalf[0,1]
    counter = 1


    #loop while halves not merged yet
    while numpy.size(array)-2 < numpy.size(lhalf) + numpy.size(rhalf):


        #comparison for elements in both halves based on index ir and il
        #after sorting also applies new position value
        if int(lhalf[il,0]) <= int(rhalf[ir,0]):
            array=numpy.append(array,[lhalf[il]],axis=0)
            array[counter,1] = row_track
            row_track += 1
            counter += 1
            il += 1

        else:
            array= numpy.append(array,[rhalf[ir]],axis=0)
            array[counter,1] = row_track
            row_track += 1
            counter += 1
            ir += 1


        #check if merge completed
        if ir == len(rhalf):
            #merge rest
            for i in range(len(lhalf)-il):
                array=numpy.append(array,[lhalf[il+i]],axis=0)
            
            while counter!= len(array):
                array[counter,1] =row_track
                row_track += 1
                counter += 1
            break
        
        if il == len(lhalf):
            for i in range(len(rhalf)-ir):
                array=numpy.append(array,[rhalf[ir+i]],axis=0)
            while counter!= len(array):
                array[counter,1] =row_track
                row_track += 1
                counter += 1
            break
    
    #remove unnecessary element in array and draw array
    array= numpy.delete(array,0,axis=0)
    draw_all(array)
    return array

#shell sort works by swapping big numbers to the top in a gap and then reducing this gap and repeating
def shell_sort(array):
    space = len(array)// 2
    while space > 0:
        for i in range(space,len(array)):
            temp = array[i,0]
            j = i
            #swap gaps
            while j>= space and array[j-space,0]>temp:
                array[j,0] = array[j-space,0]
                draw_single(array,array[(j),1])
                j -= space
            #swap gaps
            array[j,0]=temp
            draw_single(array,array[j,1])
        #reduce gap size
        space = space//2
    print(array)




#create array 2d array with value and position
def CreateUnsortArray(sample_size):
    array= numpy.array([[random.randrange(1,sample_size), i]for i in range(sample_size)], dtype=int)
    print(array)
    return array




################################################
#GAME LOOP



# main game loop
def main():
    run = True
    while run:
        screen.fill((white)) 



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                run= False
            if event.type == pygame.MOUSEBUTTONDOWN: #different checks for if mouse clicked a button
                sample_size = int(slider.getValue())
                if width/4 <= mouse[0] <= width/4+140 and height/4 <= mouse[1] <= height/4+40:
                    array= CreateUnsortArray(sample_size)
                    array2= numpy.copy(array)
                    array3= numpy.copy(array)
                    bubble_sort(array)
                    screen.fill(white)
                    draw_all(array2)
                    merge_sort(array2)
                    screen.fill(white)
                    draw_all(array3)
                    shell_sort(array3)

                elif width/4+200 <= mouse[0] <= width/4+340 and height/4 <= mouse[1] <= height/4+40:
                    array= CreateUnsortArray(sample_size)
                    bubble_sort(array)

                elif width/4 <= mouse[0] <= width/4+140 and height/4+100 <= mouse[1] <= height/4+140:
                    array= CreateUnsortArray(sample_size)
                    draw_all(array)
                    merge_sort(array)

                elif width/4+200 <= mouse[0] <= width/4+340 and height/4+10 <= mouse[1] <= height/4+140:
                    array= CreateUnsortArray(sample_size)
                    draw_all(array)
                    shell_sort(array)


        #drawing buttons
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen,color_dark,[width/4,height/4,140,40])
        pygame.draw.rect(screen,color_dark,[width/4+200,height/4,140,40])
        pygame.draw.rect(screen,color_dark,[width/4,height/4+100,140,40])
        pygame.draw.rect(screen,color_dark,[width/4+200,height/4+100,140,40])

        #change button color if hovered over button
        if width/4 <= mouse[0] <= width/4+140 and height/4 <= mouse[1] <= height/4+40:
            pygame.draw.rect(screen,color_light,[width/4,height/4,140,40])
        
        elif width/4+200 <= mouse[0] <= width/4+340 and height/4 <= mouse[1] <= height/4+40:
            pygame.draw.rect(screen,color_light,[width/4+200,height/4,140,40])

        elif width/4 <= mouse[0] <= width/4+140 and height/4+100 <= mouse[1] <= height/4+140:
            pygame.draw.rect(screen,color_light,[width/4,height/4+100,140,40])

        elif width/4+200 <= mouse[0] <= width/4+340 and height/4+100 <= mouse[1] <= height/4+140:
            pygame.draw.rect(screen,color_light,[width/4+200,height/4+100,140,40])

        #place text on button
        screen.blit(playall , (width/4+10,height/4+5))
        screen.blit(playbubble , (width/4+210,height/4+5))
        screen.blit(playmerge , (width/4+10,height/4+105))
        screen.blit(playshell , (width/4+210,height/4+105))

        #update slider
        output.setText(slider.getValue())
        pygame_widgets.update(pygame.event.get())

        #update entire display
        pygame.display.update()
    pygame.quit()




if __name__ == "__main__":
    main()











