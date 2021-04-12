#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:17:03 2021

@author: laurelmyers
"""

#-------------------CODE FROM OUTSIDE SOURCE: NISHU JAIN (START)---------------------------------

# import numpy as np

# samplerate = 44100 #Frequecy in Hz

# def get_wave(freq, duration=0.75):
#     '''
#     Function takes the "frequecy" and "time_duration" for a wave 
#     as the input and returns a "numpy array" of values at all points 
#     in time
#     '''
    
#     amplitude = 4096
#     t = np.linspace(0, duration, int(samplerate * duration))
#     wave = amplitude * np.sin(2 * np.pi * freq * t)
    
#     return wave

# # To get a 1 second long wave of frequency 440Hz
# a_wave = get_wave(440, 1)

# #wave features
# print(len(a_wave)) # 44100
# print(np.max(a_wave)) # 4096
# print(np.min(a_wave)) # -4096

# from pprint import pprint

# def get_piano_notes():
#     '''
#     Returns a dict object for all the piano 
#     note's frequencies
#     '''
#     # White keys are in Uppercase and black keys (sharps) are in lowercase
#     octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
#     base_freq = 261.63 #Frequency of Note C4
    
#     note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
#     note_freqs[''] = 0.0 # silent note
    
#     return note_freqs
  
#   # To get the piano note's frequencies
# note_freqs = get_piano_notes()
# pprint(note_freqs)
# '''
#            {'': 0.0,
#            'A': 440.00745824565865,
#            'B': 493.8916728538229,
#            'C': 261.63,
#            'D': 293.66974569918125,
#            'E': 329.63314428399565,
#            'F': 349.2341510465061,
#            'G': 392.0020805232462,
#            'a': 466.1716632541139,
#            'c': 277.18732937722245,
#            'd': 311.1322574981619,
#            'f': 370.00069432367286,
#            'g': 415.31173722644}
#  '''
# import numpy as np

# def get_song_data(music_notes):
#     '''
#     Function to concatenate all the waves (notes)
#     '''
#     note_freqs = get_piano_notes() # Function that we made earlier
#     song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
#     song = np.concatenate(song)
#     return song

# music_notes = 'C-C-g-a-B'
# data = get_song_data(music_notes)

# data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
# from scipy.io.wavfile import write
# write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))

#-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C
#-----------------------CODE FROM OUSTIDE SOURCE: NISHU JAIN (END)------------------------------


#packages needed:
   
    
   # numpy (should come pre-loaded), pygame, sys

import numpy as np

samplerate = 44100 #Frequecy in Hz

def get_wave(freq, duration=0.75):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

# To get a 1 second long wave of frequency 440Hz
a_wave = get_wave(440, 1)

#wave features
print(len(a_wave)) # 44100
print(np.max(a_wave)) # 4096
print(np.min(a_wave)) # -4096

from pprint import pprint

def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    all_notes = ['A3', 'asharp3', 'B3','C4', 'csharp4', 'D4', 'dsharp4', 'E4', 'F4', 'fsharp4', 'G4', 'gsharp4', 'A4', 'asharp4', 'B4','csharp5','C5'] 
    base_freq = 220.00 #Frequency of Note A3, the A before middle C
    
    note_freqs = {all_notes[i]: base_freq * pow(2,(i/12)) for i in range(len(all_notes))}        
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs
  
  # To get the piano note's frequencies
note_freqs = get_piano_notes()
pprint(note_freqs)

 
import numpy as np

def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    '''
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

music_notes = 'C4-C4-gsharp4-asharp3-B3' 
data = get_song_data(music_notes)

data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
from scipy.io.wavfile import write
write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))
#convert notes from dictionary entries to wave files:


A3 = get_wave(note_freqs['A3'])
asharp3 = get_wave(note_freqs['asharp3'])
B3 = get_wave(note_freqs['B3'])
C4 = get_wave(note_freqs['C4'])
csharp4 = get_wave(note_freqs['csharp4'])
D4 = get_wave(note_freqs['D4'])
dsharp4 = get_wave(note_freqs['dsharp4'])
E4 = get_wave(note_freqs['E4'])
F4 = get_wave(note_freqs['F4'])
fsharp4 = get_wave(note_freqs['fsharp4'])
G4 = get_wave(note_freqs['G4'])
gsharp4 = get_wave(note_freqs['gsharp4'])
A4 = get_wave(note_freqs['A4'])
asharp4 = get_wave(note_freqs['asharp4'])
B4 = get_wave(note_freqs['B4'])
csharp5 = get_wave(note_freqs['csharp5'])
C5 = get_wave(note_freqs['C5'])

# #create separate wave file for each note:
write('A3.wav', samplerate, A3.astype(np.int16))
write('asharp3.wav', samplerate, asharp3.astype(np.int16))
write('B3.wav', samplerate, B3.astype(np.int16))
write('C4.wav', samplerate, C4.astype(np.int16))
write('csharp4.wav', samplerate, csharp4.astype(np.int16))
write('D4.wav', samplerate, D4.astype(np.int16))
write('dsharp4.wav', samplerate, dsharp4.astype(np.int16))
write('E4.wav', samplerate, E4.astype(np.int16))
write('F4.wav', samplerate, F4.astype(np.int16))
write('fsharp4.wav', samplerate, fsharp4.astype(np.int16))
write('G4.wav', samplerate, G4.astype(np.int16))
write('gsharp4.wav', samplerate, gsharp4.astype(np.int16))
write('A4.wav', samplerate, A4.astype(np.int16))
write('asharp4.wav', samplerate, asharp4.astype(np.int16))
write('B4.wav', samplerate, B4.astype(np.int16))
write('csharp5.wav', samplerate, csharp5.astype(np.int16))
write('C5.wav', samplerate, C5.astype(np.int16))

import pygame, sys
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width, screen_height])
mixer.init()
#create playable variables for each note (compatible with pygame):
A3_note = pygame.mixer.Sound("A3.wav")
a3sharp_note = pygame.mixer.Sound("asharp3.wav")
B3_note = pygame.mixer.Sound("B3.wav")
C4_note = pygame.mixer.Sound("C4.wav")
c4sharp_note = pygame.mixer.Sound("csharp4.wav")
D4_note = pygame.mixer.Sound("D4.wav")
d4sharp_note = pygame.mixer.Sound("dsharp4.wav")
E4_note = pygame.mixer.Sound("E4.wav")
F4_note = pygame.mixer.Sound("F4.wav")
f4sharp_note = pygame.mixer.Sound("fsharp4.wav")
G4_note = pygame.mixer.Sound("G4.wav")
g4sharp_note = pygame.mixer.Sound("gsharp4.wav")
A4_note = pygame.mixer.Sound("A4.wav")
a4sharp_note = pygame.mixer.Sound("asharp4.wav")
B4_note = pygame.mixer.Sound("B4.wav")
c5sharp_note = pygame.mixer.Sound("csharp5.wav")
C5_note = pygame.mixer.Sound("C5.wav")




mixer.music.set_volume(0.7)
black = (0,0,0)
while True:
    screen.fill(black)
    pygame.display.flip()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.KEYDOWN: #when a specified key is pressed and held down, a note plays
            if event.key == pygame.K_a:
                  A3_note.play(-1)
            if event.key == pygame.K_s:
                  B3_note.play(-1)      
            if event.key == pygame.K_d:
                  C4_note.play(-1) #(-1)plays the sound infinitely! Perfect for continuous synth
            if event.key == pygame.K_f:
                  D4_note.play(-1)
            if event.key == pygame.K_g:
                  E4_note.play(-1)
            if event.key == pygame.K_h:
                  F4_note.play(-1)
            if event.key == pygame.K_j:
                  G4_note.play(-1)
            if event.key == pygame.K_k:
                  A4_note.play(-1)
            if event.key == pygame.K_l:
                  B4_note.play(-1)
            if event.key == pygame.K_SEMICOLON:
                  C5_note.play(-1)
            if event.key == pygame.K_w:
                  a3sharp_note.play(-1)
            if event.key == pygame.K_r:
                  c4sharp_note.play(-1)
            if event.key == pygame.K_t:
                  d4sharp_note.play(-1)
            if event.key == pygame.K_u:
                  f4sharp_note.play(-1)
            if event.key == pygame.K_i:
                  g4sharp_note.play(-1)
            if event.key == pygame.K_o:
                  a4sharp_note.play(-1)
            if event.key == pygame.K_p:
                  c5sharp_note.play(-1)
           
                  
                  
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                  A3_note.stop()
            if event.key == pygame.K_s:
                  B3_note.stop()
            if event.key == pygame.K_d: #when 1 is released, the music stops
                  C4_note.stop()
            if event.key == pygame.K_f:
                  D4_note.stop()
            if event.key == pygame.K_g:
                  E4_note.stop()
            if event.key == pygame.K_h:
                  F4_note.stop()
            if event.key == pygame.K_j:
                  G4_note.stop()
            if event.key == pygame.K_k:
                  A4_note.stop()
            if event.key == pygame.K_l:
                  B4_note.stop()
            if event.key == pygame.K_SEMICOLON:
                  C5_note.stop()
            if event.key == pygame.K_w:
                  a3sharp_note.stop()
            if event.key == pygame.K_r:
                  c4sharp_note.stop()
            if event.key == pygame.K_t:
                  d4sharp_note.stop()
            if event.key == pygame.K_u:
                  f4sharp_note.stop()
            if event.key == pygame.K_i:
                  g4sharp_note.stop()
            if event.key == pygame.K_o:
                  a4sharp_note.stop()
            if event.key == pygame.K_p:
                  c5sharp_note.stop()
                  
# Visualizing the keyboard
#
# Demonstrates how to build a simple piano instrument playable
# through the computer keyboard.
#
 
from music import *
from gui import *
 
Play.setInstrument(PIANO)   # set desired MIDI instrument (0-127)
 
# load piano image and create display with appropriate size
pianoIcon = Icon("pianooctave.jpeg")     # image for complete piano
d = Display("iPiano", pianoIcon.getWidth(), pianoIcon.getHeight())
d.add(pianoIcon)       # place image at top-left corner
 
# NOTE: The following loads a partial list of icons for pressed piano
#       keys, and associates them (via parallel lists) with the
# virtual keys corresponding to those piano keys and the corresponding
# pitches.  These lists should be expanded to cover the whole octave
# (or more).
 
# load icons for pressed piano keys
# (continue loading icons for additional piano keys)
downKeyIcons = []    # holds all down piano-key icons
downKeyIcons.append( Icon("pianowhiteleftdown.jpeg") )   # C
downKeyIcons.append( Icon("pianoblackleftdown.jpeg") )       # C sharp
downKeyIcons.append( Icon("pianoDdown.jpeg") ) # D
downKeyIcons.append( Icon("pianodsharpdown.jpeg") )       # D sharp
downKeyIcons.append( Icon("pianoEdown.jpeg") )  # E
downKeyIcons.append( Icon("pianoFdown.jpeg") )   # F
 
# lists of virtual keys and pitches corresponding to above piano keys
virtualKeys = [VK_Z, VK_S, VK_X, VK_D, VK_C, VK_V]
pitches     = [C4,   CS4,  D4,   DS4,  E4,   F4]
 
# create list of display positions for downKey icons
#
# NOTE:  This as hardcoded - they depend on the used images!
#
iconLeftXCoordinates = [0, 45, 76, 138, 150, 223]
 
keysPressed = []   # holds which keys are currently pressed
 
#####################################################################
# define callback functions
def beginNote( key ):
   """Called when a computer key is pressed.  Implements the
      corresponding piano key press (i.e., adds key-down icon on
      display, and starts note).  Also, counteracts the key-repeat
      function of computer keyboards.
   """
 
   # loop through all known virtual keys
   for ii in range( len(virtualKeys) ):   
 
      # if this is a known key (and NOT already pressed)
      if key == virtualKeys[ii] and key not in keysPressed:  
 
         # "press" this piano key (by adding pressed key icon)
         d.add( downKeyIcons[ii], iconLeftXCoordinates[i], 0 )
         Play.noteOn( pitches[ii] )    # play corresponding note
         keysPressed.append( key )    # avoid key-repeat
 
def endNote( key ):
   """Called when a computer key is released.  Implements the
      corresponding piano key release (i.e., removes key-down icon,
      and stops note).
   """
 
   # loop through known virtual keys
   for ii in range( len(virtualKeys) ):   
 
      # if this is a known key (we can assume it is already pressed)
      if key == virtualKeys[ii]:  
 
         # "release" this piano key (by removing pressed key icon)
         d.remove( downKeyIcons[ii] )
         Play.noteOff( pitches[ii] )    # stop corresponding note
         keysPressed.remove( key )     # and forget key
 
#####################################################################
# associate callback functions with GUI events
d.onKeyDown( beginNote )
d.onKeyUp( endNote )
