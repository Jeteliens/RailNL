import csv


class Station:
    """State the connections every train station has.

    Read the connections information.
    Make a list for every object with matching connections information.

    Attributes:
        name: name of the object
        x: x coordinate of the object
        y: y coordinate of the object
        connections_file: reference to file with directions
        stations_list: reference to list with object information
    """

    def __init__(self, name, x, y):
        self.directions = []
        self.name = name
        self.x_position = x
        self.y_position = y


    def add_directions(self, connections_file, stations_list):
        """Organize the object with the connections it has."""

        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            connection_id = 0

            # add the right connections to the object
            for row in reader:
                # give every object an id
                connection_id += 1
                if row['station1'] == self.name:
                    self.directions.append([row['station2'], float(row['distance']), connection_id])
                elif row['station2'] == self.name:
                    self.directions.append([row['station1'], float(row['distance']), connection_id])

        # connect station to directions
        for direction in self.directions:
            for station in stations_list:
                if direction[0] == station.name:
                    direction[0] = station


    def __repr__(self):
        """Properly print the object if it is in a list or dict."""
        return self.name