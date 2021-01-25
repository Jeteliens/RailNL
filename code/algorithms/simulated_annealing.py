import random
import math
from code.classes.map import Map
from code.algorithms.randomise2 import Randomise

class SimulatedAnnealing():
    """
    The SimulatedAnnealing class that replaces the last or first station of a random train in a map with a random valid station.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """

    def __init__(self, stations_file, connections_file, max_number_of_trains, time_frame, temperature):
        self.station_file = stations_file
        self.connections_file = connections_file
        self.max_number_of_trains = max_number_of_trains
        self.time_frame = time_frame
        self.map = self.create_random_map(stations_file, connections_file)
        self.T0 = temperature
        self.T = temperature
        self.score = self.map.calculate_score()

    def create_random_map(self, stations_file, connections_file):
        random_map = Map(stations_file, connections_file)

        randomise = Randomise(random_map)
        randomise.run(self.max_number_of_trains, self.time_frame)
        random_map = randomise.map

        return random_map

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        
        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def make_small_change(self, map):
        index = random.randint(0, len(map.trains) - 1)
        trajectory = map.trains[index]
        train = trajectory['stations']

        # make small change to the chosen train
        if len(train[-1].directions) == 1:
            # possible_new_directions = train[0].directions.remove[train[1]]
            possible_new_directions = [direction for direction in train[0].directions if direction[0] != train[1]]
                
            # for direction in train[0].directions:
            #     if direction[0] != train[1]:
            #         possible_new_stations.append(direction[0])

            # remove ridden stations
            for direction in possible_new_directions:
                for station in train:
                    if direction[0] == station:
                        possible_new_directions.remove(direction)

            # add new train to the front
            if possible_new_directions:     
                new_direction = random.choice(possible_new_directions)
                new_station = new_direction[0]
                distance_new_direction = new_direction[1]
                                
                # determine the distance to the station to be removed
                distance_old_direction = 0
                for direction in train[-1].directions:
                    if direction[0] == train[-2]:
                        distance_old_direction = direction[1]
                        break
                    
                train_distance = map.train_distances[index] 
                train_distance += distance_new_direction - distance_old_direction
                
                if train_distance <= map.time_frame:
                    trajectory['stations'].pop()
                    trajectory['stations'].insert(0, new_station)
                    map.train_distances[index] = train_distance
                    
        elif len(train[0].directions) == 1:
            possible_new_directions = [direction for direction in train[-1].directions if direction[0] != train[-2]]
                
            # for direction in train[0].directions:
            #     if direction[0] != train[1]:
            #         possible_new_stations.append(direction[0])

            # remove ridden stations
            for direction in possible_new_directions:
                for station in train:
                    if direction[0] == station:
                        possible_new_directions.remove(direction)

            # add new train to the front
            if possible_new_directions:     
                new_direction = random.choice(possible_new_directions)
                new_station = new_direction[0]
                distance_new_direction = new_direction[1]
                                
                # determine the distance to the station to be removed
                distance_old_direction = 0
                for direction in train[0].directions:
                    if direction[0] == train[1]:
                        distance_old_direction = direction[1]
                        break
                    
                train_distance = map.train_distances[index] 
                train_distance += distance_new_direction - distance_old_direction
                
                if train_distance <= map.time_frame:
                    trajectory['stations'].pop(0)
                    trajectory['stations'].append(new_station)
                    map.train_distances[index] = train_distance
        else:                  
            # determine the distance to the station to be removed
            distance_old_direction = 0
            for direction in train[-1].directions:
                if direction[0] == train[-2]:
                    distance_old_direction = direction[1]
                    break
                    
            train_distance = map.train_distances[index] 
            train_distance -= distance_old_direction
            trajectory['stations'].pop()
            map.train_distances[index] = train_distance

    def check_solution(self, new_map):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        old_score = self.score
        new_score = new_map.calculate_score()
        
        # Calculate the probability of accepting this new map
        delta = new_score - old_score
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.map = new_map
            self.score = new_score

        # Update the temperature
        self.update_temperature()
        

    def run(self, iterations):
        self.iterations = iterations

        random_map = self.map
        
        for _ in range(iterations):
            self.make_small_change(random_map)
            self.check_solution(random_map)

        return self.map
