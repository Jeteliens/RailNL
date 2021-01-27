from .randomise import Randomise
from code.classes.map import Map
import csv
import copy
import random

class HillClimber():
    """
    The HillClimber class that iterates through the trains in a map and replaces a random train with another. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, stations_file, connections_file, max_number_of_trains, time_frame):
        self.max_number_of_trains = max_number_of_trains
        self.time_frame = time_frame
        self.map = copy.deepcopy(self.create_random_map(stations_file, connections_file))
        self.score = self.map.calculate_score()
    
    def create_random_map(self, stations_file, connections_file):
        random_map = Map(stations_file, connections_file)

        randomise = Randomise(random_map)
        randomise.run(self.max_number_of_trains, self.time_frame)
        random_map = randomise.map

        return random_map

    def make_change(self, map):
        n = random.randint(0, len(map.trains) - 1)
        trajectory = map.trains[n]
        randomise = Randomise(map)
        new_train_data = randomise.create_train()

        old_train = trajectory['stations']
        new_train = new_train_data['train']
        new_train_distance = new_train_data['train_distance']
        trajectory['stations'] = new_train
        old_train_distance = map.train_distances[n]
        map.train_distances[n] = new_train_distance

        map.total_distance = map.total_distance + new_train_distance - old_train_distance

        ridden_connections_old_train = self.determine_ridden_connections(old_train)

        for cnx_id in ridden_connections_old_train:
            map.all_ridden_connections.remove(cnx_id)
                
        map.ridden_connections = self.remove_duplicates(map.all_ridden_connections)
        map.number_of_ridden_connections = len(map.ridden_connections)

    def make_small_change(self, map):
        index = random.randint(0, len(map.trains) - 1)
        trajectory = map.trains[index]
        train = trajectory['stations']
       
        # make small change to the chosen train
        if len(train[-1].directions) == 1:
            self.remove_last_station(trajectory, map, index)
        elif len(train[0].directions) == 1:
            self.remove_first_station(trajectory, map, index)

        # update map attributes
        map.total_distance = sum(map.train_distances)
        map.ridden_connections = self.remove_duplicates(map.all_ridden_connections)
        map.number_of_ridden_connections = len(map.ridden_connections)

    def check_solution(self, new_map):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        old_score = self.score
        new_score = new_map.calculate_score()

        if new_score >= old_score:
            self.map = copy.deepcopy(new_map)
            self.score = new_score

        if new_score > old_score:
            print(f"New high score: {new_score}")

    def run(self, iterations):
        self.iterations = iterations
  
        for _ in range(iterations):
            new_map = copy.deepcopy(self.map)
            # new_map = self.map
            # self.make_change(new_map)
            self.make_change(new_map)
            self.check_solution(new_map)

        return self.map
    
    def determine_ridden_connections(self, train):

        ridden_connections = []
        
        connections_list = []
        for m in range(len(train) - 1):
            connection = train[m:m+2]
            connections_list.append(connection)

        for connection in connections_list:
            with open(self.map.connections_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                connection_id = 0
                for row in reader:
                    connection_id += 1

                    if row['station1'] == connection[0].name and row['station2'] == connection[1].name:
                        ridden_connections.append(connection_id)
                    elif row['station2'] == connection[0].name and row['station1'] == connection[1].name:
                        ridden_connections.append(connection_id)

        return ridden_connections

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list

    def remove_last_station(self, trajectory, map, index):
        
        train = trajectory['stations']
        possible_new_directions = [direction for direction in train[0].directions if direction[0] != train[1]]
    
        # remove ridden stations
        for direction in possible_new_directions:
            for station in train:
                if direction[0] == station:
                    possible_new_directions.remove(direction)

        # add new station to the front
        if possible_new_directions:     
            new_direction = random.choice(possible_new_directions)
            new_station = new_direction[0]
            distance_new_direction = new_direction[1]
            new_cnx_id = new_direction[2]
                            
            # determine the distance to the station to be removed
            distance_old_direction = 0
            for direction in train[-1].directions:
                if direction[0] == train[-2]:
                    distance_old_direction = direction[1]
                    old_cnx_id = direction[2]
                    break
                
            train_distance = map.train_distances[index] 
            train_distance += distance_new_direction - distance_old_direction
            
            # make change to the map
            if train_distance <= map.time_frame:
                trajectory['stations'].pop()
                trajectory['stations'].insert(0, new_station)
                map.train_distances[index] = train_distance
                map.all_ridden_connections.remove(old_cnx_id)
                map.all_ridden_connections.append(new_cnx_id)

    def remove_first_station(self, trajectory, map, index):

        train = trajectory['stations']
        possible_new_directions = [direction for direction in train[-1].directions if direction[0] != train[-2]]

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