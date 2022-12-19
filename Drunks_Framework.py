# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:35:03 2022

@author: mip22dmc
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022
@author: Dan Chaib
"""
import random

class Drunk():
    """
    Class used to provide functionality to drunks interacting
    with environment, as well as protecting x and y coordinate values.
    """
    def __init__(self, environment, drunks, y = None, x = None):
        """
        Used to initialise drunks into the environment.
        
        Parameters
        ----------
        environment : List
            A list of integer values used to form an environment.
        drunks : List
            A list of all 'drunks'.
        y : Number (Integer)
            y-coordinate of each drunk. The default is None.
        x : Number (Integer)
            y-coordinate of each drunk. The default is None.
        Returns
        -------
        None.
        """
        if y == None:
            self._y = random.randint(1,300) 
        else:
            self._y = y
        if x == None:
            self._x = random.randint(1,300) 
        else:
            self._x = x
        self.environment = environment
        self.drunks = []
        self.pints = random.randint(1, 10)
        
# Functions to set and get x and y values.
    def setx(self, value):
        """
        Sets x attribute value.
        Parameters
        ----------
        value : Number (Integer)
        Returns
        -------
        None.
        """
        self._x = value
        
    def sety(self, value):
        """
        Sets y attribute value.
        Parameters
        ----------
        value : Number (Integer)
        Returns
        -------
        None.
        """
        self._y = value      
    
    def getx(self):
        """
        Retrieves x attribute value.
        Returns
        -------
        Number (Float)
            self._x
        
        """
        return self._x
    
    def gety(self):
        """
        Retrieves x attribute value.
        Returns
        -------
        Number (Float)    
            self._y
        """
        return self._y

# Function moving drunks, if store is greater drunk moves fewer spaces (more \
# drunk).
# In addition, random number condition dictating direction and length of \
# travel.
# Finally, a condition has been added where if a drunk is within a certain \
# number of spaces of the boundary of the 300x300 environment, they will move \
# back towards to middle of the axis of the environment for which they are \
# close to the boundary limit.
    def move(self, i):
        """
        Function which moves drunks by changing their x and y-
        coordinates.
        Returns
        -------
        None.
        """        
        if self.environment[self.y][self.x] == (i+1)*10:
            self._x == self.x
            self._y == self.y
            self.pints = 0
            print("Drunk" ,i+1, "is home")
        
        else:
        
            if self.pints > 5:
                if self._x in range (6, 296):
                    if random.random() < 0.5:
                        self._x = (self._x + 5)
                    else:
                        self._x = (self._x - 5)
                if self._x in range (1, 6):
                    self._x = (self._x + 5)
                if self._x in range (296, 301):
                    self._x = (self._x - 5)
        
                if self._y in range (6, 296):
                    if random.random() < 0.5:
                        self._y = (self._y + 5)
                    else:
                        self._y = (self._y - 5)
                if self._y in range (1, 6):
                    self._y = (self._y + 5)
                if self._y in range (296, 301):
                    self._y = (self._y - 5)
        
            if self.pints <= 5:
                if self._x in range (11, 291):
                    if random.random() < 0.5:
                        self._x = (self._x + 10)
                    else:
                        self._x = (self._x - 10)
                if self._x in range (1, 11):
                    self._x = (self._x + 10)
                if self._x in range (291, 301):
                    self._x = (self._x - 10)
        
                if self._y in range (11, 291):
                    if random.random() < 0.5:
                        self._y = (self._y + 10)
                    else:
                        self._y = (self._y - 10)
                if self._y in range (1, 11):
                    self._y = (self._y + 10)
                if self._y in range (291, 301):
                    self._y = (self._y - 10)
            
# Per step a drunk takes, the environment reduces value by 1, creating a path.
# This happens at the pub only in the areas of the map not taken up by houses \
# or the pub:. 
    def path(self):
        """
        Function allowing for 'drunks' to leave their paths in the environment.
        Returns
        -------
        None.
        """
        if self.environment[self.y][self.x] <= 0:
            self.environment[self.y][self.x] -= 10
        
# When printed each drunk for each iteration, gives drunks coordinates and \
# store.
    def __str__(self):
        """
        Gives the y-coordinate, x-coordinate and store values of 'drunks'.
        Returns
        -------
        None.
        """
        print(self._y, self._x, self.pints)

# Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.")