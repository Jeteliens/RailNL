from .randomise2 import Randomise
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
            self.map.score = new_score
            print(f"New high score: {new_score}")

    def run(self, iterations):
        self.iterations = iterations
  
        for _ in range(iterations):
            new_map = copy.deepcopy(self.map)
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