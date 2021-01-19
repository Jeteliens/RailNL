from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise1 import randomise
# from code.visualisation.visualise import visualise
import csv
import random

if __name__ == '__main__':
    
    # stations_file = "data/Holland/StationsHolland.csv"
    # connections_file = "data/Holland/ConnectiesHolland.csv"
    # output = "output.csv"
    
    # test_map = Map(stations_file, connections_file)
    # test_map.create_map_object(output)
    # n = test_map.number_of_ridden_connections
    # print(f"Number of ridden connections: {n}")

    # --------------------------- Opdracht 1 ---------------------------------------

    # stations_file = "data/Holland/StationsHolland.csv"
    # connections_file = "data/Holland/ConnectiesHolland.csv"
    
    # max_number_of_trains = 7
    # time_frame = 120

    # while True:
    #     test_map = Map(stations_file, connections_file)
    #     randomise_train(test_map, max_number_of_trains, time_frame)

    #     if test_map.number_of_ridden_connections == test_map.number_of_connections:
    #         test_map.create_output()
    #         print(f"Found a map where all connections are ridden!")
    #         print(f"Number of ridden connections: {test_map.number_of_ridden_connections}")
    #         test_map.create_output()
    #         visualise(test_map)
    #         break
 

    # --------------------------- Opdracht 2 ---------------------------------------

    # stations_file = "data/Holland/StationsHolland.csv"
    # connections_file = "data/Holland/ConnectiesHolland.csv"
    
    # max_number_of_trains = 7
    # time_frame = 120

    # highest_score = 0
    # lowest_score = 10000

    # run_freq = 1000000
    # scores_sum = 0

    # for _ in range(run_freq):
    #     test_map = Map(stations_file, connections_file)
    #     randomise_train(test_map, max_number_of_trains, time_frame)

    #     if test_map.calculate_score() > highest_score:
    #         highest_score = test_map.calculate_score()
    #         best_map = test_map
    #         print(f"New highest score: {highest_score}")
    #     elif test_map.calculate_score() < lowest_score:
    #         lowest_score = test_map.calculate_score()
        
    #     scores_sum += test_map.calculate_score()

    # average_score = scores_sum / run_freq

    # print(f"Max number of train: {max_number_of_trains}")
    # print(f"Number of states searched: {run_freq}")
    # print("=================================")
    # print(f"Highest score: {highest_score}")
    # print(f"Lowest score: {lowest_score}")
    # print(f"Average score: {average_score}")
    # print(f"Number of ridden connections: {best_map.number_of_ridden_connections}")
    
    # best_map.create_output()


    # --------------------------- Opdracht 3 ---------------------------------------

    stations_file = "data/Nationaal/StationsNationaal.csv"
    connections_file = "data/Nationaal/ConnectiesNationaal.csv"
    
    max_number_of_trains = 20
    time_frame = 180

    highest_score = 0
    lowest_score = 10000

    run_freq = 10
    scores_sum = 0

    for _ in range(run_freq):
        test_map = Map(stations_file, connections_file)
        randomise(test_map, max_number_of_trains, time_frame)
        # randomise = Randomise(stations_file, connections_file)
        # randomise.run(max_number_of_trains, time_frame)

        if test_map.calculate_score() > highest_score:
            highest_score = test_map.calculate_score()
            best_map = test_map
            print(f"New highest score: {highest_score}")
        elif test_map.calculate_score() < lowest_score:
            lowest_score = test_map.calculate_score()
        
        scores_sum += test_map.calculate_score()

    average_score = scores_sum / run_freq

    print(f"Max number of train: {max_number_of_trains}")
    print(f"Number of states searched: {run_freq}")
    print("=================================")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {average_score}")
    print(f"Number of ridden connections: {best_map.number_of_ridden_connections}")
    print(f"Number of trains: {best_map.number_of_trains}")

    best_map.create_output()