import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text
import random


def visualise(map):
    # x = [4.7, 4.7, 4.9, 4.9]
    # y = [52.1, 52.6, 52.3, 52.4]
    # n = ['Alphen a/d Rijn', 'Alkmaar', 'Amsterdam Amstel', 'Amsterdam Centraal']

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'yellow', 'orange', 'pink', 'lawngreen', 'silver', 'saddlebrown']
    used_colors = []

    background = plt.imread(r"code/visualisation/nederlandgroot.png")

    # initialize figure
    fig, ax = plt.subplots(figsize=(10,9))
    ax = plt.axes(frameon=False)
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)

    # set boundries for image
    BBox = (3.362, 7.234, 50.786, 53.557)
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
        
    # make new lists for every trajectory
    for train in map.trains:
        train = train['stations']
        x = []
        y = []
        # draw lines between the stations for each trajectory
        for station in train:
            x.append(station.x_position)
            y.append(station.y_position)
            
            color = random.choice(colors)
            if color in used_colors:
                color = random.choice(colors)
            else:
                used_colors.append(color)
            
            ax.plot(y, x, c=color)

    x_positions = []
    y_positions = []
    names = []

    # list all the stations that are ridden in the trajectory
    for station in map.ridden_stations:
        x_positions.append(station.x_position)
        y_positions.append(station.y_position)
        names.append(station.name)
    
    # place a point for each ridden station
    ax.scatter(y_positions, x_positions, c='k', marker=("."))
    
    texts = []
    for x, y, s in zip(y_positions, x_positions, names):
        texts+=[plt.text(x, y, s, fontsize=6)]

    # # write the names by each point
    # for i, txt in enumerate(names):
    #     plt.annotate(txt, (y_positions[i], x_positions[i]), size=4)

    adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.5), only_move={'points':'y', 'texts':'y'})

    # show the image
    ax.imshow(background, zorder=0, extent = BBox, aspect= 'equal')

    # show the plots
    plt.show()

    plt.savefig("trajectories.jpeg", format="jpeg")