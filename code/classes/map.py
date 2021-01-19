import csv
from .station import Station
import json

class Map():
    """Put a map together with trajectories.

    Read the object and connections information.
    Make a list for every object with matching object information.
    Count number of connections for object.
    Build trajectories and make output file.

    Attributes:
        stations_file: reference to the file with object information
        connections_file: reference to the file with object information
        train_id: specific number for every trajectory
        train_trajectory: list of stations in a trajectory
        train_distance: the sum of distances between all stations in a trajectory
    """

    def __init__(self, stations_file, connections_file):
        self.connections_file = connections_file
        self.trains = []
        self.number_of_trains = 0
        self.stations = self.load_stations(stations_file, connections_file)
        self.ridden_stations = []
        self.total_distance = 0
        self.number_of_connections = self.calculate_number_of_connections(connections_file)
        self.number_of_ridden_connections = 0
        self.ridden_connections = []

    def load_stations(self, stations_file, connections_file):
        """Read csv files and save the information in lists."""
        stations = []
        
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
        
            for row in reader:
                stations.append(Station(row['station'], float(row['x']), float(row['y'])))

        for station in stations:
            station.add_directions(connections_file, stations)
        
        return stations

    def calculate_number_of_connections(self, connections_file):
        """Count the connections of the object."""
        with open(connections_file, 'r') as in_file:
            reader = csv.reader(in_file)
            number_of_connections = len(list(reader)) - 1

        return number_of_connections
    
    def add_train(self, train_id, train_trajectory, train_distance):
        """Create trajectory."""
        trajectory = {}
        trajectory["train"] = train_id
        trajectory["stations"] = train_trajectory
        self.trains.append(trajectory)

        for station in train_trajectory:
            self.ridden_stations.append(station)

        # remove duplicated ridden stations from the list
        self.ridden_stations = self.remove_duplicates(self.ridden_stations)
        # temp_list = [] 
        # [temp_list.append(station) for station in self.ridden_stations if station not in temp_list]
        # self.ridden_stations = temp_list

        self.number_of_trains = len(self.trains)
        self.total_distance += train_distance

    def calculate_score(self):
        """Calculate the quality of the trajectories."""
        p = self.number_of_ridden_connections / self.number_of_connections
        T = self.number_of_trains
        Min = self.total_distance
        
        quality_score = p*10000 - (T*100 + Min)

        return quality_score

    def create_output(self):
        """Build an output csvfile with alle trajectory information."""
        csv_colums = ['train', 'stations']
        output_file = "output.csv"
        
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, fieldnames=csv_colums)
            writer.writeheader()
           
            for train in self.trains:
                writer.writerow(train)

            output.write(f"score,{self.calculate_score()}")

    def create_map_object(self, file):

        with open(file, 'r') as in_file:
            reader = csv.DictReader(in_file)
        
            for row in reader:
                if row['train'] == "score":
                    break
                
                train_data = {}
                # stations.append(Station(row['station'], float(row['x']), float(row['y'])))
                train_data['train'] = row['train']
                train_data['stations'] = json.loads(row['stations'])
                train = json.loads(row['stations'])
                # print(train)
                self.trains.append(train_data)
                # self.number_of_trains = len(self.trains)
                
                for station in train:
                    self.ridden_stations.append(station)
                    # connection = []
                    # connection.append(station)

                # print(train)
                # print(f"len(train): {len(train)}")
                for n in range(len(train) - 1):
                    connection = train[n:n+1]
                    self.ridden_connections.append(connection)
        
        self.number_of_trains = len(self.trains)
        self.total_distance = self.calculate_total_distance()
        self.number_of_ridden_connections = self.calculate_number_of_ridden_connections(file)
        self.ridden_stations = self.remove_duplicates(self.ridden_stations)

        # self.number_of_ridden_connections = 

    def calculate_total_distance(self):

        total_distance = 0

        connections_data = []
        with open(self.connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            for row in reader:
                data_1 = []
                data_2 = []
                
                data_1.append(row['station1'])
                data_1.append(row['station2'])
                data_1.append(row['distance'])

                data_2.append(row['station2'])
                data_2.append(row['station1'])
                data_2.append(row['distance'])

                connections_data.append(data_1)
                connections_data.append(data_2)
        
        # print("Ridden connections:")
        # print(self.ridden_connections)
        for element in self.ridden_connections:
            # print(f"Element: {element}")
            for connection in connections_data:
                # print(f"Connection: {connection}")
                if element[0] == connection[0] and element[1] == connection[1]:
                    total_distance += connection[2]
                    
        print(f"Total distance 1: {total_distance}")
        return total_distance

    def calculate_number_of_ridden_connections(self, file):

        score = None

        with open(file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            for row in reader:
                if row['train'] == "score":
                    score = float(row['stations'])
                    break

        print(f"Score: {score}")
        noc = self.number_of_connections
        print(f"Number of connections: {noc}")
        T = self.number_of_trains
        print(f"Number of trains: {T}")
        Min = self.total_distance
        print(f"Total distance: {Min}")
    
        norc = ((score + (T*100 + Min))*noc) / 10000
        print(f"Number of ridden connections: {norc}")

        return norc

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list