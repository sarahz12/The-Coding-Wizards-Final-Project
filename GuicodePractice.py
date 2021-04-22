from tkinter import*
import time;
import datetime
import pygame

pygame.init()
root = Tk()
root.title('Music Box')
root.geometry('1352x700+0+0')
root.configure(background = 'white')

ABC1 = Frame(root, bg = 'powder blue', bd = 20, relief = RIDGE)
ABC1.grid()
ABC2 = Frame(root, bg = 'powder blue', bd = 20, relief = RIDGE)
ABC3.grid()
ABC = Frame(root, bg = 'powder blue', bd = 20, relief = RIDGE)
ABC3.grid()

Str1 = StringVar()
str.set('Just Like Music')
Date1 = StringVar()
Time1 = StringVar()

strl.set('C#')
sound=pygame.mixer.Sound



















Label(ABC1, text = 'Piano Musical Keys', font = ('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg = 'powder blue',
fg = 'white', justify = CENTER).grid(row = 0, column=0, columnspan=11)

txtDisplay= Entry(ABC1, textvariable=Date1, font = ('arial', 18, 'bold'), bd=34, bg = 'powder blue', fg= 'white', width=28, justify=CENTER).grid(row=1, column=0, pady=1)

btnCs= Button(ABC2, height = 6, width =6, text='C#', font = ('arial', 18, 'bold'), bd =4, bg = 'black', fg= 'white')
btnCs.grid(row=0, column=0, padx=8, pady=5)

btnCs= Button(ABC2, height = 6, width =6, text='C#', font = ('arial', 18, 'bold'), bd =4, bg = 'black', fg= 'white')
btnCs.grid(row=0, column=2, padx=8, pady=5)

root.mainloop()
