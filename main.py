from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise import Randomise
from code.algorithms.hill_climber import HillClimber
from code.algorithms.simulated_annealing import SimulatedAnnealing
from code.visualisation.visualise import visualise
import csv
import random

TIME_FAME_HOLLAND = 120
MAX_TRAINS_HOLLAND = 7
TIME_FAME_NATIONAL = 180
MAX_TRAINS_NATIONAL = 20
TEMP = 50

if __name__ == '__main__':
    
    while True:
        type_of_file = input("Choose 1 to use the data of Holland\nChoose 2 to use the data of National:\n")
        
        if type_of_file == '1':
            stations_file = "data/Holland/StationsHolland.csv"
            connections_file = "data/Holland/ConnectiesHolland.csv"
            max_number_of_trains = MAX_TRAINS_HOLLAND
            time_frame = TIME_FAME_HOLLAND
            break
        elif type_of_file == '2':
            stations_file = "data/Nationaal/StationsNationaal.csv"
            connections_file = "data/Nationaal/ConnectiesNationaal.csv"
            max_number_of_trains = MAX_TRAINS_NATIONAL
            time_frame = TIME_FAME_NATIONAL
            break
    
    while True:
        iterations = int(input("How many iterations?: "))
        if iterations > 0:
            break
  
    while True:
        algorithm = input("Choose 1 to use Randomise\nChoose 2 to use HillClimber\nChoose 3 to use Simulated Annealing:\n")
        if algorithm == '1':
            train_map = Map(stations_file, connections_file)
            randomise = Randomise(train_map)
            randomise.run(max_number_of_trains, time_frame, iterations)
            best_map = randomise.map


            print(f"Highest score: {randomise.score}")
            print(f"Lowest score: {randomise.lowest_score}")
            print(f"Average score: {randomise.average_score}")

            best_map.create_output("random_output.csv")
            break
        elif algorithm == '2' or algorithm == '3':
            change_choice = input("Choose 1 to change trains\nChoose 2 to change stations:\n")
            if change_choice == '1':
                change = "Change train"
            elif change_choice == '2':
                change = "Change station"

            if algorithm == '2' and change == '1':
                hc = HillClimber(stations_file, connections_file, max_number_of_trains, time_frame)
                hc.map.create_output("output1.csv")
                first_score = hc.map.score
                print(f"Old score: {first_score}")

                best_map = hc.run(iterations, change)

                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
            elif algorithm == '3' and change == '2':
                while True:
                    choice = str(input("Choose temperature yourself?(y/n): ")).lower().strip()
                    if choice[0] == 'y':
                        temperature = int(input("Temperature: "))
                        break
                    elif choice[0] == 'n':
                        temperature = TEMP
                        break
                simanneal = SimulatedAnnealing(stations_file, connections_file, max_number_of_trains, time_frame, temperature)
                simanneal.map.create_output("output1.csv")
                print(f"Old score: {simanneal.map.score}")

                best_map = simanneal.run(iterations)
                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
            elif algorithm == '2' and change == '2':
                hc = HillClimber(stations_file, connections_file, max_number_of_trains, time_frame)
                hc.map.create_output("output1.csv")
                first_score = hc.map.score
                print(f"Old score: {first_score}")

                best_map = hc.run(iterations, change)

                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
            elif algorithm == '3' and change == '1':
                while True:
                    choice = str(input("Choose temperature yourself?(y/n): ")).lower().strip()
                    if choice[0] == 'y':
                        temperature = int(input("Temperature: "))
                        break
                    elif choice[0] == 'n':
                        temperature = TEMP
                        break
                
                simanneal = SimulatedAnnealing(stations_file, connections_file, max_number_of_trains, time_frame, temperature)
                simanneal.map.create_output("output1.csv")
                print(f"Old score: {simanneal.map.score}")

                best_map = simanneal.run(iterations, change)
                print(f"New score: {best_map.score}")

                best_map.create_output("output2.csv")
                break
    
    visualisation = str(input("Do you want a visualisation?(y/n): ")).lower().strip()
    
    if visualisation[0] == 'y':
        visualise(best_map)
