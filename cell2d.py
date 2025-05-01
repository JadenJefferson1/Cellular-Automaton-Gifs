# https://www.youtube.com/watch?v=wBxwPSMOWWc

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = r'C:/ffmpeg/bin/ffmpeg.exe'
Glidergun = np.loadtxt('gosbel.txt', delimiter=',').astype(np.int8)
plt.imshow(Glidergun, cmap='Greys')

def tick(matrix):
    new_state = np.copy(matrix)
    for i in range(np.size(matrix, 0) -1):
        for j in range(np.size(matrix, 1) -1):
            north = matrix[i][j-1] if j>0 else 0
            south = matrix[i][j+1] if j<(np.size(matrix, 1) -2) else 0
            west = matrix[i+1][j] if i<(np.size(matrix, 0) -2) else 0
            east = matrix[i-1][j] if i>0 else 0

            se = matrix[i+1][j+1] if i<(np.size(matrix, 0) -2) and j<(np.size(matrix,1) -2) else 0
            sw = matrix[i+1][j-1] if i<(np.size(matrix, 0) -2) and j>0 else 0
            ne = matrix[i-1][j+1] if i>0 and j<(np.size(matrix, 1) -2) else 0
            nw = matrix[i-1][j-1] if i>0 and j>0 else 0

            neighbors = np.sum([north,south,west,east,se,sw,ne,nw])
            
            #rules
            if matrix[i][j] == 0 and neighbors == 3:
                new_state[i][j] = 1
            elif matrix[i][j] == 1 and neighbors < 2:
                new_state[i][j] = 0
            elif matrix[i][j] == 1 and neighbors > 3:
                new_state[i][j] = 0
            elif matrix[i][j] == 1 and (neighbors == 3 or neighbors == 2): 
                new_state[i][j] = 1

    return new_state

anim = None 
def animateArtist(frames, inputinterval, matrix): 
    fig = plt.figure()

    ims = []
    for frame in range(frames):
        im = plt.imshow(matrix, animated=True, cmap='Greys')
        ims.append([im])
        matrix = tick(matrix)
    plt.close

    anim = animation.ArtistAnimation(fig, ims, interval=inputinterval, blit=True)
    anim.save('gameoflife.gif', writer = 'ffmpeg', fps = 30) 

animateArtist(400, 50,Glidergun)