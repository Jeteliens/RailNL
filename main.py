from code.classes.map import Kaart
from code.classes.station import Station
from code.algorithms.randomise import randomise_train
import random

if __name__ == '__main__':
    
    stations_file = "data/Holland/StationsHolland.csv"
    connections_file = "data/Holland/ConnectiesHolland.csv"
    
    test_map = Kaart(stations_file)
    
    visualise(test_map.directions)
    
    for station in test_map.stations:
        station.add_directions(connections_file)
    
    number_of_trains = random.randint(1,7)

    randomise_train(test_map, number_of_trains)
    # add_train

    test_map.create_output()

    # print(test_map.stations)
    # print("\n")
    # print(test_map.stations[1].x_position)
    # print(test_map.stations[1].y_position)