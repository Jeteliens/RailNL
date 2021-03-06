import csv
from .station import Station
from helpers.remove_duplicates import remove_duplicates


class Map:
    """Put a map together with trajectories.

    Read the object and connections information.
    Make a list for every object with matching object information.
    Count number of connections for object.
    Build trajectories and make output file.

    Attributes:
        stations_file: reference to the file with object information
        connections_file: reference to the file with object information
    """

    def __init__(self, stations_file, connections_file):
        self.connections_file = connections_file
        self.trains = []
        self.number_of_trains = 0
        self.stations = self.load_stations(stations_file, connections_file)
        # self.ridden_stations = self.determine_ridden_stations()
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
        
            # add the positions of the stations
            for row in reader:
                stations.append(Station(row['station'], float(row['x']), float(row['y'])))

        # add the directions of the stations
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

        self.number_of_trains = len(self.trains)
        # sum all train distances
        self.total_distance += train_distance
        self.train_distances.append(train_distance)


    def calculate_score(self):
        """Calculate the quality of the trajectories."""
        # determine variables for formula
        p = self.number_of_ridden_connections / self.number_of_connections
        T = self.number_of_trains
        Min = self.total_distance
        
        quality_score = p*10000 - (T*100 + Min)

        self.score = quality_score

        return quality_score


    def create_output(self, output_name):
        """Build an output csvfile with alle trajectory information."""
        csv_colums = ['train', 'stations']
        output_file = "results/" + output_name
        
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, fieldnames=csv_colums)
            writer.writeheader()
           
            # put every trajectory in the file
            for train in self.trains:
                writer.writerow(train)

            # end with the quality score
            output.write(f"score,{self.calculate_score()}")


    def determine_ridden_stations(self):
        ridden_stations = []
        
        for train in self.trains:
            for station in train["stations"]:
                ridden_stations.append(station)

        # remove duplicate ridden stations from the list
        ridden_stations = remove_duplicates(ridden_stations)

        return ridden_stations