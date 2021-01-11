from code.classes.map import Kaart
from code.classes.station import Station
from code.algorithms.randomise import randomise_train
# from code.visualisation.visualise import visualise
import random

if __name__ == '__main__':
    
    stations_file = "data/Holland/StationsHolland.csv"
    connections_file = "data/Holland/ConnectiesHolland.csv"
    
    test_map = Kaart(stations_file)

    # print(test_map.stations)
    
    for station in test_map.stations:
        # print(station)
        station.add_directions(connections_file, test_map.stations)
        # for direction in station.directions:
        #     # print(direction)
        #     for element in test_map.stations_dictionary:
        #         # print(element)
        #         if direction[0] == element:
        #             # print(direction[0])
        #             direction[0] = test_map.stations_dictionary[element]

    # visualise(test_map.directions)
    
    number_of_trains = random.randint(1,7)

    trains = randomise_train(test_map, number_of_trains)
    
    for train in trains:
        print(train)
    
    # add_train
    # for train in trains:
    #     id = 1
    #     train_id = f"train_{i}"
    #     train_distance
    #     test_map.add_train(train_id, train, train_distance)
    #     id += 1

    test_map.create_output()

    # print(test_map.stations)
    # print("\n")
    # print(test_map.stations[1].x_position)
    # print(test_map.stations[1].y_position)s