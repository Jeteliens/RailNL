import random
import copy

def randomise_train(test_map, number_of_trains):
    list_of_stations = test_map.stations
    number_of_stations = random.randint(1,22)
    train = []
    start_point = random.choice(list_of_stations)
    
    station = start_point
    train.append(station)
    
    print(start_point)

    for number in range(number_of_stations - 1):
        print(station)
        next_station = random.choice(station.directions)[0]
        train.append(next_station)
        station = next_station

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