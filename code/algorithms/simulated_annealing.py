import random
# import numpy as np
import math
import copy
from .hill_climber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that replaces the last or first station of a random train in a map with a random valid station.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """

    def __init__(self, stations_file, connections_file, max_number_of_trains, time_frame, temperature):
        # Use the init of the Hillclimber class
        super().__init__(stations_file, connections_file, max_number_of_trains, time_frame)
        
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        
        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def check_solution(self, new_map):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_score = new_map.calculate_score()
        old_score = self.score

        # Calculate the probability of accepting this new map
        # use np.float128 to prevent an overflow error
        delta = old_score - new_score
        try:
            probability = math.exp(-delta / self.T)
        except OverflowError:
            print(delta)
            print(old_score, new_score)
            print(self.T)
            exit("OverflowError")
        

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.map = new_map
            self.score = new_score
            # print(f"New high score: {new_score}")

        # Update the temperature
        self.update_temperature()
        