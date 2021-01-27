import random
import copy
from code.classes.map import Map
# time_frame = 120

class Randomise:
    
    def __init__(self, train_map):
        self.map = train_map
        # a list that contains the id's of the ridden connections
        self.ridden_connections = []
    
    def run(self, number_of_trains, time_frame):
        
        self.map.time_frame = time_frame

        # train id
        t_id = 1
        
        # create multiple trains
        for _ in range(number_of_trains):
            if len(self.ridden_connections) == self.map.number_of_connections:
                break

            # create a train
            train_data = self.create_train()
            train = train_data['train']
            train_distance = train_data['train_distance']

            # add train to the map
            train_id = f"train_{t_id}"
            self.map.add_train(train_id, train, train_distance)
                
            t_id += 1

            # remove duplicated (ridden) connection ids from the list
            self.ridden_connections = self.remove_duplicates(self.ridden_connections)

        # determine the number of ridden connections
        self.map.number_of_ridden_connections = len(self.ridden_connections)


    def create_train(self):

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
            self.ridden_connections.append(connection_id)
            self.map.all_ridden_connections.append(connection_id) 
            train_distance += distance_to_next_station

            station = next_station

        train_data = {}
        train_data['train'] = train
        train_data['train_distance'] = train_distance

        return train_data

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list