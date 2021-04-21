#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:47:13 2021

@author: laurelmyers
"""
# set up all the base white and black keys

# parse the songs

# play the song

#generate piano:

pygame.draw.rect(screen,white,(195,200,50,175)) #For C key

pygame.draw.rect(screen,white,(250,200,35,100))
pygame.draw.rect(screen,white,(250,200 +100,50,75)) #for D key

pygame.draw.rect(screen,white,(305,200,50,175))

pygame.draw.rect(screen,white,(360,200,50,175))

pygame.draw.rect(screen,white,(415,200,50,175))

pygame.draw.rect(screen,white,(470,200,50,175))

pygame.draw.rect(screen,white,(525,200,35,100))
pygame.draw.rect(screen,white,(525,200 +100,50,75)) #for B key

pygame.draw.rect(screen,white,(580,200,50,175))


#for black keys
pygame.draw.rect(screen,black,(230,200,35,100))

pygame.draw.rect(screen,black,(285,200,35,100))

pygame.draw.rect(screen,black,(340,200,35,100))

pygame.draw.rect(screen,black,(395,200,35,100))

pygame.draw.rect(screen,black,(450,200,35,100))


twinkle_notes = 'C--C--G--G--A--A--G---F--F--E--E--D--D--C---G--G--F--F--E--E--D---G--G--F--F--E--E--D---C--C--G--G--A--A--G---F--F--E--E--D--D--C'
twinkle_song = split_song_data(twinkle_notes)

dict = {'C': [195, 200], 'D': [250,200],'E':[305,200], 'F': [360,200], 
        'G':[415,200], 'A':[470,200], 'B': [525,200], 'C1': [580,200], 
        'C_s': [230,200], 'D_s': [285,200], 'F_s': [340,200], 'G_s': [395,200],'A_s': [450,200]} # fill in this
prevNote = None

for note in twinkle_song:
    if prevNote is not None:
        prev_x = dict[prevNote][0]
        prev_y = dict[prevNote][1]     
        # rect(prev_x, prev_y, 100, 175) # white
    x_coord = dict[note][0]
    y_coord = dict[note][1]
    
    if note == '-':
        playsound('Silence.wav')
        
    if note == 'B' or note == 'D': 
        pygame.draw.rect(screen,gray,(x_coord,y_coord,35,100))
        pygame.draw.rect(screen,gray,(x_coord,y_coord +100,50,75))
  
    if prevNote == 'B' or prevNote == 'D':
        pygame.draw.rect(screen,white,(prev_x,prev_y,35,100))
        pygame.draw.rect(screen,white,(prev_x,prev_y +100,50,75))
        
    else:
        pygame.draw.rect(screen,white,(prev_x,prev_y,50,175))
        
    playsound(note)
   
    prevNote = note
    

    # timer (1 sec)
    
    
    
    


