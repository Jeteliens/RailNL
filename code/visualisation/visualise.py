import matplotlib.pyplot as plt

def visualise(self, kaart):
    x = []
    y = []

    for station in kaart.stations:
        x.append(station.x_position)
        y.append(station.y_position)

    plt.figure(figsize=(9, 3))

    plt.scatter(x, y, c=r, marker=("."))
    plt.set_title("Stations")

    # plt.tight_layout()
    plt.show()
    plt.savefig("filename.ext", format="ext")

    # positions = [station for station in map.stations.values()]
    # name = [station.name for station in positions]
    # color = [station.get_value().colour.get_web() if station is not None else "grey"
    #           for station in positions]