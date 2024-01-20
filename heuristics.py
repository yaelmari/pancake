def base_heuristic(_pancake_state):
    state_str = _pancake_state.get_state_str()
    pancake_list = state_str.split(',')

    # This variable will count from which level the pancakes aren't where they should be
    count = len(pancake_list)
    for i in range(len(pancake_list)):
        value = int(pancake_list[i])
        expected_location = len(pancake_list) - i
        if value != expected_location:
            count = i
            break

    # Sum the values of the pancakes to get the heuristic value
    heuristic = 0
    for n in range(count, len(pancake_list)):
        heuristic += int(pancake_list[n])

    return heuristic


def advanced_heuristic(_pancake_state):
    return 0
