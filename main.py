import heuristics
from search import search
from pancake_state import pancake_state
from heuristics import *

if __name__ == '__main__':
    goal_state = "4,3,2,1"
    # pancake_input = "4,2,3,1"
    pancake_input = "4,3,2,1"
    # pancake_input = "7,6,4,5,1,2,3"
    pancake_state = pancake_state(pancake_input)
    # tuple_list = pancake_state.get_neighbors()
    # print(tuple_list)
    heuristic = heuristics.base_heuristic(pancake_state)
    print(heuristic)
    # search_result = search(pancake_state, base_heuristic, goal_state)
