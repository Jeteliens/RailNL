import matplotlib.pyplot as plt


def hillplot(run_freq):
    """Make a plot of the evolvement of the score for HillClimber."""
    
    scores = [1234, 1345, 1345, 1456, 1456, 1678, 1678, 1678]
    # initialize figure
    fig, ax = plt.subplots(figsize=(5,6))
    ax.set_title('Evolvement HillClimber')
    ax.set_ylabel('Score')
    ax.set_xlabel('Run')
    
    x = []
    y = []

    # put runs on the x-axis
    for run in range(run_freq):
        x.append(run)

    # put score on the y-axis
    for score in scores:
        y.append(score)
    
    ax.plot(x, y, zorder=1)

    # show the plots
    plt.show()

    plt.savefig("hillplot.jpeg", format="jpeg", dpi=250)


def simplot(run_freq):
    """Make a plot of the evolvement of the score for Simulated Annealing."""
    
    scores = [1234, 1345, 1245, 1476, 1576, 1430, 1678, 1678]
    # initialize figure
    fig, ax = plt.subplots(figsize=(5,6))
    ax.set_title('Evolvement Simulated Annealing')
    ax.set_ylabel('Score')
    ax.set_xlabel('Run')

    x = []
    y = []

    # put runs on the x-axis
    for run in range(run_freq):
        x.append(run)

    # put score on the y-axis
    for score in scores:
        y.append(score)
    
    ax.plot(x, y, zorder=1)

    # show the plots
    plt.show()

    plt.savefig("simplot.jpeg", format="jpeg", dpi=250)