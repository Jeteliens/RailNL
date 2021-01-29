from code.classes.map import Map
from code.classes.station import Station
from code.algorithms.randomise import Randomise
from code.algorithms.hill_climber import HillClimber
from code.algorithms.simulated_annealing import SimulatedAnnealing
from code.visualisation.visualise_names import visualise_names
import csv
import random

TIME_FAME_HOLLAND = 120
MAX_TRAINS_HOLLAND = 7
TIME_FAME_NATIONAL = 180
MAX_TRAINS_NATIONAL = 20
TEMP = 50

if __name__ == '__main__':
    # choose for which area you want to make trajectories
    while True:
        type_of_file = input("For files choose 1 or 2:\n 1: Holland\n 2: National\n==> ")
        
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
    
    # choose the amount of iterations
    while True:
        iterations = int(input("----\nHow many iterations?: "))
        if iterations > 0:
            break
  
    # choose the algorithm
    while True:
        algorithm = input("----\nFor algorithm choose 1, 2 or 3:\n 1: Randomise\n 2: HillClimber\n 3: Simulated Annealing\n==> ")
        if algorithm == '1':
            train_map = Map(stations_file, connections_file)
            randomise = Randomise(train_map)
            randomise.run(max_number_of_trains, time_frame, iterations)
            best_map = randomise.map

            print(f"Highest score: {randomise.score}")
            print(f"Lowest score: {randomise.lowest_score}")
            print(f"Average score: {randomise.average_score}")

            best_map.create_output("output_random.csv")
            break

        # choose the type of change 
        elif algorithm == '2' or algorithm == '3':
            while True:
                change_choice = input("----\nFor change choose 1 or 2:\n 1: change trains\n 2: change stations\n==> ")
                if change_choice == '1':
                    change = "Change train"
                    break
                elif change_choice == '2':
                    change = "Change station"
                    break

            # hillclimber
            if algorithm == '2':
                hc = HillClimber(stations_file, connections_file, max_number_of_trains, time_frame)
                hc.map.create_output("output_hc1.csv")
                visualise_names(hc.map)
                first_score = hc.map.score
                print(f"Old score: {first_score}")

                best_map = hc.run(iterations, change)

                print(f"Old score: {first_score}")
                print(f"New score: {best_map.score}")

                best_map.create_output("output_hc2.csv")
                break
            
            # simulated annealing 
            elif algorithm == '3':
                while True:
                    choice = str(input("----\nChoose temperature yourself?(y/n): ")).lower().strip()
                    # use chosen temperature
                    if choice[0] == 'y':
                        temperature = int(input("Temperature: "))
                        break
                    # use standard temperature
                    elif choice[0] == 'n':
                        temperature = TEMP
                        break
                simanneal = SimulatedAnnealing(stations_file, connections_file, max_number_of_trains, time_frame, temperature)
                simanneal.map.create_output("output_sa1.csv")
                visualise_names(simanneal.map)
                first_score = simanneal.map.score
                print(f"Old score: {first_score}")

                best_map = simanneal.run(iterations, change)

                print(f"Old score: {first_score}")
                print(f"Last new score: {best_map.score}")

                best_map = simanneal.best_map
                print(f"Highest encountered score: {best_map.calculate_score()}")

                best_map.create_output("output_sa2.csv")
                break
    
    # choose for a visualisation or not
    # while True:
    #     visualisation = str(input("----\nDo you want a visualisation?(y/n): ")).lower().strip()
    
    #     if visualisation[0] == 'y':
    #         visualise_names(best_map)
    #         break
    #     if visualisation[0] == 'n':
    #         break

    visualise_names(best_map)