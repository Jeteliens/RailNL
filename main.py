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

    highest_score = 0
    lowest_score = 10000

    randomise_train(test_map, number_of_trains)

    # for _ in range(5):
    #     randomise_train(test_map, number_of_trains)

    #     if test_map.calculate_score() > highest_score:
    #         highest_score = test_map.calculate_score()
    #         best_map = test_map
    #     elif test_map.calculate_score() < lowest_score:
    #         lowest_score = test_map.calculate_score()

    # print(f"Highest score is: {highest_score}")
    # print(f"Lowesst score is: {lowest_score}")

    # best_map.create_output()
    test_map.create_output()

    # visualise(test_map)