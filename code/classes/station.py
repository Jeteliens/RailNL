import csv

class Station():
    def __init__(self, name, x, y):
        self.directions = []
        self.name = name
        self.x_position = x
        self.y_position = y

    def add_directions(self, connections_file):
        
        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                if row['station1'] == self.name:
                    self.directions.append([row['station2'], int(row['distance'])])
                elif row['station2'] == self.name:
                    self.directions.append([row['station1'], int(row['distance'])])

    def __repr__(self):
        return self.name