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


# def advanced_heuristic(_pancake_state):
#     # return 0
#     state_str = _pancake_state.get_state_str()
#     pancake_list = state_str.split(',')
#     count = len(pancake_list)
#     h = 0
#     for i in range(count-1):
#         if abs(int(pancake_list[i]) - int(pancake_list[i+1])) > 1:
#             h += 1
#
#     return h


def advanced_heuristic(_pancake_state):
    pancake_list = _pancake_state.getStateAsInts()
    total_count = 0

    for i in range(len(pancake_list)):
        current_number = pancake_list[i]
        count_greater = sum(num for num in pancake_list[i + 1:] if num > current_number)
        total_count += count_greater

    return total_count

