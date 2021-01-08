import csv
from .station import Station

class Map():
    def __init__(self, stations_file):
        self.trains = None
        self.stations = self.load_stations(stations_file)

    def load_stations(self, stations_file):
        
        stations = []
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
        
            for row in reader:
                stations.append(Station(row['station'], float(row['x']), float(row['y'])))
    
        return stations
    
    def create_train(self, train):
        trains = []
        trains.append(train)

    def add_visited(self):
        pass

    def remove_visited(self):
        pass

    def calculate_score(self):
        pass

    def create_output(self):
        return file
        