import random
import math
import copy
from .hill_climber import HillClimber


class SimulatedAnnealing(HillClimber):
    """Replaces a random station or a random train in a map.Each improvement
    or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.

    Attributes:
        stations_file: reference to the file with object information
        connections_file: reference to file with directions
        max_number_of_trains: maximum amount of trains in a map
        time_frame: maximum duration of a trajectory
        temperature: determines whether a change gets accepted
    """

    def __init__(self, stations_file, connections_file, max_number_of_trains, time_frame, temperature):
        # use the init of the HillClimber class
        super().__init__(stations_file, connections_file, max_number_of_trains, time_frame)
        
        self.T0 = temperature
        self.T = temperature
        self.best_map = copy.deepcopy(self.map)


    def update_temperature(self):
        """Implements a *linear* cooling scheme where temperature will 
        become zero if all iterations have passed to the run()method."""
        
        self.T = self.T - (self.T0 / self.iterations)

        # exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0


    def check_solution(self, new_map):
        """Checks and accepts better solutions than the current solution."""
        new_score = new_map.calculate_score()
        old_score = self.score

        # calculate the probability of accepting the new map
        delta = old_score - new_score
        try:
            probability = math.exp(-delta / self.T)
        # ensure the probability does not overflow
        except OverflowError:
            print(delta)
            print(old_score, new_score)
            print(self.T)
            exit("OverflowError")

        # pull a random number between 0 and 1 and accept score or not
        if random.random() < probability:
            self.map = new_map
            self.score = new_score
            # print(f"Current score: {self.score}")

        if new_score >= self.best_map.calculate_score():
            self.best_map = new_map

        self.update_temperature()
        