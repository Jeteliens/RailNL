import random
import math
from code.classes.map import Map

class SimulatedAnnealing():
    """
    The SimulatedAnnealing class that replaces the last or first station of a random train in a map with a random valid station.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """

    def __init__(self, stations_file, connections_file  max_number_of_trains, time_frame, temperature):
        self.station_file = stations_file
        self.connections_file = connections_file
        self.max_number_of_trains = max_number_of_trains
        self.time_frame = time_frame
        self.map = create_random_map(stations_file, connections_file)
        self.T0 = temperature
        self.T = temperature
        self.score = self.map.calculate_score()

    def create_random_map(self, stations_file, connections_file):
        random_map = Map(stations_file, connections_file)

        randomise = Randomise(random_map)
        randomise.run(self.max_number_of_trains, self.time_frame)
        random_map = randomise.map

        return random_map

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

    def make_small_change(self, map):
        trajectory = random.choice(map.trains)
        trajectory['stations']

        # make small change to the chosen train

    def check_solution(self, new_map):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        old_score = self.old_score
        new_score = new_map.calculate_score()
        
        # Calculate the probability of accepting this new map
        delta = new_score - old_score
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.map = new_map
            self.score = new_score

        # Update the temperature
        self.update_temperature()
        

    def run(self, iterations):
        self.iterations = iterations

        random_map = self.create_random_map()
        
        for iteration in range(iterations):
            random_map.make_small_change()
            self.check_solution(random_map)

        return self.map
