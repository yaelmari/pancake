class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        # you may add data structures to improve the search

    # returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    # (pancake _state2, cost2)...]
    def get_neighbors(self):
        pancake_list = self.state_str.split(',')
        neighbors = []

        # Iterate through each level and flip the pancakes
        for i in range(1, len(pancake_list)):
            # Create a copy of the original list to avoid modifying it
            new_neighbor_list = pancake_list.copy()

            # flip the pancakes
            for p in range(0, i + 1):
                new_neighbor_list[p] = pancake_list[i - p]

            # Convert the list back to a string and append the cost that will always be 1
            neighbors.append(((','.join(new_neighbor_list)), 1))

        return neighbors

    # you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    # you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str
