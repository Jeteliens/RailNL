from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise import randomise_train
from code.visualisation.visualise import visualise
import csv
import random

if __name__ == '__main__':
    
    stations_file = "data/Nationaal/StationsNationaal.csv"
    connections_file = "data/Nationaal/ConnectiesNationaal.csv"
    
    # stations_file = "data/Holland/StationsHolland.csv"
    # connections_file = "data/Holland/ConnectiesHolland.csv"

    # test_map = Map(stations_file, connections_file)
        
    number_of_trains = 15

    highest_score = 0
    lowest_score = 10000

    # randomise_train(test_map, number_of_trains)

    run_freq = 5
    scores_sum = 0

    print(f"Max number of train: {number_of_trains}")
    print(f"Number of states searched: {run_freq}")

    for _ in range(run_freq):
        test_map = Map(stations_file, connections_file)
        randomise_train(test_map, number_of_trains)

        if test_map.calculate_score() > highest_score:
            highest_score = test_map.calculate_score()
            best_map = test_map
        elif test_map.calculate_score() < lowest_score:
            lowest_score = test_map.calculate_score()
        
        scores_sum += test_map.calculate_score()

    average_score = scores_sum / run_freq

    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {average_score}")
    print(f"Number of ridden connections: {best_map.number_of_ridden_connections}")
    
    best_map.create_output()
    # test_map.create_output()

    # visualise(best_map)
    # visualise(test_map)