from search_node import search_node
import queue


class OpenList:
    def __init__(self):
        self.dic = {}
        self.lst = queue.PriorityQueue()

    def getMap(self):
        return self.dic

    def getLst(self):
        return self.lst

    def isNotEmpty(self):
        return self.lst != []


def create_open_set():
    return OpenList()


def create_closed_set():
    return {}


def add_to_open(vn, open_set):
    open_set.getLst().put(vn)
    open_set.getMap()[vn.state.state_str] = [vn.g, vn]


def open_not_empty(open_set):
    return open_set.isNotEmpty()


def get_best(open_set):
    value = open_set.getLst().get()
    dic = open_set.getMap()
    # Loop until a value with a corresponding state is found in the dictionary
    while dic.get(value.state.state_str) is None:
        # Get the next value from the list
        value = open_set.getLst().get()

    # Remove the state from the dictionary
    open_set.getMap().pop(value.state.state_str)
    return value


def add_to_closed(vn, closed_set):
    closed_set[vn.state.state_str] = vn.g


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    # Get the dictionary and list from the open set
    dic, lst = open_set.getMap(), open_set.getLst()
    # If the state is in the dictionary, check if the new path to this state is shorter
    if vn.state.state_str in dic:
        if vn.g < dic.get(vn.state.state_str)[0]:
            # If the new path is shorter, remove the old entry from the dictionary
            dic.pop(vn.state.state_str)
            return False
        return True
    return False


# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    if vn.state.state_str in closed_set:
        # If the state is in the closed set, check if the new path to this state is shorter
        if vn.g < closed_set.get(vn.state.state_str):
            # If the new path is shorter, remove the old entry from the closed set
            closed_set.pop(vn.state.state_str)
            return False
        return True
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None
