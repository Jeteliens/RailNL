class DepthFirst:

    def __init__(self, stations):
        self.stations = stations
        self.random_trains = {}
    

    def make_random_trains(self):
        for station in self.stations:
            self.random_trains[station] = 

    def randomise(self, start_station, number_of_trains):
        
        trains = []
        
        for _ in range(number_of_trains):
            train = []
            train.append(start_station)
            
            number_of_stations = len(self.stations)
            # train = []
            train_distance = 0
            
            # randomly chose the start point
            # station = random.choice(stations)
            
            # train.append(station)

            # create a train
            for _ in range(number_of_stations):
                possible_next_stations = []
                
                # assure that no station is ridden more than once in a single trejectory
                for direction in start_station.directions:
                    if direction[0] not in train:
                        # if direction[2] not in ridden_connections:
                        possible_next_stations.append(direction)
                
                    # possible_next_stations.append(direction)

                if possible_next_stations:
                    next_station_data = random.choice(possible_next_stations)
                else:
                    break

                # extract data of the next station
                next_station = next_station_data[0]
                distance_to_next_station = next_station_data[1]
                connection_id = next_station_data[2]
                        
                if train_distance + distance_to_next_station > time_frame:
                    break

                train.append(next_station)
                ridden_connections.append(connection_id) 
                train_distance += distance_to_next_station

                station = next_station

            
            trains.append(train)
            train_distances.append(train_distance)

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.stations:
            new_graph = self.get_next_station()

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()

            if node is not None:
                self.build_children(new_graph, node)
            else:
                # Stop if we find a solution
                # break

                # or ontinue looking for better graph
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution