from .randomise2 import Randomise
import csv

class HillClimber:
    """
    The HillClimber class that iterates through the trains in a map and replaces each train with a random train. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, map):
        self.map = map
        self.old_map = None
        self.best_map = None


        # trains = [{'train': 'train_1', 'stations': [Helmond, Eindhoven, Tilburg, Breda, Etten-Leur, Roosendaal, Vlissingen]}]
    
    def run(self, number_of_runs):
        # old_score = self.map.score
        
        # print(self.map.all_ridden_connections)

        for i in range(number_of_runs):
            # print(self.map.all_ridden_connections)
            
            n = 0
            # print(self.map.trains)
            for trajectory in self.map.trains:
                old_score = self.map.calculate_score()
                # print(f"Old score: {old_score}")
                randomise = Randomise(self.map)
                new_train_data = randomise.create_train()
                # print(new_train_data)

                old_train = trajectory['stations']
                # print(f"Old train: {old_train}", end="")
                new_train = new_train_data['train']
                new_train_distance = new_train_data['train_distance']
                # print(f"New train: {new_train}")
                trajectory['stations'] = new_train
                old_train_distance = self.map.train_distances[n]
                self.map.train_distances[n] = new_train_distance

                # print(self.map.train_distances)
                
                # print(f" ==> Old train distance: {old_train_distance}")
                # new_train_distance = new_train_data['train_distance']
                self.map.total_distance = self.map.total_distance + new_train_distance - old_train_distance

                # remove the ridden connections in the old train from the list
                ridden_connections_old_train = self.determine_ridden_connections(old_train)
                # print(f"ridden_connections_old_train: {ridden_connections_old_train}")
                # if i == 0:
                #     print(f"Before removing: {self.map.all_ridden_connections}")
                for cnx_id in ridden_connections_old_train:
                    # if cnx_id in self.map.all_ridden_connections:
                    self.map.all_ridden_connections.remove(cnx_id)
                # if i == 0:
                #     print(f"After removing: {self.map.all_ridden_connections}")
                
                # add the ridden connections in the new train to the list
                # print(f"New Train: {new_train}")
                # print(f"{self.determine_ridden_connections(new_train)}")
                # print(self.map.all_ridden_connections)
                self.map.all_ridden_connections += self.determine_ridden_connections(new_train)

                # if i == 0:
                #     print(f"Before: {self.map.ridden_connections}")
                self.map.ridden_connections = self.remove_duplicates(self.map.all_ridden_connections)
                # if i == 0:
                #     print(f"After: {self.map.ridden_connections}")

                # print(self.map.all_ridden_connections)
                self.map.number_of_ridden_connections = len(self.map.ridden_connections)
                # print(f"Number of ridden connections: {self.map.number_of_ridden_connections}")

                new_score = self.map.calculate_score()

                # if new_score > old_score:
                #     self.best_map = self.map
                
                # if new_score < old_score:
                #     # self.best_map = self.old_map
                #     self.map = self.old_map
                # else:
                #     self.best_map = self.map
                #     self.old_map = self.map
                
                if new_score > old_score:
                    self.best_map = self.map
                    # self.old_map = self.map
                else:
                    self.map = self.best_map

                n += 1

        return self.best_map

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

        for connection in connections_list:
            with open(self.map.connections_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                connection_id = 0
                for row in reader:
                    connection_id += 1
                    # print(f"{connection_id}" , end="")
                    # print(f"row['station1']: {row['station1']} / row['station2']: {row['station2']} || ", end="")
                    # print(f"connection[0]: {connection[0]} / connection[1]: {connection[1]}")
                    # print(f"connection[0]: {connection[0]}")
                    if row['station1'] == connection[0].name and row['station2'] == connection[1].name:
                        # print("condition 1 is met")
                        ridden_connections.append(connection_id)
                        # break
                    elif row['station2'] == connection[0].name and row['station1'] == connection[1].name:
                        # print("condition 2 is met")
                        ridden_connections.append(connection_id)
                        # break
                    # else:
                    #     print("No condition met")
                
                # print(f"Ridden connections: {ridden_connections}")
                # print("---------------")

        # print(f"Ridden connections: {ridden_connections}")
        # print("===========================================")
        return ridden_connections

    def remove_duplicates(self, input_list):
        """Removes duplicated elements from a list"""
        
        temp_list = [] 
        [temp_list.append(element) for element in input_list if element not in temp_list]
        return temp_list