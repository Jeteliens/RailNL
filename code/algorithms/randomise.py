import random
import copy

def random_assignment(map, possibilities):
    for station in map.stations.values():
        station.set_value(random.choice(possibilities))

def random_reconfigure_station(map, station, possibilities):
    station.set_value(random.choice(possibilities))

def random_reconfigure_stations(map, stations, possibilities):
    for station in stations:
        random_reconfigure_station(map, station, possibilities)

def random_reassignment(map, possibilities):
    new_map = copy.deepcopy(map)

    random_assignment(new_map, possibilities)

    violating_stations = new_map.get_violations()

    while len(violating_stations):
        random_reconfigure_stations(new_map, violating_stations, possibilities)

        violating_stations = new_map.get_violations()

    return new_map