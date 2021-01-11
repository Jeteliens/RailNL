# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

def visualise():
    x = [3, 5, 9, 12]
    y = [2, 6, 8, 13]
    n = ['Amsterdam', 'Alkmaar', 'Haarlem', 'Delft']

    # BBox = ((df.longitude.min(3.2932),   df.longitude.max(6.2869),      
        #  df.latitude.min(52.9701), df.latitude.max(51.6998))


    # for station in kaart.stations:
    #     x.append(station.x_position)
    #     y.append(station.y_position)

    # img = plt.imread("kaart1.png")
    plt.figure()
    # plt.imshow(img)
    plt.plot(x, y, c='g', marker=("."))

    for i, txt in enumerate(n):
        plt.annotate(txt, (y[i], x[i]))

    plt.title('Stations')

    plt.tight_layout()
    plt.xlim(-1, 15)
    plt.ylim(-1, 15)
    plt.show()
    plt.savefig("filename.jpeg", format="jpeg")

if __name__ == '__main__':
    
    visualise()