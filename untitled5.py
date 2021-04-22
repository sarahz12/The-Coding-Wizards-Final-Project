#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:39:16 2021

@author: laurelmyers
"""
import os

os.system("stringsplittest.py")

twinkle_notes = 'C--C--G--G--A--A--G---F--F--E--E--D--D--C---G--G--F--F--E--E--D---G--G--F--F--E--E--D---C--C--G--G--A--A--G---F--F--E--E--D--D--C'
twinkle_song = split_song_data(twinkle_notes)

print(twinkle_song)

dict = {'C': [195, 200], 'D': [250,200],'E':[305,200], 'F': [360,200], 
        'G':[415,200], 'A':[470,200], 'B': [525,200], 'C1': [580,200], 
        'C_s': [230,200], 'D_s': [285,200], 'F_s': [340,200], 'G_s': [395,200],'A_s': [450,200], '':[0,0]} # 
prevNote = None

for note in twinkle_song:
    print(prevNote)
    print(note)
    if note == '':
                playsound('Silence.wav')
    else:
    
        x_coord = dict[str(note)][0]
        y_coord = dict[str(note)][1]
    
        if prevNote is not None:
        
            prev_x = dict[str(prevNote)][0]
            prev_y = dict[str(prevNote)][1]
        
            if prevNote == 'B' or prevNote == 'D':
                    pygame.draw.rect(screen,white,(prev_x,prev_y,35,100))
                    pygame.draw.rect(screen,white,(prev_x,prev_y +100,50,75))
                    
            else:
                pygame.draw.rect(screen,white,(prev_x,prev_y,50,175))
                # rect(prev_x, prev_y, 100, 175) # white
                
        if note == 'B' or note == 'D': 
            pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
            pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
          
        else:
            pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        
        playsound(note + '.wav')
       
    prevNote = note
    
   
   