from .randomise2 import Randomise
import csv
import copy

class HillClimber:
    """
    The HillClimber class that iterates through the trains in a map and replaces each train with a random train. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, map):
        self.map = copy.deepcopy(map)
        self.best_map = copy.deepcopy(map)
    
    def run(self, number_of_runs):

        # trains = [{'train': 'train_1', 'stations': [Helmond, Eindhoven, Tilburg, Breda, Etten-Leur, Roosendaal, Vlissingen]}]
        for i in range(number_of_runs):          
            n = 0

            print(self.map.trains)
            for trajectory in self.map.trains:
                old_score = self.map.calculate_score()
                randomise = Randomise(self.map)
                new_train_data = randomise.create_train()

                old_train = trajectory['stations']
                new_train = new_train_data['train']
                new_train_distance = new_train_data['train_distance']
                trajectory['stations'] = new_train
                old_train_distance = self.map.train_distances[n]
                self.map.train_distances[n] = new_train_distance

                self.map.total_distance = self.map.total_distance + new_train_distance - old_train_distance

                ridden_connections_old_train = self.determine_ridden_connections(old_train)

                self.map.all_ridden_connections += self.determine_ridden_connections(new_train)
        
                # print(f"Old train connections: {ridden_connections_old_train}")
                # print(f"All ridden connections: {self.map.all_ridden_connections}")
                # print(i)
                for cnx_id in ridden_connections_old_train:
                    self.map.all_ridden_connections.remove(cnx_id)
                    
                self.map.ridden_connections = self.remove_duplicates(self.map.all_ridden_connections)

                self.map.number_of_ridden_connections = len(self.map.ridden_connections)

                new_score = self.map.calculate_score()

                if new_score > old_score:
                    self.best_map = copy.deepcopy(self.map)
                    print(f"New high score: {new_score}")
                else:
                    self.map = copy.deepcopy(self.best_map)

                n += 1

        return self.best_map

    def determine_ridden_connections(self, train):

        ridden_connections = []
        
        connections_list = []
        for n in range(len(train) - 1):
            connection = train[n:n+2]
            connections_list.append(connection)

        for connection in connections_list:
            with open(self.map.connections_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                connection_id = 0
                for row in reader:
                    connection_id += 1

                    if row['station1'] == connection[0].name and row['station2'] == connection[1].name:
                        ridden_connections.append(connection_id)
                    elif row['station2'] == connection[0].name and row['station1'] == connection[1].name:
                        ridden_connections.append(connection_id)

        return ridden_connections

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list