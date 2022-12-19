# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:45:52 2022

@author: mip22dmc
"""

import random
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import matplotlib.animation 
import Drunks_Framework
import csv
import numpy as np

# Defines the number of drunks and iterations and creates an empty coordinates
# list for drunks.  
num_of_drunks = 25
num_of_iterations = 10000
drunks = []

# Opens in.txt file and reads the csv into the environment list 
with open('drunk.plan', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = [] 
        for value in row:
            rowlist.append(value)
            #print(value) 
        environment.append(rowlist)

# Creates lists of x- and y-coordinates
array = np.array(environment)
index = np.argwhere(array == 1)
#print(index)
index2 = index.tolist()
pubrows = list(zip(*index2))[0]
pubcols = list(zip(*index2))[1]

# Creates the animation        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, \
frames=gen_function, repeat=False)
    canvas.draw()         

# For animation.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# For GUI
root = tkinter.Tk()
root.wm_title("Drunks Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run) 

# Make the drunks.
for i in range(num_of_drunks):
    y = random.choice(pubrows)
    x = random.choice(pubcols)
    print(x, y)
    drunks.append(Drunks_Framework.Drunk(environment, drunks, y, x))

# For stopping function.
carry_on = True

# Drunks move, eat, share, drop, and print location and store information.
# Drunks are shuffled into a random order before each iteration of events.    
def update(frame_number):
    
    fig.clear()   
    global carry_on 
    
    for i in range(num_of_drunks):
        
        drunks[i].move(i)
        drunks[i].path()
        drunks[i].__str__()

    # Stoppng Conditon - All Drunks Pints values == 0
    count = 0
    for i in range(num_of_drunks):
        if drunks[i].pints == 0:
            count = count + 1
    if count == len(drunks):
        print ("Stopping Condition", frame_number + 1)
        carry_on = False
    
# Plot the drunks in the environment.   
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_drunks):
        matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)
        print(drunks[i].x,drunks[i].y, "drunk")
        plt.text(drunks[i].x,drunks[i].y, "drunk")
    #matplotlib.pyplot.show()
    canvas.draw()
    
# For generating stopping condition.
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a >= 0) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# Write out the environment as new file.
updatedenv = open('updateddrunkenv.csv', 'w', newline='')
writer = csv.writer(updatedenv, delimiter=' ')
for row in environment:
    writer.writerow(row)
updatedenv.close()

tkinter.mainloop() 