import csv
from .station import Station

class Kaart():
    def __init__(self, stations_file):
        self.trains = [{"train": 'train_1', "station": "[AmsterdamZuid,Haarlem]"}, {"train": 'train_2', "station": "[Alkmaar,Hoorn]"}]
        self.number_of_trains = 0
        self.stations = self.load_stations(stations_file)
        self.total_distance = 0

    def load_stations(self, stations_file):
        
        stations = []
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
        
            for row in reader:
                stations.append(Station(row['station'], float(row['x']), float(row['y'])))
    
        return stations
    
    def add_train(self, train_id, train_trajectory, train_distance):
        train_1
        self.trains[train_id] = train_trajectory
        self.number_of_trains += 1
        self.total_distance += train_distance

    def calculate_score(self):
               
        ridden_stations = 0
        total_stations = 0
        
        for station in self.stations:
            if station.times_visited > 0:
                ridden_stations += 1
            
            total_stations += 1

        p = ridden_stations / total_stations
        T = self.number_of_trains
        Min = self.total_distance
        
        quality_score = p*10000 - (T*100 + Min)

        return quality_score

    def create_output(self):
        csv_colums = ['train', 'stations']
        output_file = "Trajectories.csv"
        
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, fieldnames=csv_colums)
            writer.writeheader()
           
            for train in self.trains:
                writer.writerow(train)

            output.write(f"score,{self.calculate_score()}")