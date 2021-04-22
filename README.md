# The-Coding-Wizards-Final-Project
Michelle Liu, Laurel Myers, and Sarah Zylberfuden

Final CLPS 0950 Project

Creating a Musical Keyboard

Instructions: 
Download the code at https://github.com/sarahz12/The-Coding-Wizards-Final-Project.git
Toolboxes needed (some might already be installed depending on text editor used/what people already have): 

pygame

os 

sys

scipy

pprint

playsound

music

gui

numpy

write 

While there are a lot of practice files that anyone is free to view to see our progress, here are the primary files needed to see final results: 

PIANOCODEFORREAL.py: 

The code in this file generates notes of frequencies that correspond to notes on a piano using a modified sine wave. We applied the function get_piano_notes to this sine wave, which is edited from a previous code that we found (written by Nishu Jain). This gives us a series of notes starting from a base frequency, which we set as the frequency of A3. 
The pygame part of the code assigns each note to a key on the keyboard, and creates a sound from a keypress event. This makes a playable piano from your own keyboard and screen. The code instructs which keys play which notes. 

GUICODEFINAL.py:

This uses a code (written by Imram Khan) for a piano GUI for which the keys turn grey as you hover the mouse over them, and which plays a .wav file corresponding to a note on a piano when you click on a key with your mouse. The GUI is generated using pygame commands. We got rid of the stock .wav files and mapped the keys on this GUI to our own sine-based notes (using some of the code from PIANOCODEFORREAL.py). 

selfplayingpianoFINAL.py:

This code creates a self-playing piano, which currently plays “Twinkle Twinkle Little Star”  but which can be altered easily to play any number of songs (once translated into string inputs corresponding to the notes in our dictionary). This borrows somewhat from the code written by Imram Khan, but we drew the GUI in a completely different way: using equations from the original code, we did the math by hand to find the coordinates for each key, and initialized the GUI by creating a function piano_gui. We then used a for loop which overlays white or black keys with grey ones and then overlays another white or black key once the next note plays (in the case of the black keys, we overlay all the black keys with black rectangles after every iteration--details can be found in the code). The piano plays .wav files created from the altered sine wave generated in PIANOCODEFORREAL.py).


Ultimately, the code should generate a piano and a self-playing song.
