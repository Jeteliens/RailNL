import csv

class Station():
    def __init__(self, name, x, y):
        self.directions = []
        self.name = name
        self.x_position = x
        self.y_position = y
        self.times_visited = 0

    def add_directions(self, connections_file, stations_list):
        
        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            connection_id = 0

            for row in reader:
                connection_id += 1
                if row['station1'] == self.name:
                    self.directions.append([row['station2'], int(row['distance']), connection_id])
                elif row['station2'] == self.name:
                    self.directions.append([row['station1'], int(row['distance']), connection_id])

        for direction in self.directions:
            for station in stations_list:
                if direction[0] == station.name:
                    direction[0] = station

    def set_visited(self):
        self.times_visited += 1

    def __repr__(self):
        return self.name