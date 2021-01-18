import csv
from .station import Station

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
        self.trains = []
        self.number_of_trains = 0
        self.stations = self.load_stations(stations_file, connections_file)
        self.ridden_stations = []
        self.total_distance = 0
        self.number_of_connections = self.calculate_number_of_connections(connections_file)
        self.number_of_ridden_connections = 0


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
        temp_list = [] 
        [temp_list.append(station) for station in self.ridden_stations if station not in temp_list]
        self.ridden_stations = temp_list

        self.number_of_trains += 1
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