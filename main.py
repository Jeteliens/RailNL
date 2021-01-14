from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise import randomise_train
from code.visualisation.visualise import visualise
import csv
import random

if __name__ == '__main__':
    
    stations_file = "data/Holland/StationsHolland.csv"
    connections_file = "data/Holland/ConnectiesHolland.csv"
    
    test_map = Map(stations_file, connections_file)
        
    number_of_trains = 7

    randomise_train(test_map, number_of_trains)

    # visualise(test_map)

    test_map.create_output()