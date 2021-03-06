"""
Tic-Tac-Toe
Matheus Plinta
"""

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    x_turn = True

    while True:
        print_grid(grid)

        # Check for win
        is_winner = check_winner(grid)

        if is_winner is not None:
            print(
                f'\n{"x won!" if is_winner == "x" else "o won!"} Thanks for playing!')
            break

        # Check for draw
        if check_if_draw(grid):
            print('\nIt\'s a draw! Thanks for playing!')
            break

        # User input
        try:
            position = int(
                input(f'\n{"x" if x_turn else "o"}\'s turn to choose a square (1-9): '))
        except ValueError:
            print('\nInvalid input.')
            continue

        # Process input
        if 1 <= position <= 9:
            current_value = grid[position - 1]

            if current_value == 'x' or current_value == 'o':
                print(
                    f'There is already a \'{current_value}\' in this position.')
                continue

            grid[position - 1] = 'x' if x_turn else 'o'

            x_turn = not x_turn
        else:
            print('\nPlease type a number from 1 to 9 only.')


def print_grid(grid_):
    print(
        f'\n{grid_[0]}|{grid_[1]}|{grid_[2]}\n-+-+-\n{grid_[3]}|{grid_[4]}|{grid_[5]}\n-+-+-\n{grid_[6]}|{grid_[7]}|{grid_[8]}')


def check_winner(grid_):
    if grid_[0] == grid_[1] and grid_[1] == grid_[2]:
        return grid_[0]
    elif grid_[3] == grid_[4] and grid_[4] == grid_[5]:
        return grid_[3]
    elif grid_[6] == grid_[7] and grid_[7] == grid_[8]:
        return grid_[6]
    elif grid_[0] == grid_[3] and grid_[3] == grid_[6]:
        return grid_[0]
    elif grid_[1] == grid_[4] and grid_[4] == grid_[7]:
        return grid_[1]
    elif grid_[2] == grid_[5] and grid_[5] == grid_[8]:
        return grid_[2]
    elif grid_[0] == grid_[4] and grid_[4] == grid_[8]:
        return grid_[0]
    elif grid_[2] == grid_[4] and grid_[4] == grid_[6]:
        return grid_[2]

    return None


def check_if_draw(grid_):
    for play in grid_:
        if type(play) is int:
            return False

    return True


if __name__ == '__main__':
    main()
