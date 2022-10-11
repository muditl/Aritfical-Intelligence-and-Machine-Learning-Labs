import numpy as np

puzzles = [np.array([[1, 3, 0], [4, 2, 5], [8, 7, 6]]), np.array([[1, 3, 0], [4, 2, 5], [7, 8, 6]])]
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


def generate_puzzle():
    arr = np.zeros((3, 3), int)
    positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    fill = 1
    while fill < 9:
        num = np.random.randint(0, 9)
        while arr[positions[num][0], positions[num][1]] != 0:
            num = np.random.randint(0, 9)
        arr[positions[num][0], positions[num][1]] = fill
        fill += 1
    return arr


def calculate_inversion(unsolved):
    # convert to 1D array
    array = unsolved.flatten()
    # remove 0
    array = array[array != 0]
    total = 0
    # for all elements
    for i in range(len(array)):
        count = 0
        # count how many elements in after of it should not be after of it
        for j in range(i, len(array)):
            if array[j] < array[i]:
                count += 1
        total += count
    return total


# calculate manhattan distance as heuristc
def heuristic(current_state, final_state):
    total = 0
    for x in range(3):
        for y in range(3):
            # for all numbers
            # except 0
            if current_state[x][y] != 0:
                cur = current_state[x][y]
                # find where it should be
                target_x, target_y = np.where(final_state == cur)
                # find manhattan distance and add to total
                total += np.abs(target_y - y) + np.abs(target_x - x)
    return total


def get_moves(state):
    zero_x, zero_y = np.where(state == 0)
    if zero_x == 0 and zero_y == 0:
        return [(0, 1), (1, 0)]
    if zero_x == 0 and zero_y == 1:
        return [(1, 0), (0, 1), (0, -1)]
    if zero_x == 0 and zero_y == 2:
        return [(1, 0), (0, -1)]
    if zero_x == 1 and zero_y == 0:
        return [(1, 0), (-1, 0), (0, 1)]
    if zero_x == 1 and zero_y == 1:
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if zero_x == 1 and zero_y == 2:
        return [(1, 0), (-1, 0), (0, -1)]
    if zero_x == 2 and zero_y == 0:
        return [(-1, 0), (0, 1)]
    if zero_x == 2 and zero_y == 1:
        return [(-1, 0), (0, 1), (0, -1)]
    if zero_x == 2 and zero_y == 2:
        return [(-1, 0), (0, -1)]


def solve_eight_puzzle(current_state, final_state):
    solution = solver_runner(current_state, final_state)
    if solution:
        print_solution(puzzle, solution, goal_state)


def solver_runner(current_state, final_state):
    if calculate_inversion(current_state) % 2 == 1:
        print("This puzzle is unsolvable since it has an inversion of " + str(
            calculate_inversion(current_state)) + ", which is an odd number.")
        return False
    solution_steps = []
    while not np.array_equal(current_state, final_state):
        moves = get_moves(current_state)
        h = heuristic(current_state, final_state)
        new_state = make_move(current_state, moves.pop())
        while heuristic(new_state, final_state) >= h:
            if len(moves) == 0:
                print("got stuck here")
                return solution_steps
            new_state = make_move(current_state, moves.pop())
        solution_steps.append(new_state)
        current_state = new_state
    return solution_steps


def make_move(current_state, move):
    zero_x, zero_y = np.where(current_state == 0)
    num_to_swap = current_state[zero_x + move[0], zero_y + move[1]]
    new_state = np.copy(current_state)
    new_state[zero_x, zero_y] = num_to_swap
    new_state[zero_x + move[0], zero_y + move[1]] = 0
    return new_state


def print_solution(unsolved, steps, final_state):
    print("Goal state:")
    print(final_state)
    print("---------------")
    print("Initial state:")
    print(unsolved)
    print("---------------")
    print("The steps:")
    for step in steps:
        print(step)
        print("---------------")


puzzle = puzzles[1]
solve_eight_puzzle(puzzle, goal_state)
