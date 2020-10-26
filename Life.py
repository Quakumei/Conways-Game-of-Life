import pygame
import time


def count_neighbors(x, y, game_map):
    """
    Returns count of live neighbours
    around the cell with coordinates
    (x,y)
    """
    width = len(game_map[0])
    height = len(game_map)
    count = 0
    for yn in range(y - 1, y + 1 + 1):
        for xn in range(x - 1, x + 1 + 1):
            # Statement check
            if (yn >= 0) and (yn < height) and \
                    (xn >= 0) and (xn < width):  # Check whether out of bounds
                if not ((yn == y) and (xn == x)):
                    if game_map[yn][xn] == 1:
                        count += 1
    return count


def do_turn(game_map):
    """
    Makes a turn of Life game for a given map,
    returns next game_map
    """

    width = len(game_map[0])
    height = len(game_map)
    survivor_map = [[0 for _ in range(width)] for _ in
                    range(height)]  # Memory suffers, maybe do something with it later on?
    for y in range(height):
        for x in range(width):
            neigh_count = count_neighbors(x, y, game_map)
            if game_map[y][x] == 1 and (2 <= neigh_count <= 3):
                survivor_map[y][x] = 1
            elif game_map[y][x] == 0 and (neigh_count == 3):
                survivor_map[y][x] = 1

    return survivor_map


def draw_map(game_map, screen, x0, y0, tile_size, dead_tile_pic, alive_tile_pic):
    height = len(game_map)
    width = len(game_map[0])
    for y in range(height):
        for x in range(width):
            tile_pic = -1
            if game_map[y][x] == 0:
                tile_pic = dead_tile_pic
            elif game_map[y][x] == 1:
                tile_pic = alive_tile_pic
            screen.blit(tile_pic, (x0 + x * tile_size, y0 + y * tile_size))


def log_map(game_map):
    for y_line in game_map:
        print(y_line)


def main():
    pygame.init()
    pygame.display.set_caption("Implementation of Conway's Game of Life.")
    logo = pygame.image.load("Life/10.png")

    # Initialize empty field game

    # # Map
    """
        Map is a 2d array which contains
        integers - states of the cell.
        0 - dead. 1 - alive.
    """
    map_width = 10
    map_height = 10
    turn_latency = 1

    empty_map = [[0 for _ in range(map_width)] for _ in range(map_height)]

    #
    # Map Configuration
    #
    for y in range(2, 7):
        empty_map[y][5] = 1

    # # Turn counter
    """
        For further extensions, but
        on the first stage, it plays
        no role as the behaviour of cells
        doesn't depend on the turn.
        Though it be a good measure of
        measuring time.
    """
    turn = 0

    game_state = {
        "map": empty_map,
        "turn": turn
    }

    """
        It is supposed that
        after the creation of empty map
        player will set the live cells
        by mouse and start the game by 
        clicking corresponding button or key
    """

    # # Window creation

    # TODO: Create map viewer. - Done!
    # Load images...
    tile_size = 16  # In pixels
    number_image = [pygame.image.load("Life/" + str(num) + ".png") for num in range(11)]  # 10.png is null tile
    alive_tile_pic = pygame.image.load("Life/alive_tile.png")
    dead_tile_pic = pygame.image.load("Life/dead_tile.png")

    # Window
    screen_width = tile_size * (map_width + 1)  # +1 is for coordinates indexes
    screen_height = tile_size * (map_height + 1)
    screen = pygame.display.set_mode((screen_width, screen_height))

    # TODO: Draw Coordinates' system - Done!
    window_bg_rgb = (100, 100, 100)
    screen.fill(window_bg_rgb)  # For testing purposes is taken 100 100 100

    # Y axis
    for i in range(0, map_height):
        x = 0
        y = tile_size * (i + 1)
        screen.blit(number_image[i % 10], (x, y))

    # X axis
    for i in range(0, map_width):
        x = tile_size * (i + 1)
        y = 0
        screen.blit(number_image[i % 10], (x, y))

    # 0,0
    screen.blit(number_image[10], (0, 0))

    # Main cycle further...
    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # TODO: Game state-changer - Done!
        draw_map(game_state["map"], screen, tile_size, tile_size, tile_size, dead_tile_pic, alive_tile_pic)
        game_state["map"] = do_turn(game_state["map"])
        turn += 1

        pygame.display.flip()
        time.sleep(turn_latency)


if __name__ == "__main__":
    main()
