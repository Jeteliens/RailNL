import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.ticker as plticker
import csv


def plot(iterations, scores_data):
    """Make a plot of the evolvement of the score."""
    
    # scores = [1234, 1345, 1345, 1456, 1456, 1678, 1678, 1678]
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
    
    # plt.yticks(np.arange(0, 9500+1, 500))
    loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    loc = plticker.MultipleLocator(base=500) # this locator puts ticks at regular intervals
    ax.yaxis.set_major_locator(loc)
    ax.plot(x, y)

    ax.set(xlabel='Iteration', ylabel='Score', 
        title='Evolvement of score')

    # plt.axis([0, iterations, 0, 9500])
    # plt.xlim([0, iterations])
    # ax.set_xlim([0, iterations])
    # ax.set_ylim([0, 9500])
    # plt.xticks(4, [100,200,300,400])
    # plt.xticks(np.arange(0, iterations+1, 100))
    # plt.yticks(np.arange(5000, 9500, 500))
    
    # start, end = ax.get_xlim()
    # ax.xaxis.set_ticks(np.arange(start, end+1, 100))
    
    # locator = plticker.MultipleLocator(base=500) # this locator puts ticks at regular intervals
    # ax.yaxis.set_major_locator(locator)

    # show the plots
    plt.show()

    plt.savefig("results/plot.jpeg", format="jpeg", dpi=250)

     # put runs on the x-axis
    # for iteration in range(iterations):
    #     x.append(iteration)

    # # put score on the y-axis
    # for score in scores:
    #     y.append(score)