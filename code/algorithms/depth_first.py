class DepthFirst:

    def __init__(self):
        self.map
        self.trains
        self.stations
        
        self.best_map
    
    
    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.stations:
            new_graph = self.get_next_station()

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()

            if node is not None:
                self.build_children(new_graph, node)
            else:
                # Stop if we find a solution
                # break

                # or ontinue looking for better graph
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution