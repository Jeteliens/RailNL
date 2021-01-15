import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualise():
    df = pd.read_csv(r"StationsHolland.csv")
    map = plt.imread(r"nederland.png")

    print(df.head())

    fig, ax = plt.subplots(figsize=(8,9))

    print(df.head(2))

    ax.set_title('Trajectories')

    BBox = (3.395, 7.273, 53.593, 50.716)

    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])

    ax.scatter(5, 52, c='b', s=10)
    # ax.scatter(5, 52, )

    ax.imshow(map, zorder=0, extent = BBox, aspect= 'equal')
    plt.show()

if __name__ == '__main__':
    
    visualise()

