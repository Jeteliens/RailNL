import random
import copy
TIME_FRAME = 120

def randomise_train(map, number_of_trains):
    
    stations = map.stations
    
    trains = []
    train_distances = []
    # a list that contains the id's of the ridden connections
    ridden_connections = []
    # train id
    t_id = 1
    
    # create multiple trains
    for _ in range(number_of_trains):
        if len(ridden_connections) == map.number_of_connections:
            break
        
        number_of_stations = 21
        train = []
        train_distance = 0
        
        # randomly chose the start point
        station = random.choice(stations)
        
        train.append(station)

        # create a train
        for _ in range(number_of_stations):
            possible_next_stations = []
            
            # assure that no station is ridden more than once in a single trejectory
            for direction in station.directions:
                if direction[0] not in train:
                    possible_next_stations.append(direction)
            
            if possible_next_stations:
                next_station_data = random.choice(possible_next_stations)
            else:
                break

            # extract data of the next station
            next_station = next_station_data[0]
            distance_to_next_station = next_station_data[1]
            connection_id = next_station_data[2]
                    
            if train_distance + distance_to_next_station > TIME_FRAME:
                break

            train.append(next_station)
            ridden_connections.append(connection_id) 
            train_distance += distance_to_next_station

            station = next_station

        
        trains.append(train)
        train_distances.append(train_distance)

        # add train to the map
        train_id = f"train_{t_id}"
        train_distance = train_distances[t_id - 1]
        map.add_train(train_id, train, train_distance)
            
        t_id += 1

        # remove duplicated (ridden) connection ids from the list
        temp_list = [] 
        [temp_list.append(cnx_id) for cnx_id in ridden_connections if cnx_id not in temp_list]
        ridden_connections = temp_list

    # determine the number of ridden connections
    map.number_of_ridden_connections = len(ridden_connections)



# def random_assignment(map, possibilities):
#     for station in map.stations.values():
#         station.set_value(random.choice(possibilities))

# def random_reconfigure_station(map, station, possibilities):
#     station.set_value(random.choice(possibilities))

# def random_reconfigure_stations(map, stations, possibilities):
#     for station in stations:
#         random_reconfigure_station(map, station, possibilities)

# def random_reassignment(map, possibilities):
#     new_map = copy.deepcopy(map)

#     random_assignment(new_map, possibilities)

#     violating_stations = new_map.get_violations()

#     while len(violating_stations):
#         random_reconfigure_stations(new_map, violating_stations, possibilities)

#         violating_stations = new_map.get_violations()

#     return new_map