import random
import copy
from code.classes.map import Map
from helpers.remove_duplicates import remove_duplicates
from code.visualisation.visualise_names import visualise_names
from code.visualisation.visualise import visualise

class Randomise:
    """Make random trajectories.

    Attributes:
        train_map: input map
    """

    def __init__(self, train_map):
        self.map = train_map
        self.score = 0
        self.average_score = 0
        self.lowest_score = 0
    

    def run(self, number_of_trains, time_frame, iterations):
        """Iterate through algorithm."""
        self.map.time_frame = time_frame

        scores_sum = 0
        highest_score = 0
        lowest_score = 10000

        for iteration in range(iterations):
            random_map = self.create_map(number_of_trains)
            new_score = random_map.calculate_score()

            # if iteration == 0:
            #     visualise_names(random_map)

            if iteration != 0 and iteration%(iterations/100) == 0:
                print(f"Randomise: {(iteration / iterations)*100}%")
                print(f"Highest score: {highest_score}\n")
                # visualise(random_map)
            
            if new_score >= highest_score:
                best_map = random_map
                highest_score = new_score
            elif new_score < lowest_score:
                lowest_score = new_score

            if new_score > highest_score:
                print(f"New highest score: {new_score}")

            output_file = "results/scores_data_random.csv"
            
            with open(output_file, "a") as output:     
                output.write(f"{iteration},{highest_score}\n")

            scores_sum += new_score

        self.map = best_map
        self.score = self.map.calculate_score()
        self.average_score = scores_sum / iterations
        self.lowest_score = lowest_score


    def create_map(self, number_of_trains):
        """Put trains together in map."""
        train_map = copy.deepcopy(self.map)

        # train id
        t_id = 1
        
        # create multiple trains
        for _ in range(number_of_trains):
            if len(train_map.ridden_connections) == train_map.number_of_connections:
                break

            # create a train
            train_data = self.create_train(train_map)
            train = train_data['train']
            train_distance = train_data['train_distance']

            # add train to the map
            train_id = f"train_{t_id}"
            train_map.add_train(train_id, train, train_distance)
                
            t_id += 1

            # remove duplicated (ridden) connection ids from the list
            train_map.ridden_connections = remove_duplicates(train_map.ridden_connections)

        # determine the number of ridden connections
        train_map.number_of_ridden_connections = len(train_map.ridden_connections)

        return train_map


    def create_train(self, train_map):
        """Build a train for in the map."""
        # randomly chose the start point
        station = random.choice(self.map.stations)

        train = []
        train_distance = 0

        train.append(station)

        number_of_stations = len(self.map.stations)

        # create a train
        for _ in range(number_of_stations - 1):
            possible_directions = []
                
            # assure that no station is ridden more than once in a single trejectory
            for direction in station.directions:
                if direction[0] not in train:
                    possible_directions.append(direction)

            if possible_directions:
                next_station_data = random.choice(possible_directions)
            else:
                break

            # extract data of the next station
            next_station = next_station_data[0]
            distance_to_next_station = next_station_data[1]
            connection_id = next_station_data[2]

            if train_distance + distance_to_next_station > self.map.time_frame:
                break

            train.append(next_station)
            train_map.ridden_connections.append(connection_id)
            train_map.all_ridden_connections.append(connection_id) 
            train_distance += distance_to_next_station

            station = next_station

        train_data = {}
        train_data['train'] = train
        train_data['train_distance'] = train_distance

        return train_data
