import matplotlib.pyplot as plt


def plot(iterations):
    """Make a plot of the evolvement of the score."""
    
    scores = [1234, 1345, 1345, 1456, 1456, 1678, 1678, 1678]
    # initialize figure
    fig, ax = plt.subplots(figsize=(5,6))
    ax.set_title('Evolvement of score')
    ax.set_ylabel('Score')
    ax.set_xlabel('Iteration')
    
    x = []
    y = []

    # put runs on the x-axis
    for iteration in range(iterations):
        x.append(iteration)

    # put score on the y-axis
    for score in scores:
        y.append(score)
    
    ax.plot(x, y, zorder=1)

    # show the plots
    plt.show()

    plt.savefig("plot.jpeg", format="jpeg", dpi=250)