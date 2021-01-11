# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

def visualise():
    x = [3, 5, 9]
    y = [2, 6, 8]

    # for station in kaart.stations:
    #     x.append(station.x_position)
    #     y.append(station.y_position)

    plt.figure(figsize=(9, 3))

    plt.scatter(x, y, c='g', marker=("."))
    # plt.set_title("Stations")

    # plt.tight_layout()
    plt.show()
    plt.savefig("filename.jpeg", format="jpeg")

if __name__ == '__main__':
    
    visualise()