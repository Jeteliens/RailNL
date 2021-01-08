from code.classes.map import Map
from code.classes.station import Station

if __name__ == '__main__':
    
    stations_file = "data/Holland/StationsHolland.csv"
    connections_file = "data/Holland/ConnectiesHolland.csv"
    
    test_map = Map(stations_file)
    
    for station in test_map.stations:
        station.add_directions(connections_file)
    
    test_map.create_output()

    # print(test_map.stations)
    # print("\n")
    # print(test_map.stations[1].x_position)
    # print(test_map.stations[1].y_position)