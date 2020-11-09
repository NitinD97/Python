def display_sample_area(area):
    for row in area:
        for tile in row:
            print(f'{str(tile).rjust(6)}', end='')
        print()
    print('\n\n')


def clean_tile(area, pos_x, pos_y, max_height, max_width):
    # display_sample_area(area)
    if area[pos_x][pos_y] == 1:
        return area
    if area[pos_x][pos_y] == 0:
        # 1 marks the cleaned area
        area[pos_x][pos_y] = 1
    # to move up
    if pos_y > 0 and area[pos_x][pos_y] != -1:
        clean_tile(area, pos_x, pos_y-1, max_height, max_width)
    # to move down
    if pos_y < max_width-1 and area[pos_x][pos_y] != -1:
        clean_tile(area, pos_x, pos_y+1, max_height, max_width)
    # to move left
    if pos_x > 0 and area[pos_x][pos_y] != -1:
        clean_tile(area, pos_x-1, pos_y, max_height, max_width)
    if pos_x < max_height-1 and area[pos_x][pos_y] != -1:
        clean_tile(area, pos_x+1, pos_y, max_height, max_width)
    return area


def robot_working():
    sample_area = [
        [0, 0, 0, 0, 0, 0],
        [-1, -1, 0, 0, -1, 0],
        [0, -1, 0, -1, -1, -1],
        [-1, -1, 0, -1, 0, -1],
        [0, 0, 0, -1, -1, -1]
    ]
    display_sample_area(sample_area)


    max_width = len(sample_area[0]) # value is 6
    max_height = len(sample_area) # value is 6

    # pos_x, pos_y = map(int, input('Enter Pos: ').split()) # value daani hai 0 2
    pos_x, pos_y = 0, 2

    area = clean_tile(sample_area, pos_x, pos_y, max_height, max_width)
    display_sample_area(area)


if __name__ == '__main__':
    robot_working()