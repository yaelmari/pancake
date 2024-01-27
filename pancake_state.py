class pancake_state:

    def __init__(self, state_str, flip_index=-1):
        if isinstance(state_str, str):
            self.state_str = state_str
            self.stateAsInts = list(map(int, state_str.split(',')))
            self.flip_index = flip_index

    # returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    # (pancake _state2, cost2)...]
    def get_neighbors(self):
        pancake_list = self.getStateAsInts()
        curr_flip_index = self.flip_index
        neighbors = []

        count = 0
        # Find the number of pancakes at the bottom of the stack that are already in the correct position
        while count < len(pancake_list) and pancake_list[count] == (len(pancake_list) - count):
            count += 1

        # Generate neighbors by flipping pancakes
        for i in range(count, len(pancake_list) - 1):
            # Skip flipping the pancake at the current flip index
            if i == curr_flip_index:
                continue
            bottom = pancake_list[:i]
            top = pancake_list[i:][::-1]
            bottom.extend(top)
            # Create a new pancake state with the flipped pancake stack and calculate its heuristic value
            neighbors.append((pancake_state(",".join(map(str, bottom)), i), sum(top)))
        return neighbors

    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str

    def getStateAsInts(self):
        return self.stateAsInts
