# nums for generate some basic
NUM_OF_GENERATED_BASIC_ROOMS = 50
NUM_OF_GENERATED_COLUMNS = 50

# num of stuff on the map
NUM_OF_COLUMNS_ON_MAP = 12
NUM_OF_ADDITION_ROOMS_ON_MAP = 10
NUM_OF_BASIC_ROOMS_ON_MAP = 100

# width of rooms
MIN_WIDTH_OF_BASIC_ROOM = 4
MAX_WIDTH_OF_BASIC_ROOM = 7

MIN_WIDTH_OF_COLUMN = 1
MAX_WIDTH_OF_COLUMN = 3

# constants for generate doors
MIN_FREQ_OF_DOOR = 10
MAX_FREQ_OF_DOOR = 15

# sizes
WINDOW_SIZE = [1920, 1000]
SIZE_OF_MOVE_BOX = [600, 300]
SPAWN_POSITION = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]
SIZE_OF_TILE = 72
SIZE_OF_TILE_ON_MINI_MAP = 6
SIZE_OF_MAP = (64, 64)
SIZE_OF_MINI_MAP = (WINDOW_SIZE[1] // 3, WINDOW_SIZE[1] // 3)
SIZE_OF_TABED_MINIMAP = [WINDOW_SIZE[0] * 0.6, WINDOW_SIZE[1] * 0.6]
SIZE_OF_ICON_ON_MINIMAP = [20, 20]

# positions
POSITION_OF_MINI_MAP = [WINDOW_SIZE[0] - SIZE_OF_MINI_MAP[0], 0]
POSITION_OF_TABED_MINIMAP = [(WINDOW_SIZE[0] - SIZE_OF_TABED_MINIMAP[0]) // 2,
                             (WINDOW_SIZE[1] - SIZE_OF_TABED_MINIMAP[1]) // 2]

# nums of images
NUM_OF_UP_WALLS = 3
NUM_OF_DOWN_WALLS = 4
NUM_OF_LEFT_WALLS = 3
NUM_OF_RIGHT_WALLS = 3
NUM_OF_FLOORS = 14

# chars for tiles
CHAR_FOR_COLUMN = 'C'
CHAR_FOR_DOOR = 'D'
CHAR_FOR_SIGN = 'S'
CHAR_FOR_FLOOR = '-'
CHAR_FOR_PATH = 'P'
CHAR_FOR_UP_WALL = 'UX'
CHAR_FOR_DOWN_WALL = 'DX'
CHAR_FOR_LEFT_WALL = 'LX'
CHAR_FOR_RIGHT_WALL = 'RX'
CHAR_FOR_LEFT_DOWN_IN_CORNER = 'LDIC'
CHAR_FOR_LEFT_DOWN_OUT_CORNER = 'LDOC'
CHAR_FOR_RIGHT_DOWN_IN_CORNER = 'RDIC'
CHAR_FOR_DOWN_OUT_CORNER = 'RDOC'
CHAR_FOR_POTENTIAL_DOOR = 'PD'
CHAR_FOR_EMPTY = 'E'
CHAR_FOR_ONE_WIDTH_PATH = 'O'
CHAR_FOR_MAP_BOARD = 'B'

# sets with tiles
SET_WITH_WALLS = [CHAR_FOR_UP_WALL, CHAR_FOR_DOWN_WALL, CHAR_FOR_LEFT_WALL, CHAR_FOR_RIGHT_WALL, CHAR_FOR_DOOR,
                  CHAR_FOR_LEFT_DOWN_IN_CORNER, CHAR_FOR_LEFT_DOWN_OUT_CORNER, CHAR_FOR_DOWN_OUT_CORNER,
                  CHAR_FOR_RIGHT_DOWN_IN_CORNER]
