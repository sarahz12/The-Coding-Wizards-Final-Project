#-------------------CODE FROM OUTSIDE SOURCE: NISHU JAIN (START)---------------------------------

import numpy as np

samplerate = 44100 #Frequecy in Hz

def get_wave(freq, duration=0.5):
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
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs
  
  # To get the piano note's frequencies
note_freqs = get_piano_notes()
pprint(note_freqs)
'''
           {'': 0.0,
           'A': 440.00745824565865,
           'B': 493.8916728538229,
           'C': 261.63,
           'D': 293.66974569918125,
           'E': 329.63314428399565,
           'F': 349.2341510465061,
           'G': 392.0020805232462,
           'a': 466.1716632541139,
           'c': 277.18732937722245,
           'd': 311.1322574981619,
           'f': 370.00069432367286,
           'g': 415.31173722644}
 '''
# package needed for project
import numpy as np

def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    '''
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
data = get_song_data(music_notes)

data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
from scipy.io.wavfile import write
write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))
#-----------------------CODE FROM OUSTIDE SOURCE: NISHU JAIN (END)------------------------------

#REMEMBER: Press and release: the note should continue to play until key is released
#create a way to "record" the notes played:


#MAIN GOALS FOR THIS SECTION:
#create keypress events, where hitting "G" plays middle c, for example, 
#but when key is released, the sound stops (amp == 0)

#create a way to record key pressed with the touch of a button: in this case, hit "shift"
#to record




#pip (in terminal)
#pip install pygame(in terminal)


import pygame, os, sys
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
background_colour = (255,255,255)
(width, height) = (400, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Piano')
screen.fill(background_colour)
pygame.display.flip()
running = True

# while loop
while running:
    event = pygame.event.wait ()
    if event.type == pygame.QUIT:
        running = False  
        pygame.quit ()

# import mixer for loading and playing sounds   
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)
mixer.init()
mixer.music.load("twinkle-twinkle.wav")
mixer.music.set_volume(0.7)
for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            pygame.mixer.music.play(0)
     if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            pygame.mixer.music.stop()
        pygame.event.pump()

 

#if key is released, amplitude should equal 0!
#---this plays the note once
    
#if event.type == pygame.KEYUP
    #pygame.mixer.music.stop() # - This will stop the music.
    
    #pygame.mixer.set_num_channels() will be useful for multiple notes


