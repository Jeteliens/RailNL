from .randomise import Randomise
from code.classes.map import Map
from helpers.remove_duplicates import remove_duplicates
import csv
import copy
import random


class HillClimber:
    """Make changes to a random train from a map. Each improvement or
    equivalent solution is kept for the next iteration.
    Accepts only improvements.

    Attributes:
        stations_file:reference to the file with object information
        connections_file: reference to file with directions
        max_number_of_trains: maximum amount of trains in a map
        time_frame: maximum duration of a trajectory
        train_map:
        new_map: a map with a changed train
        iterations: run frequency
        train:
    """

    def __init__(self, stations_file, connections_file, max_number_of_trains, time_frame):
        self.max_number_of_trains = max_number_of_trains
        self.time_frame = time_frame
        self.map = copy.deepcopy(self.create_random_map(stations_file, connections_file))
        self.score = self.map.calculate_score()
    

    def create_random_map(self, stations_file, connections_file):
        """Creates a valid eandom map."""
        random_map = Map(stations_file, connections_file)
        randomise = Randomise(random_map)
        randomise.run(self.max_number_of_trains, self.time_frame)
        random_map = randomise.map

        return random_map


    def change_train(self, train_map):
        """Replace a random train in the map with another train."""
        # choose a random train from the map
        index = random.randint(0, len(train_map.trains) - 1)
        trajectory = train_map.trains[index]

        # create a new random train
        randomise = Randomise(train_map)
        new_train_data = randomise.create_train()
        new_train = new_train_data['train']
        new_train_distance = new_train_data['train_distance']

        old_train = trajectory['stations']
        old_train_distance = train_map.train_distances[index]

        # replace the old train
        trajectory['stations'] = new_train
        train_map.train_distances[index] = new_train_distance     

        ridden_connections_old_train = self.determine_ridden_connections(old_train)

        # update the data of the map
        for cnx_id in ridden_connections_old_train:
            train_map.all_ridden_connections.remove(cnx_id)
                
        train_map.ridden_connections = remove_duplicates(train_map.all_ridden_connections)
        train_map.number_of_ridden_connections = len(train_map.ridden_connections)
        train_map.total_distance += new_train_distance - old_train_distance


    def change_station(self, train_map):
        """Choose a random train in the map, remove first or last station 
        and add a new valid station."""
        # choose a random train
        index = random.randint(0, len(train_map.trains) - 1)
        trajectory = train_map.trains[index]
        train = trajectory['stations']
       
        # delete either the last or first station 
        if len(train[-1].directions) == 1:
            self.remove_last_station(trajectory, train_map, index)
        elif len(train[0].directions) == 1:
            self.remove_first_station(trajectory, train_map, index)

        # update map attributes
        train_map.total_distance = sum(train_map.train_distances)
        train_map.ridden_connections = remove_duplicates(train_map.all_ridden_connections)
        train_map.number_of_ridden_connections = len(train_map.ridden_connections)

    def check_solution(self, new_map):
        """Checks and accepts better solutions than the current solution."""
        old_score = self.score
        new_score = new_map.calculate_score()

        # accept only better scores
        if new_score >= old_score:
            self.map = copy.deepcopy(new_map)
            self.score = new_score

        if new_score > old_score:
            print(f"New high score: {new_score}")


    def run(self, iterations):
        """Iterate through algorithm."""
        self.iterations = iterations
  
        for _ in range(iterations):
            new_map = copy.deepcopy(self.map)
            # new_map = self.map
            # self.change_station(new_map)
            self.change_train(new_map)
            self.check_solution(new_map)

        return self.map
    

    def determine_ridden_connections(self, train):
        """Make and update a list of all connections that are ridden in a map."""
        ridden_connections = []
        
        # seperate train in connections
        connections_list = []
        for m in range(len(train) - 1):
            connection = train[m:m+2]
            connections_list.append(connection)

        for connection in connections_list:
            with open(self.map.connections_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                # give id to every ridden connection and add to list
                connection_id = 0
                for row in reader:
                    connection_id += 1

                    if row['station1'] == connection[0].name and row['station2'] == connection[1].name:
                        ridden_connections.append(connection_id)
                    elif row['station2'] == connection[0].name and row['station1'] == connection[1].name:
                        ridden_connections.append(connection_id)

        return ridden_connections


    def remove_last_station(self, trajectory, train_map, index):
        """Remove last station of a train and add one at the beginning."""
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
                
            train_distance = train_map.train_distances[index] 
            train_distance += distance_new_direction - distance_old_direction
            
            # make change to the map
            if train_distance <= train_map.time_frame:
                trajectory['stations'].pop()
                trajectory['stations'].insert(0, new_station)
                train_map.train_distances[index] = train_distance
                train_map.all_ridden_connections.remove(old_cnx_id)
                train_map.all_ridden_connections.append(new_cnx_id)


    def remove_first_station(self, trajectory, train_map, index):
        """Remove first station of a train and add one at the end."""
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
                
            train_distance = train_map.train_distances[index] 
            train_distance += distance_new_direction - distance_old_direction
            
            # make change to the map
            if train_distance <= train_map.time_frame:
                trajectory['stations'].pop(0)
                trajectory['stations'].append(new_station)
                train_map.train_distances[index] = train_distance
                train_map.all_ridden_connections.remove(old_cnx_id)
                train_map.all_ridden_connections.append(new_cnx_id)