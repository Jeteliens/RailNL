import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.ticker as plticker
import csv


def plot(scores_data):
    """Make a plot of the evolvement of the score."""
    
    # initialize figure
    fig, ax = plt.subplots()

    x = []
    y = []

    with open(scores_data, 'r') as in_file:
        reader = csv.DictReader(in_file)
        
        # add the positions of the stations
        for row in reader:
            x.append(int(row['iteration']))
            y.append(math.floor(float(row['score'])))
    
    # loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
    # ax.xaxis.set_major_locator(loc)
    # loc = plticker.MultipleLocator(base=500) # this locator puts ticks at regular intervals
    # ax.yaxis.set_major_locator(loc)

    ax.plot(x, y)

    ax.set(xlabel='Iteration', ylabel='Score', 
        title='Evolvement of score')

    # show the plots
    plt.show()

    plt.savefig("results/plot.jpeg", format="jpeg", dpi=250)


if __name__ == '__main__':
    scores_data = "scores_data.csv"

    plot(scores_data)