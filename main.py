from code.classes.map import Kaart
from code.classes.station import Station
from code.algorithms.randomise import randomise_train
from code.visualisation.visualise import visualise
import csv
import random

if __name__ == '__main__':
    
    stations_file = "data/Holland/StationsHolland.csv"
    connections_file = "data/Holland/ConnectiesHolland.csv"
    
    test_map = Kaart(stations_file)

    # print(test_map.stations)
    
    for station in test_map.stations:
        # print(station)
        station.add_directions(connections_file, test_map.stations)

    with open(connections_file, 'r') as in_file:
        reader = csv.reader(in_file)
        test_map.number_of_connections = len(list(reader)) - 1
        # print(number_of_connections)

    # visualise(test_map.directions)
    
    # number_of_trains = random.randint(2,8)
    number_of_trains = 8

    trains_data = randomise_train(test_map, number_of_trains)
    # print(trains_data)

    trains = trains_data[0]
    # print(trains)
    trains_distances = trains_data[1]
    # print(trains_distances)
    
    # for train in trains:
    #     print(train)

    # print(trains_data)
    # print(trains_distances)
    
    # add_train
    id = 1

    for train in trains:
        train_id = f"train_{id}"
        train_distance = trains_distances[id-1]
        test_map.add_train(train_id, train, train_distance)

        id += 1

    # visualise(test_map)

    # create csv output file
    test_map.create_output()

    # print(test_map.stations)
    # print("\n")
    # print(test_map.stations[1].x_position)
    # print(test_map.stations[1].y_position)s