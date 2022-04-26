import numpy
import pygame
import random
from Pygame_code import *



#Bubble sort algorythm simply 
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
def CreateUnsortArray():
    array= numpy.array([[random.randrange(1,500), i]for i in range(500)], dtype=int)
    print(array)
    return array



