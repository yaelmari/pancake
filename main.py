import heuristics
from search import search
from pancake_state import pancake_state
from heuristics import *
import time

if __name__ == '__main__':
    # goal_state = "7,6,5,4,3,2,1"
    # pancake_input = "3,5,6,4,2,7,1,8"
    # goal_state = "8,7,6,5,4,3,2,1"
    # pancake_input ="7,2,6,4,3,9,5,1,8"
    goal_state = "9,8,7,6,5,4,3,2,1"
    pancake_input = "5,9,1,8,2,7,3,6,4"
    # pancake_input = "1,4,6,2,3,5"
    # goal_state = "6,4,5,3,2,1"
    # pancake_input = "8,7,6,5,4,2,1,3"

    #
    # pancake_input = "12,3,6,8,2,9,15,5,1,11,4,14,10,7,16,13"
    # goal_state = "16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1"
    # pancake_input = "27,7,19,16,8,5,2,22,14,3,11,6,21,10,18,15,4,26,20,13,12,1,9,23,17,25,24"
    # goal_state = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27"[::-1]
    # # pancake_input = "7,19,26,16,8,5,2,22,14,28,3,23,11,6,21,10,18,25,15,4,20,30,13,12,29,24,1,9,27,17"
    #
    # goal_state = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30"
    # pancake_input = "2,4,1,3,5"
    # goal_state = "5,4,3,2,1"

    start_time = time.time()

    pancake_state = pancake_state(pancake_input)
    print(advanced_heuristic(pancake_state))

    # pancake_state = pancake_state(pancake_input)
    temp = pancake_state
    # while temp.
    # tuple_list = pancake_state.get_neighbors()
    # print(tuple_list)
    heuristic = heuristics.advanced_heuristic(pancake_state)

    # print(heuristic)
    search_result = search(pancake_state, advanced_heuristic, goal_state)
    end_time = time.time()
    x =0
    for i in search_result:
        print("stage: " + str(x))
        print(i.state.state_str)
        # print("H: "+str(i.h))
        print("G: "+str(i.g))
        # print("F: " + str(i.f))
        x+=1
        print("_____________________")

    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")
