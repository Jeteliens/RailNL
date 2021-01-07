import csv

class Station():
    def __init__(self, name, x, y):
        self.directions = self.add_directions(source_file)
        self.name = name
        self.x_position = x
        self.y_position = y

    def load_station(self, source_file):
        
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['station'], row['x'], row['y'])


    def add_directions(self, source_file):
        
        directions = []
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                if row['station1'] == self.name:
                    directions.append([row['station2'], row['distance']])
                elif row['station2'] == self.name:
                    directions.append([row['station1'], row['distance']])

        return directions