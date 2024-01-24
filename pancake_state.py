class pancake_state:


    def __init__(self, state_str, flip_index=-1):
        if isinstance(state_str, str):
            self.state_str = state_str
            self.stateAsInts = list(map(int,state_str.split(',') ))
            self.flip_index = flip_index


        # you may add data structures to improve the search

    # returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    # (pancake _state2, cost2)...]
    def get_neighbors(self):
        # #******** YEAL'S **********************
        # pancake_list = self.state_str.split(',')
        # neighbors = []

        #     # Iterate through each level and flip the pancakes
        #     for i in range(1, len(pancake_list) - 1):
        #         # Create a copy of the original list to avoid modifying it
        #         new_neighbor_list = pancake_list.copy()
        #
        #         # flip the pancakes
        #         # for p in range(0, i + 1):
        #         temp_for_flip = len(pancake_list) - 1
        #         for p in range(i, len(pancake_list)):
        #             new_neighbor_list[p] = pancake_list[temp_for_flip]
        #             temp_for_flip -= 1
        #
        #         # Convert the list back to a string and append the cost that will always be 1
        #         neighbors.append((pancake_state(','.join(new_neighbor_list)),1))
        #
        #     return neighbors

        # ***** FReshie **********
        pancake_list = self.getStateAsInts()
        neighbors = []
        for i in range(0,len(pancake_list)-1):
            bottom = pancake_list[:i]
            top = pancake_list[i:][::-1]
            bottom.extend(top)
            # print(','.join(bottom))
            neighbors.append((pancake_state(",".join(map(str, bottom))),sum(top)))
        return neighbors

        # pancake_list = self.getStateAsInts()
        # curr_flip_index = self.flip_index
        # neighbors = []
        #
        # count = 0
        # # find
        # while count < len(pancake_list) and pancake_list[count] == (len(pancake_list) - count):
        #     count += 1
        #
        # for i in range(count, len(pancake_list) - 1):
        #     if i == curr_flip_index:
        #         continue
        #     bottom = pancake_list[:i]
        #     top = pancake_list[i:][::-1]
        #     bottom.extend(top)
        #     # print(','.join(bottom))
        #     neighbors.append((pancake_state(",".join(map(str, bottom)), i), sum(top)))
        # return neighbors

    # you can change the body of the function if you want
    def __hash__(self):
        return self.myHash

    # you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str

    def getStateAsInts(self):
        return self.stateAsInts

#
# n = pancake_state( "8,7,6,5,4,3,2,1")
# n.get_neighbors()
