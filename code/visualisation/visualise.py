import matplotlib.pyplot as plt

def visualise(map):

    positions = [station for station in map.stations.values()]
    name = [station.name for station in positions]
    color = [station.get_value().colour.get_web() if station is not None else "grey"
              for station in positions]


    for station in test_map.stations:
        station.add_directions(connections_file)

        x = test_map.stations.x_position
        y = test_map.stations.y_position

    fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)

    axs[1, 0].scatter(x, y, s=80, c=z, marker=("."))
    axs[1, 0].set_title("Stations")

    plt.tight_layout()
    plt.show()
