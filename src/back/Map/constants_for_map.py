SIZE_OF_MAP = (48, 48)

# nums for generate some basic
NUM_OF_GENERATED_BASIC_ROOMS = 50
NUM_OF_GENERATED_COLUMNS = 50

# num of stuff on the map
NUM_OF_COLUMNS_ON_MAP = SIZE_OF_MAP[0] * SIZE_OF_MAP[1] // 200
NUM_OF_ADDITION_ROOMS_ON_MAP = SIZE_OF_MAP[0] * SIZE_OF_MAP[1] // 200
NUM_OF_BASIC_ROOMS_ON_MAP = SIZE_OF_MAP[0] * SIZE_OF_MAP[1] // 200

# width of rooms
MIN_WIDTH_OF_BASIC_ROOM = 4
MAX_WIDTH_OF_BASIC_ROOM = 7

MIN_WIDTH_OF_COLUMN = 1
MAX_WIDTH_OF_COLUMN = 3

# constants for generate doors
MIN_FREQ_OF_DOOR = 10
MAX_FREQ_OF_DOOR = 15

# sizes

SIZE_OF_TILE = 72
SIZE_OF_TILE_ON_MINI_MAP = 12
SIZE_OF_ITEM_ON_MINI_MAP = 12
MINI_MAP_SCALE = 12 / 72

SIZE_OF_ICON_ON_MINIMAP = [20, 20]

# nums of images
NUM_OF_UP_WALLS = 3
NUM_OF_DOWN_WALLS = 4
NUM_OF_LEFT_WALLS = 3
NUM_OF_RIGHT_WALLS = 3
NUM_OF_FLOORS = 14

# chars for tiles
CHAR_FOR_COLUMN = 'Q'
CHAR_FOR_DOOR = 'W'
CHAR_FOR_SIGN = 'E'
CHAR_FOR_FLOOR = 'R'
CHAR_FOR_PATH = 'T'
CHAR_FOR_UP_WALL = 'Y'
CHAR_FOR_DOWN_WALL = 'U'
CHAR_FOR_LEFT_WALL = 'Z'
CHAR_FOR_RIGHT_WALL = 'O'
CHAR_FOR_LEFT_DOWN_IN_CORNER = 'P'
CHAR_FOR_LEFT_DOWN_OUT_CORNER = 'A'
CHAR_FOR_RIGHT_DOWN_IN_CORNER = 'S'
CHAR_FOR_DOWN_OUT_CORNER = 'D'
CHAR_FOR_POTENTIAL_DOOR = 'F'
CHAR_FOR_EMPTY = 'G'
CHAR_FOR_ONE_WIDTH_PATH = 'H'
CHAR_FOR_MAP_BOARD = 'J'
CHAR_FOR_OPEN_DOOR = 'K'
CHAR_FOR_CLOSED_DOOR = 'L'

# sets with tiles
SET_WITH_WALLS = [CHAR_FOR_UP_WALL, CHAR_FOR_DOWN_WALL, CHAR_FOR_LEFT_WALL, CHAR_FOR_RIGHT_WALL, CHAR_FOR_DOOR,
                  CHAR_FOR_LEFT_DOWN_IN_CORNER, CHAR_FOR_LEFT_DOWN_OUT_CORNER, CHAR_FOR_DOWN_OUT_CORNER,
                  CHAR_FOR_RIGHT_DOWN_IN_CORNER]

SET_WITH_CORNERS = [CHAR_FOR_LEFT_DOWN_IN_CORNER, CHAR_FOR_LEFT_DOWN_OUT_CORNER, CHAR_FOR_DOWN_OUT_CORNER,
                    CHAR_FOR_RIGHT_DOWN_IN_CORNER]

SET_WITH_DOORS = [CHAR_FOR_DOOR, CHAR_FOR_CLOSED_DOOR, CHAR_FOR_OPEN_DOOR]

# specific constants
DEPTH_OF_DFS_FOR_PATHS = 5
MAX_SIZE_OF_START_ROOM = 20
