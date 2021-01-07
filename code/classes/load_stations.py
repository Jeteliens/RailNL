def load_stations(self, source_file):
        
    stations = {}
    with open(source_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        
        for row in reader:
            stations[row['station']] = Station(row['station'], row['x'], row['y'])
    
    return stations