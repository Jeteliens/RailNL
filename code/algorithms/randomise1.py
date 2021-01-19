import random
import copy
# time_frame = 120

def randomise(map, number_of_trains, time_frame):
    
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
        
        number_of_stations = len(stations) - 1
        train = []
        train_distance = 0
        
        # randomly choose the start point
        station = random.choice(stations)
        
        train.append(station)

        # create a train
        for _ in range(number_of_stations):
            possible_next_stations = []
            
            # assure that no station is ridden more than once in a single trejectory
            for direction in station.directions:
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
    # print(map.number_of_ridden_connections)
