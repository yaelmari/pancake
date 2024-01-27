def base_heuristic(_pancake_state):
    state_str = _pancake_state.get_state_str()
    pancake_list = state_str.split(',')

    # This variable will count from which level the pancakes aren't where they should be
    count = len(pancake_list)
    # Initialize a boolean flag to track if the pancake stack is valid
    valid = True
    for i in range(len(pancake_list)):
        value = int(pancake_list[i])
        expected_location = len(pancake_list) - i
        # Check if the pancake is not in its expected location and the stack is still valid
        if value != expected_location and valid:
            count = i
            # Set the flag to indicate that the stack is no longer valid
            valid = False

    # Sum the values of the pancakes to get the heuristic value
    heuristic = 0
    for n in range(count, len(pancake_list)):
        heuristic += int(pancake_list[n])

    return heuristic


def advanced_heuristic(_pancake_state):
    pancake_list = _pancake_state.stateAsInts

    # Find the first misplaced pancake from the start
    count_from_start = len(pancake_list)
    for i in range(len(pancake_list)):
        value = pancake_list[i]
        expected_location = len(pancake_list) - i
        if value != expected_location:
            # Update the count indicating the number of misplaced pancakes from the start and exit the loop
            count_from_start = i
            break

    # Find the first misplaced pancake from the end
    count_from_end = 0
    expected_location = 1
    for i in range(len(pancake_list) - 1, count_from_start, -1):
        value = pancake_list[i]
        if value != expected_location:
            # Update the count indicating the number of misplaced pancakes from the end and exit the loop
            count_from_end = i
            break
        expected_location += 1

    #  Calculate the heuristic value by summing the values of the misplaced pancakes
    heuristic = 0
    for n in range(count_from_start, count_from_end + 1):
        heuristic += int(pancake_list[n])

    return heuristic
