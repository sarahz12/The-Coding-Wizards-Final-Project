# import simpleaudio as sa

# filename = 'myfile.wav'
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done()  # Wait until sound has finished playing
########### code from outside source (START) #############
## this is meant to show how to mix several voices into one single-channel output
# iPianoParallel.py
#
# Demonstrates how to build a simple piano instrument playable
# through the computer keyboard.
#
 
import wave

w1 = wave.open("/Users/sarahzylberfuden/Desktop/clps950final/The-Coding-Wizards-Final-Project/A3.wav")
w2 = wave.open("/Users/sarahzylberfuden/Desktop/clps950final/The-Coding-Wizards-Final-Project/C4.wav")

#get samples formatted as a string.
samples1 = w1.readframes(w1.getnframes())
samples2 = w2.readframes(w2.getnframes())

#takes every 2 bytes and groups them together as 1 sample. ("123456" -> ["12", "34", "56"])
samples1 = [samples1[i:i+2] for i in range(0, len(samples1), 2)]
samples2 = [samples2[i:i+2] for i in range(0, len(samples2), 2)]

#convert samples from strings to ints
def bin_to_int(bin):
    as_int = 0
    for char in bin[::-1]: #iterate over each char in reverse (because little-endian)
        #get the integer value of char and assign to the lowest byte of as_int, shifting the rest up
        as_int <<= 8
        as_int += char
    return as_int

samples1 = [bin_to_int(s) for s in samples1] #['\x04\x08'] -> [0x0804]
samples2 = [bin_to_int(s) for s in samples2]

#average the samples:
samples_avg = [(s1+s2)//2 for (s1, s2) in zip(samples1, samples2)]



# import struct
# import math
# import pyaudio
# from itertools import count

# pa = pyaudio.PyAudio()

# FORMAT = pyaudio.paFloat32
# CHANNELS = 1
# RATE = 44100

# OUTPUT_BLOCK_TIME = 0.05
# OUTPUT_FRAMES_PER_BLOCK = int(RATE*OUTPUT_BLOCK_TIME)


# def sine_gen():
#     time = 0
#     format = "%df" % OUTPUT_FRAMES_PER_BLOCK
#     song = []
#     song.append(lambda sampletime: math.sin(sampletime * math.pi * 2 * 440.0))

#     for frame in count():
#         block = []
#         for i in xrange(OUTPUT_FRAMES_PER_BLOCK):
#             sampletime = time + (float(i) / OUTPUT_FRAMES_PER_BLOCK) * OUTPUT_BLOCK_TIME
#             sample = sum(song(sampletime) for song in song) / len(song)
#             block.append(sample)
#         yield struct.pack(format, *block)
#         time += OUTPUT_BLOCK_TIME
#         if frame == 20:
#             song.append(
#                 lambda sampletime: math.sin(sampletime * math.pi * 2 * 880.0)
#             )

# stream = pa.open(format=FORMAT,
#     channels=CHANNELS, rate=RATE, output=1)

# for i, block in enumerate(sine_gen()):
#     stream.write(block)
# Visualizing the keyboard
#
# Demonstrates how to build a simple piano instrument playable
# through the computer keyboard.
#
 
from music import *
from gui import *
 
Play.setInstrument(PIANO)   # set desired MIDI instrument (0-127)
 
# load piano image and create display with appropriate size
pianoIcon = Icon("iPianoOctave.png")     # image for complete piano
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
downKeyIcons.append( Icon("iPianoWhiteLeftDown.png") )   # C
downKeyIcons.append( Icon("iPianoBlackDown.png") )       # C sharp
downKeyIcons.append( Icon("iPianoWhiteCenterDown.png") ) # D
downKeyIcons.append( Icon("iPianoBlackDown.png") )       # D sharp
downKeyIcons.append( Icon("iPianoWhiteRightDown.png") )  # E
downKeyIcons.append( Icon("iPianoWhiteLeftDown.png") )   # F
 
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
   for i in range( len(virtualKeys) ):   
 
      # if this is a known key (we can assume it is already pressed)
      if key == virtualKeys[i]:  
 
         # "release" this piano key (by removing pressed key icon)
         d.remove( downKeyIcons[i] )
         Play.noteOff( pitches[i] )    # stop corresponding note
         keysPressed.remove( key )     # and forget key
 
#####################################################################
# associate callback functions with GUI events
d.onKeyDown( beginNote )
d.onKeyUp( endNote )



