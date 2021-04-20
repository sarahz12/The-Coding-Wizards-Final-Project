#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:39:38 2021

@author: laurelmyers
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:27:13 2021

@author: laurelmyers


"""

#generated notes starting from c4 up to B5:
    
import numpy as np
import matplotlib.pyplot as plt

samplerate = 44100 #Frequecy in Hz

def get_wave(freq, duration = 0.75):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    
    wave = (amplitude * np.sin(2 * np.pi * freq * t) )+ (amplitude/2.) * np.sin(1. * np.pi * freq * t)  
    return wave

def get_piano_notes_2():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    all_notes = ['C4_2', 'csharp4_2', 'D4_2','dsharp4_2', 'E4_2', 'F4_2', 'fsharp4_2', 'G4_2', 'gsharp4_2', 'A5_2', 'asharp5_2', 'B5_2', 'C5_2'] 
    base_freq = 261.63 #Frequency of Note A3, the A before middle C
    
    note_freqs_2 = {all_notes[i]: base_freq * pow(2,(i/12)) for i in range(len(all_notes))}        
    note_freqs_2[''] = 0.0 # silent note
    
    return note_freqs_2
  
  # To get the piano note's frequencies
note_freqs_2 = get_piano_notes_2()


from scipy.io.wavfile import write

C4_2 = get_wave(note_freqs_2['C4_2'], 1)
csharp4_2 = get_wave(note_freqs_2['csharp4_2'], 1)
D4_2 = get_wave(note_freqs_2['D4_2'], 1)
dsharp4_2 = get_wave(note_freqs_2['dsharp4_2'])
E4_2 = get_wave(note_freqs_2['E4_2'], 1)
F4_2 = get_wave(note_freqs_2['F4_2'], 1)
fsharp4_2 = get_wave(note_freqs_2['fsharp4_2'])
G4_2 = get_wave(note_freqs_2['G4_2'])
gsharp4_2 = get_wave(note_freqs_2['gsharp4_2'], 1)
A5_2 = get_wave(note_freqs_2['A5_2'])
asharp5_2 = get_wave(note_freqs_2['asharp5_2'], 1)
B5_2= get_wave(note_freqs_2['B5_2'])
C5_2= get_wave(note_freqs_2['C5_2'])

# #create separate wave file for each note:
write('C4_2.wav', samplerate, C4_2.astype(np.int16))
write('csharp4_2.wav', samplerate, csharp4_2.astype(np.int16))
write('D4_2.wav', samplerate, D4_2.astype(np.int16))
write('dsharp4_2.wav', samplerate, dsharp4_2.astype(np.int16))
write('E4_2.wav', samplerate, E4_2.astype(np.int16))
write('F4_2.wav', samplerate, F4_2.astype(np.int16))
write('fsharp4_2.wav', samplerate, fsharp4_2.astype(np.int16))
write('G4_2.wav', samplerate, G4_2.astype(np.int16))
write('gsharp4_2.wav', samplerate, gsharp4_2.astype(np.int16))
write('A5_2.wav', samplerate, A5_2.astype(np.int16))
write('asharp5_2.wav', samplerate, asharp5_2.astype(np.int16))
write('B5_2.wav', samplerate, B5_2.astype(np.int16))
write('C5_2.wav', samplerate, C5_2.astype(np.int16))

#--------------GUI CODE: NOT OURS, JUST ADDED THE NOTES GENERATED--------------------------
import pygame
from playsound import playsound

black = (0,0,0)
white = (255,255,255)
grey = (175,175,175)
pygame.init()

background = pygame.image.load('harrypotter.jpeg')

A = 'A5_2.wav'
B = 'B5_2.wav'
C = 'C4_2.wav'
C1 = 'C5_2.wav'
D = 'D4_2.wav'
E = 'E4_2.wav'
F = 'F4_2.wav'
G = 'G4_2.wav'


C_s = 'csharp4_2.wav'
D_s = 'dsharp4_2.wav'
F_s = 'fsharp4_2.wav'
G_s = 'gsharp4_2.wav'
A_s = 'asharp5_2.wav'


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def black_btn(x,note):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_coord = 55*x+175
    y_coord = 200

    
# generate a list with notes where - is a rest:
    
def split_song_data(song_notes):
    song_split = song_notes.split('-')
    return song_split
    
    

twinkle_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'

    for note in range (len(twinkle_songsong)):
        

if .
        pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
        playsound(note,False)

    else:
        pygame.draw.rect(screen,black,(x_coord,y_coord,35,100))


def white_btn(x,note):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_coord = 55*x+140
    y_coord = 200
    x_coord1 = 55*x + 175 # Where the black key starts
    y_coord1 = 275 # where the black keys start and are 100 long.

    if (y_coord+100< mouse[1] < y_coord+175) and (x_coord+50 > mouse[0] > x_coord):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 > mouse[0] > x_coord) and (x in (1,4)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (1,4)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 15) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 35) and (x in (2,5,6)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+15 < mouse[0] < x_coord+50) and (x in (3,7)):
        pygame.draw.rect(screen,grey,(x_coord +15,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
        if click[0] == 1:
            playsound(note,False)

    elif (x == 8) and (y_coord < mouse[1] < y_coord+175) and (x_coord < mouse[0] < x_coord + 50):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    else:
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

import sys

running = True
while running:
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()

    screen.fill((0,100,130))
    screen.blit(background, (0, 0))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Piano", largeText)
    TextRect.center = (400,100)
    screen.blit(TextSurf, TextRect)


    white_btn(1,C)
    white_btn(2,D)
    white_btn(3,E)
    white_btn(4,F)
    white_btn(5,G)
    white_btn(6,A)
    white_btn(7,B)
    white_btn(8,C1)

    black_btn(1,C_s)
    black_btn(2,D_s)
    black_btn(4,F_s)
    black_btn(5,G_s)
    black_btn(6,A_s)

    pygame.display.update()