import csv
from .station import Station
# import json

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
        self.train_distances = []
        self.total_distance = 0
        self.number_of_connections = self.calculate_number_of_connections(connections_file)
        self.number_of_ridden_connections = 0
        self.ridden_connections = []
        self.all_ridden_connections = []
        self.score = 0
        self.time_frame = None

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
        self.train_distances.append(train_distance)

    def calculate_score(self):
        """Calculate the quality of the trajectories."""
        p = self.number_of_ridden_connections / self.number_of_connections
        T = self.number_of_trains
        Min = self.total_distance
        
        quality_score = p*10000 - (T*100 + Min)

        self.score = quality_score
        return quality_score

    def create_output(self, output_name):
        """Build an output csvfile with alle trajectory information."""
        csv_colums = ['train', 'stations']
        output_file = output_name
        
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, fieldnames=csv_colums)
            writer.writeheader()
           
            for train in self.trains:
                writer.writerow(train)

            output.write(f"score,{self.calculate_score()}")

    # def create_extra_output(self, train_distance):

    #     csv_colums = ['train', 'distance']
    #     extra_output = "extra_output.csv"

    #     with open(extra_output, "w") as output:
    #         writer = csv.DictWriter(output, fieldnames=csv_colums)
    #         writer.writeheader()

    #         for train in self.trains:

    #             writer.writerow(train)
    #             writer.writerow(train_distance)

    #         output.write(f"score,{self.calculate_score()}\n")
    #         output.write(f"number of connections,{self.number_of_connections}\n")
    #         output.write(f"number of ridden connections,{self.number_of_ridden_connections}\n")
    #         output.write(f"total distance,{self.total_distance}\n")
    #         output.write(f"number of trains,{self.number_of_trains}")
            
    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list