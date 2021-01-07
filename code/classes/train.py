import csv
from . import Station

class Train():
    def __init__(self, trajectory):
        self.stations = trajectory

    # def load_stations(self, trajectory):
    #     trajectory = []

    #     return trajectory
    
    def load_station(self, source_file):
        
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['station'], row['x'], row['y'])