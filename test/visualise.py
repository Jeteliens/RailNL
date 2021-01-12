import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def visualise():

    plt.figure(figsize=(2.61538461538, 3))
    ax = plt.axes(projection=ccrs.EuroPP())
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    # ax.coastlines(resolution='50m')
    ax.gridlines()

    ax.set_extent([-150, 60, -25, 60])
    # img_extent = (-120.67660000000001, -106.32104523100001, 13.2301484511245, 30.766899999999502)

    x = [3, 5, 9, 12]
    y = [2, 6, 8, 13]
    n = ['Amsterdam', 'Alkmaar', 'Haarlem', 'Delft']


    # BBox = ((df.longitude.min(3.2932),   df.longitude.max(6.2869),      
        #  df.latitude.min(52.9701), df.latitude.max(51.6998))


    # for station in kaart.stations:
    #     x.append(station.x_position)
    #     y.append(station.y_position)


    # plt.figure()
    # plt.plot(x, y, c='g', marker=("."))

    # for i, txt in enumerate(n):
    #     plt.annotate(txt, (y[i], x[i]))

    # plt.title('Stations')

    # plt.tight_layout()
    # plt.xlim(-1, 15)
    # plt.ylim(-1, 15)
    plt.show()
    plt.savefig("filename.jpeg", format="jpeg")

if __name__ == '__main__':
    
    visualise()