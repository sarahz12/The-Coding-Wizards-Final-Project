#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:27:13 2021

# Written by: Sarah Zylberfuden
 Pair programmed with Michelle Liu
# Debugging: Laurel Myers
Time Spent: 9 hours


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
    t = np.linspace(0, duration, int(samplerate * duration)) # creating a numeric sequence
    # creating the actual wave by combining amplitude, freq, t
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

# so that code can recognize the sound of the keys
from scipy.io.wavfile import write

C4_2 = get_wave(note_freqs_2['C4_2'], 1) # retrieving note frequencies, duration
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
# we chose the background image behind the piano
background = pygame.image.load('harrypotter.jpeg')
# connecting note names to the wave files
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

# display the screen 800,600 = dimensions
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# defining the black keys
def black_btn(x,note):
     mouse = pygame.mouse.get_pos() # clicking detection
     click = pygame.mouse.get_pressed()
     x_coord = 55*x+175
     y_coord = 200

     if x_coord+35 > mouse[0] > x_coord and y_coord+100>mouse[1]>y_coord:
         pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100)) # populating surface with 'objects' (keys) to be displayed
         if click[0] == 1:
             playsound(note,False)
    
     else:
         pygame.draw.rect(screen,black,(x_coord,y_coord,35,100))

# defining white keys
def white_btn(x,note):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_coord = 55*x+140 # numbers retrieved from other code
    y_coord = 200
    x_coord1 = 55*x + 175 
    y_coord1 = 275 

    if (y_coord+100< mouse[1] < y_coord+175) and (x_coord+50 > mouse[0] > x_coord):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 > mouse[0] > x_coord) and (x in (1,4)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75)) # This is to keep the piano shape: without it, there would be only a white rect and nothing near the black keys
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (1,4)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 15) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 35) and (x in (2,5,6)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175)) # makes the key grey when clicked on 
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+15 < mouse[0] < x_coord+50) and (x in (3,7)):
        pygame.draw.rect(screen,grey,(x_coord +15,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75)) # This is to keep the piano shape: without it, there would be only a white rect and nothing near the black keys
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
# goal to create a canvas of desired size and then create a surface of smaller size containing the object to be displayed
    screen.fill((0,100,130)) # color argument
    screen.blit(background, (0, 0)) # overlap, the surface on the canvas at the rect position 
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Piano", largeText)
    TextRect.center = (400,100)
    screen.blit(TextSurf, TextRect)


    white_btn(1,C) # number of location and note
    white_btn(2,D)
    white_btn(3,E)
    white_btn(4,F)
    white_btn(5,G)
    white_btn(6,A)
    white_btn(7,B)
    white_btn(8,C1)

    black_btn(1,C_s) # same as above but with sharps 
    black_btn(2,D_s)
    black_btn(4,F_s)
    black_btn(5,G_s)
    black_btn(6,A_s)

    pygame.display.update()
    #system exit for quit