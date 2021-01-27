from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise import Randomise
from code.algorithms.hill_climber import HillClimber
from code.algorithms.simulated_annealing import SimulatedAnnealing
from code.visualisation.visualise import visualise
from code.visualisation.plot import plot
import csv
import random
import sys

if __name__ == '__main__':
    
    while True:
        type_of_file = input("Choose 1 to use the data of Holland\nChoose 2 to use National data:\n")
        
        if type_of_file == '1':
            stations_file = "data/Holland/StationsHolland.csv"
            connections_file = "data/Holland/ConnectiesHolland.csv"
            max_number_of_trains = 7
            time_frame = 120
            break
        elif type_of_file == '2':
            stations_file = "data/Nationaal/StationsNationaal.csv"
            connections_file = "data/Nationaal/ConnectiesNationaal.csv"
            max_number_of_trains = 20
            time_frame = 180
            break
    
    while True:
        iterations = int(input("How many iterations?: "))
        if iterations > 0:
            break
  
    while True:
        algorithm = input("Choose 1 to use Randomise\nChoose 2 to use HillClimber\nChoose 3 to use Simulated Annealing:\n")
        if algorithm == '1':
            for i in range(iterations):
                test_map = Map(stations_file, connections_file)
                randomise(test_map, max_number_of_trains, time_frame)
                if test_map.calculate_score() > highest_score:
                    highest_score = test_map.calculate_score()
                    best_map = test_map
                    print(f"New highest score: {highest_score}")
                elif test_map.calculate_score() < lowest_score:
                    lowest_score = test_map.calculate_score()
            
                    scores_sum += test_map.calculate_score()

                average_score = scores_sum / run_freq

                print(f"Highest score: {highest_score}")
                best_map.create_output()
                break
        elif algorithm == '2' or algorithm == '3':
            change = input("Choose 1 to change trains\nChoose 2 to change stations:\n")
            if algorithm == '2' and change == '1':
                hc = HillClimber(stations_file, connections_file, max_number_of_trains, time_frame)
                hc.map.create_output("output1.csv")
                first_score = hc.map.score
                print(f"Old score: {first_score}")

                best_map = hc.run(iterations)

                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
            elif algorithm == '3' and change == '2':
                temperature = 50
                simanneal = SimulatedAnnealing(stations_file, connections_file, max_number_of_trains, time_frame, temperature)
                simanneal.map.create_output("results/output1.csv")
                print(f"Old score: {simanneal.map.score}")

                best_map = simanneal.run(iterations)
                print(f"New score: {best_map.score}")

                best_map.create_output("results/output2.csv")
                break
            elif algorithm == '2' and change == '2':
                hc = HillClimber(stations_file, connections_file, max_number_of_trains, time_frame)
                hc.map.create_output("output1.csv")
                first_score = hc.map.score
                print(f"Old score: {first_score}")

                best_map = hc.run(iterations)

                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
            elif algorithm == '3' and change == '1':
                temperature = 50
                simanneal = SimulatedAnnealing(stations_file, connections_file, max_number_of_trains, time_frame, temperature)
                simanneal.map.create_output("results/output1.csv")
                print(f"Old score: {simanneal.map.score}")

                best_map = simanneal.run(iterations)
                print(f"New score: {best_map.score}")

                best_map.create_output("results/output2.csv")
                break
    
    visualisation = str(input("Do you want a visualisation?(y/n): ")).lower().strip()
    
    if visualisation[0] == 'y':
        visualise(best_map)
