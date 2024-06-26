class search_node:
    def __init__(self, state, g=0, h=0, prev=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.prev = prev

    def __eq__(self, other):
        return self.state.state_str == other.state.state_str

    def __lt__(self, other):
        if self.f < other.f:
            return True
        elif self.f == other.f and self.h < other.h:
            return True
        return False

    def get_neighbors(self):
        return self.state.get_neighbors()

    def __hash__(self):
        return hash(self.state.state_str)

