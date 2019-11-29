# -*- coding: utf-8 -*-
"""RL_gridworld.ipynb
Author: Diganta Kalita (digankate26@gmail.com)
"""

import numpy as np

grid = np.zeros((5,5))
grid

Y = .90  #discount value
for num in range(10): #number of times we will go through the whole grid
  for i in range(5):      #all the rows
    for j in range(5):    #all the columns
      
      up_grid = grid[i-1][j] if i > 0 else None   #if going up takes us out of the grid then its value be 0
      down_grid = grid[i+1][j] if i < 4 else None  #if going down takes us out of the grid then its value be 0
      left_grid = grid[i][j-1] if j > 0 else None  #if going left takes us out of the grid then its value be 0
      right_grid = grid[i][j+1] if j < 4 else None  #if going right takes us out of the grid then its value be 0

      all_dirs = [up_grid, down_grid, left_grid, right_grid]     

      value=0  
      if i==0 and j==1: # the position of A
        value = 10 + Y*grid[4][1]
      elif i==0 and j==3: # the position of B
        value = 5 + Y*grid[2][3]
      else:
        for direc in all_dirs:
          if direc != None: 
            value += .25 * (0 + Y*direc)  #if we don't go out of the grid
          else:
            value += .25 * (-1 + Y*grid[i][j]) #if we go out of the grid
        
      grid[i][j] = value

np.round(grid, 1)

