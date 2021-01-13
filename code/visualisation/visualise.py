import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualise(train):
    # x = [4.7, 4.7, 4.9, 4.9]
    # y = [52.1, 52.6, 52.3, 52.4]
    # n = ['Alphen a/d Rijn', 'Alkmaar', 'Amsterdam Amstel', 'Amsterdam Centraal']

    x = []
    y = []
    n = train

    for station in train:
        x.append(station.x_position)
        y.append(station.y_position)

    df = pd.read_csv(r"data/Holland/StationsHolland.csv")
    map = plt.imread(r"code/visualisation/nederland.png")

    print(df.head())

    fig, ax = plt.subplots(figsize=(7,9))

    ax.set_title('Trajectories')

    BBox = (3.395, 7.273, 50.716, 53.593)
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])

    ax.plot(y, x, c='b', marker=("."))

    for i, txt in enumerate(n):
        plt.annotate(txt, (y[i], x[i]), size=6)

    ax.imshow(map, zorder=0, extent = BBox, aspect= 'equal')
    plt.show()
    plt.savefig("trajectories.jpeg", format="jpeg")
