import csv
from .station import Station

class Kaart():
    
    def __init__(self, stations_file):
        
        # self.trains = [{"train": 'train_1', "stations": "[AmsterdamZuid,Haarlem]"}, {"train": 'train_2', "stations": "[Alkmaar,Hoorn]"}]
        self.trains = []
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
        
        trajectory = {}
        trajectory["train"] = train_id
        trajectory["stations"] = train_trajectory
        self.trains.append(trajectory)

        self.number_of_trains += 1
        self.total_distance += train_distance

    def calculate_score(self):
               
        total_stations = len(self.stations)
        ridden_stations = 0
       
        for station in self.stations:
            # print("Loop entered")
            print(f"Times visited: {station.times_visited}")
            if station.times_visited > 0:
                ridden_stations += 1

        p = ridden_stations / total_stations
        print(f"ridden_stations:{ridden_stations}")
        print(f"p:{p}")
        T = self.number_of_trains
        print(f"T:{T}")
        Min = self.total_distance
        print(f"Min:{Min}")
        
        quality_score = p*10000 - (T*100 + Min)

        return quality_score

    def create_output(self):
        
        csv_colums = ['train', 'stations']
        output_file = "output.csv"
        
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, fieldnames=csv_colums)
            writer.writeheader()
           
            for train in self.trains:
                # print(train)
                writer.writerow(train)

            output.write(f"score,{self.calculate_score()}")