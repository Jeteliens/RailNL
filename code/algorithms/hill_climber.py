from .randomise2 import Randomise
import csv

class HillClimber:
    """
    The HillClimber class that iterates through the trains in a map and replaces each train with a random train. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, map):
        self.map = map
        self.original_map = map


        # trains = [{'train': 'train_1', 'stations': [Helmond, Eindhoven, Tilburg, Breda, Etten-Leur, Roosendaal, Vlissingen]}]
    
    def run(self, number_of_runs):
        old_score = self.map.score
        
        for i in range(number_of_runs):
            for trajectory in self.map.trains:
                randomise = Randomise(self.map)
                new_train_data = randomise.create_train()

                old_train = trajectory['stations']
                new_train = new_train_data['train']
                trajectory['stations'] = new_train

                old_train_distance = self.map.train_distances[i]
                new_train_distance = new_train_data['train_distance']
                self.map.total_distance = self.map.total_distance + new_train_distance - old_train_distance

                # remove the ridden connections in the old train from the list
                for cnx_id in self.determine_ridden_connections(old_train):
                    self.map.all_ridden_connections.remove(cnx_id)
                
                # add the ridden connections in the new train to the list
                # print(self.determine_ridden_connections(new_train))
                self.map.all_ridden_connections += self.determine_ridden_connections(new_train)

                self.map.ridden_connections = self.remove_duplicates(self.map.all_ridden_connections)

                # print(self.map.all_ridden_connections)
                self.map.number_of_ridden_connections = len(self.map.all_ridden_connections)

                new_score = self.map.calculate_score()

                if new_score < old_score:
                    self.map = self.original_map

        return self.map

    def determine_ridden_connections(self, train):

        # print(train)

        ridden_connections = []
        
        connections_list = []
        for n in range(len(train) - 1):
            connection = train[n:n+2]
            # print(connection)
            connections_list.append(connection)

        # print("=====================")

        # print(connections_list)

        with open(self.map.connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for connection in connections_list:

                connection_id = 0
                for row in reader:
                    connection_id += 1
                    # print(f"row['station1']: {row['station1']}")
                    # print(f"connection[0]: {connection[0]}")
                    if row['station1'] == connection[0].name and row['station2'] == connection[1].name:
                        # print("condition 1 is met")
                        ridden_connections.append(connection_id)
                        # break
                    elif row['station2'] == connection[0].name and row['station1'] == connection[1].name:
                        # print("condition 2 is met")
                        ridden_connections.append(connection_id)
                        # break

        print(f"Ridden connections: {ridden_connections}")
        print("================")
        return ridden_connections

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list