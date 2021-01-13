import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from adjustText import adjust_text
import random

def visualise(map):
    # x = [4.7, 4.7, 4.9, 4.9]
    # y = [52.1, 52.6, 52.3, 52.4]
    # n = ['Alphen a/d Rijn', 'Alkmaar', 'Amsterdam Amstel', 'Amsterdam Centraal']

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'yellow', 'orange', 'pink', 'lawngreen', 'silver', 'saddlebrown']
    # df = pd.read_csv(r"data/Holland/StationsHolland.csv")
    background = plt.imread(r"code/visualisation/nederlandgroot.png")
    # print(df.head())

    fig, ax = plt.subplots(figsize=(10,9))

    ax.set_title('Trajectories')

    BBox = (3.362, 7.234, 50.786, 53.557)
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])

    print(map.trains)

    for train in map.trains:
        train = train['stations']
        x = []
        y = []

        for station in train:
            x.append(station.x_position)
            y.append(station.y_position)
            
            color = random.choice(colors)
            ax.plot(y, x, c=color)

    x_positions = []
    y_positions = []
    names = []

    print(map.stations)

    for station in map.stations:
        x_positions.append(station.x_position)
        y_positions.append(station.y_position)
        names.append(station.name)

    ax.scatter(y_positions, x_positions, c='k', marker=("."))
    for i, txt in enumerate(names):
        plt.annotate(txt, (y_positions[i], x_positions[i]), size=4)
        # adjust_text(n, only_move={'points':'y', 'texts':'y'}, arrowprops=dict(arrowstyle="->", color='r', lw=0.5))

        # n = train
        # , marker=(".")
        

    ax.imshow(background, zorder=0, extent = BBox, aspect= 'equal')
    plt.show()
    plt.savefig("trajectories.jpeg", format="jpeg")
