import csv
from . import Station

class Train():
    def __init__(self, trajectory):
        self.stations = trajectory

    def load_stations(self, trajectory):
        trajectory = []

        return trajectory