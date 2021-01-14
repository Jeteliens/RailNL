import random
import copy
TIME_FRAME = 120

def randomise_train(test_map, number_of_trains):
    
    list_of_stations = test_map.stations
    
    trains_data = []
    trains = []
    train_distances = []
    ridden_connections = []
    
    for i in range(number_of_trains - 1):
        number_of_stations = random.randint(2,22)
        train = []
        train_distance = 0
        start_point = random.choice(list_of_stations)
        
        station = start_point
        train.append(station)
        
        # print(start_point)
        # print(start_point.directions)

        for j in range(number_of_stations - 1):
            # print(station)

            station.set_visited()
            possible_next_stations = []
            
            for direction in station.directions:
                # print(direction)
                if direction[0] not in train:
                    possible_next_stations.append(direction)
            
            if possible_next_stations:
                next_station_data = random.choice(possible_next_stations)
            else:
                break

            # print(next_station_data)
            next_station = next_station_data[0]
            # print(next_station)
                    
            if train_distance + next_station_data[1] > TIME_FRAME:
                break

            connection_id = next_station_data[2]
            # print(f"[{station}, {next_station}]")
            ridden_connections.append(connection_id) 

            train_distance += next_station_data[1]
            # print(train_distance)
            train.append(next_station)
            station = next_station
        
        trains.append(train)
        train_distances.append(train_distance)

    # print(trains)
    trains_data.append(trains)
    # print(train_distances)
    trains_data.append(train_distances)

    elimin = [] 
    [elimin.append(cnx_id) for cnx_id in ridden_connections if cnx_id not in elimin]
    test_map.number_of_ridden_connections = len(elimin)
    
    # print(ridden_connections)
    # print(elimin)
    # print(trains_data[1])
    return trains_data

    # map.add_train(train_id, train, train_distance)  



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