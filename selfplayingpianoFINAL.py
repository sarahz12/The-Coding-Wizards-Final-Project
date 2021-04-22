#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:39:38 2021

Written by: Laurel Myers and Sarah Zylberfuden
Took turns pair programming
Debugging: Michelle Liu
Time taken: 9 hours (including research)


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
    
    wave = (amplitude * np.sin(2 * np.pi * freq * t) )+ (amplitude/2.) * np.sin(1. * np.pi * freq * t)  # sine wave
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
write('C.wav', samplerate, C4_2.astype(np.int16))
write('C_s.wav', samplerate, csharp4_2.astype(np.int16))
write('D.wav', samplerate, D4_2.astype(np.int16))
write('D_s.wav', samplerate, dsharp4_2.astype(np.int16))
write('E.wav', samplerate, E4_2.astype(np.int16))
write('F.wav', samplerate, F4_2.astype(np.int16))
write('F_s.wav', samplerate, fsharp4_2.astype(np.int16))
write('G.wav', samplerate, G4_2.astype(np.int16))
write('G_s.wav', samplerate, gsharp4_2.astype(np.int16))
write('A.wav', samplerate, A5_2.astype(np.int16))
write('A_s.wav', samplerate, asharp5_2.astype(np.int16))
write('B.wav', samplerate, B5_2.astype(np.int16))
write('C1.wav', samplerate, C5_2.astype(np.int16))

#--------------GUI CODE: NOT OURS, JUST ADDED THE NOTES GENERATED--------------------------
import pygame
from playsound import playsound

black = (0,0,0)
white = (255,255,255)
grey = (175,175,175)
pygame.init()

background = pygame.image.load('harrypotter.jpeg')

A = 'A.wav'
B = 'B.wav'
C = 'C.wav'
C1 = 'C1.wav'
D = 'D.wav'
E = 'E.wav'
F = 'F.wav'
G = 'G.wav'


C_s = 'C_s.wav'
D_s = 'D_s.wav'
F_s = 'F_s.wav'
G_s = 'G_s.wav'
A_s = 'A_s.wav'


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
# generate a list with notes where - is a rest:
    
def split_song_data(song_notes):
    song_split = song_notes.split('-')
    return song_split

# following this formula, taken from another git user: 
    #black keys:
    #x_coord = 55*x+175
     #y_coord = 200
     
     #white keys: 
    # x_coord = 55*x+140
    y_coord = 200

def piano_gui():
    
    pygame.draw.rect(screen,white,(195,200,50,175)) #For C key

    pygame.draw.rect(screen,white,(250,200,35,100)) #for D key
    pygame.draw.rect(screen,white,(250,200 +100,50,75)) # This is to create a second white rectangle directly below the thinner white triangle, this is done in order to have the white key overlapped by two black keys

    pygame.draw.rect(screen,white,(305,200,50,175)) # for E key
    
    pygame.draw.rect(screen,white,(360,200,50,175)) # for F key
    
    pygame.draw.rect(screen,white,(415,200,50,175)) # for G key
    
    pygame.draw.rect(screen,white,(470,200,50,175)) # for A key
    
    pygame.draw.rect(screen,white,(525,200,50,100)) #for B key
    pygame.draw.rect(screen,white,(525,200 +100,50,75)) 
    
    pygame.draw.rect(screen,white,(580,200,50,175)) # for C1 key
    
    
    #for black keys
    pygame.draw.rect(screen,black,(230,200,35,100)) # C sharp
    
    pygame.draw.rect(screen,black,(285,200,35,100)) # D sharp
    
    pygame.draw.rect(screen,black,(395,200,35,100)) # F sharp
    
    pygame.draw.rect(screen,black,(450,200,35,100)) # G sharp
    
    pygame.draw.rect(screen,black,(505,200,35,100)) # A sharp

# This is a second function created, because, at first, we noticed that the black keys would tend to disappear
# This function is to prevent that!  
def draw_black_keys():
    pygame.draw.rect(screen,black,(230,200,35,100))
    
    pygame.draw.rect(screen,black,(285,200,35,100))
    
    pygame.draw.rect(screen,black,(395,200,35,100))
    
    pygame.draw.rect(screen,black,(450,200,35,100))
    
    pygame.draw.rect(screen,black,(505,200,35,100))

def auto_play():
    # line 177 have the keys to the song being played and line 178 splits the notes when played
    twinkle_notes = 'C--C--G--G--A--A--G---F--F--E--E--D--D--C---G--G--F--F--E--E--D---G--G--F--F--E--E--D---C--C--G--G--A--A--G---F--F--E--E--D--D--C'
    twinkle_song = split_song_data(twinkle_notes) # when the note has three dashes instead of two, that indicates a pause

    print(twinkle_song)
    
    key_dict = {'C': [195, 200], 'D': [250,200],'E':[305,200], 'F': [360,200], 
            'G':[415,200], 'A':[470,200], 'B': [525,200], 'C1': [580,200], 
            'C_s': [230,200], 'D_s': [285,200], 'F_s': [395,200], 'G_s': [450,200],'A_s': [505,200], '':[0,0]} # 
    prevNote = ''
    
    play_file_name = ''
    for note in twinkle_song:
        print(note)
        print(prevNote)
        if note == '':
            play_file_name = 'Silence.wav'
            
        else:
        
            x_coord = key_dict[note][0]
            y_coord = key_dict[note][1]
            
            #turns the note being played grey
            if note == 'D': 
                pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100)) # last two numbers are width and height
                pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
                draw_black_keys()
            elif note == 'B':
                 pygame.draw.rect(screen,grey,(x_coord +15,y_coord,50,100))
                 pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
                 draw_black_keys()
            elif note == 'A' or note == 'C' or note == 'E' or note == 'F' or note == 'G' or note == 'C1':# fill in for black keys
                pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
                draw_black_keys()
            elif note == 'C_s' or note == 'D_s' or note == 'F_s' or note == 'G_s' or note == 'A_s':
                pygame.draw.rect(screen,black,(x_coord,y_coord,35,100))
            play_file_name = note + '.wav'
       
        if len(prevNote) > 0:
            print('hello')
            prev_x = key_dict[prevNote][0]
            prev_y = key_dict[prevNote][1]
        
            if prevNote == 'D':
                pygame.draw.rect(screen,white,(prev_x,prev_y,35,100)) 
                pygame.draw.rect(screen,white,(prev_x,prev_y +100,50,75)) # This is to create the white key underneath the black to keep it's piano shape. 
                draw_black_keys()
            elif prevNote == 'A' or prevNote == 'C' or prevNote == 'E' or prevNote == 'F' or prevNote == 'G' or prevNote == 'C1':
                pygame.draw.rect(screen,white,(prev_x,prev_y,50,175))
                draw_black_keys()
            elif prevNote == 'B':
                 pygame.draw.rect(screen,white,(x_coord +15,y_coord,50,100))
                 pygame.draw.rect(screen,white,(x_coord,y_coord +100,50,75))
                 draw_black_keys()
            elif prevNote == 'C_s' or prevNote == 'D_s' or prevNote == 'F_s' or prevNote == 'G_s' or prevNote == 'A_s':
                pygame.draw.rect(screen,black,(x_coord,y_coord,35,100))
        prevNote = note
            
           
        
        pygame.display.update()
        playsound(play_file_name)
   
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

    piano_gui()
    pygame.display.update()
    auto_play()
   

    # timer (1 sec)
    
    

