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
        # print(f"1. Train: {train}")
        # print(f"Old train distances: {map.train_distances}")
        # print(map.all_ridden_connections)
        # print(f"Old: {map.ridden_connections}")

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
                new_cnx_id = new_direction[2]
                                
                # determine the distance to the station to be removed
                distance_old_direction = 0
                # print(f"2. Train: {train}")
                for direction in train[-1].directions:
                    if direction[0] == train[-2]:
                        distance_old_direction = direction[1]
                        old_cnx_id = direction[2]
                        break
                    
                train_distance = map.train_distances[index] 
                train_distance += distance_new_direction - distance_old_direction
                
                if train_distance <= map.time_frame:
                    trajectory['stations'].pop()
                    trajectory['stations'].insert(0, new_station)
                    map.train_distances[index] = train_distance
                    map.all_ridden_connections.remove(old_cnx_id)
                    map.all_ridden_connections.append(new_cnx_id)
                    
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
                new_cnx_id = new_direction[2]
                                
                # determine the distance to the station to be removed
                distance_old_direction = 0
                for direction in train[0].directions:
                    if direction[0] == train[1]:
                        distance_old_direction = direction[1]
                        old_cnx_id = direction[2]
                        break
                    
                train_distance = map.train_distances[index] 
                train_distance += distance_new_direction - distance_old_direction
                
                if train_distance <= map.time_frame:
                    trajectory['stations'].pop(0)
                    trajectory['stations'].append(new_station)
                    map.train_distances[index] = train_distance
                    map.all_ridden_connections.remove(old_cnx_id)
                    map.all_ridden_connections.append(new_cnx_id)
        # else:                  
        #     # determine the distance to the station to be removed
        #     distance_old_direction = 0
        #     # print(f"3. Train: {train}")
        #     for direction in train[-1].directions:
        #         if direction[0] == train[-2]:
        #             distance_old_direction = direction[1]
        #             old_cnx_id = direction[2]
        #             break
        #     if len(train) > 2:        
        #         train_distance = map.train_distances[index] 
        #         train_distance -= distance_old_direction
        #         trajectory['stations'].pop()
        #         map.train_distances[index] = train_distance
        #         map.all_ridden_connections.remove(old_cnx_id)

        # map.calculate_score()

        map.total_distance = sum(map.train_distances)
        map.ridden_connections = self.remove_duplicates(map.all_ridden_connections)
        self.map.number_of_ridden_connections = len(self.map.ridden_connections)
        # print(f"New train distances: {map.train_distances}")
        # print(f"New: {map.ridden_connections}")
        return map

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
  
        for iteration in range(iterations):
            # print(f"Iteration {iteration}")      
            map = self.make_small_change(random_map)
            self.check_solution(map)

        return self.map

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list
