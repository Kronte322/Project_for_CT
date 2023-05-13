from src.back.personages import *

RUNNING = True

FPS = 60
CHARACTER = 'knight'
SIZE_OF_BASIC_CHEST = 48

DISTANCE_OF_ACTION = 100

SIZE_OF_MOVE_BOX = [600, 300]
WINDOW_SIZE = [1920, 1000]

POSITION_OF_PLAYER_ON_SCREEN = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]

SIZE_OF_MENUS = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]

SIZE_OF_MINI_MAP = (WINDOW_SIZE[1] // 3, WINDOW_SIZE[1] // 3)
SIZE_OF_TABED_MINIMAP = [WINDOW_SIZE[0] * 0.6, WINDOW_SIZE[1] * 0.6]

# positions
POSITION_OF_MINI_MAP = [WINDOW_SIZE[0] - SIZE_OF_MINI_MAP[0], 0]
POSITION_OF_TABED_MINIMAP = [(WINDOW_SIZE[0] - SIZE_OF_TABED_MINIMAP[0]) // 2,
                             (WINDOW_SIZE[1] - SIZE_OF_TABED_MINIMAP[1]) // 2]

CHARACTERS = [('skeleton', skeleton), ('hooded_protogonist', hooded_protogonist), ('wizard', wizard),
              ('knight', knight), ('magic_wizard', magic_wizard), ('fantasy_warior', fantasy_warior),
              ('huntress', huntress), ('warior', warior), ('king', king), ('skeleton_warior', skeleton_warior),
              ('goblin', goblin), ('mushroom', mushroom), ('flying_eye', flying_eye)]

# strings for UI
CAPTION = 'Isac'
WELCOME_CONDITION_STRING = 'Welcome'
PLAY_CONDITION_STRING = 'Play'
WIN_CONDITION_STRING = 'You Won'
RETRY_CONDITION_STRING = 'Retry'
QUIT_CONDITION_STRING = 'Quit'
SETTINGS_CONDITION_STRING = 'Settings'
BACK_CONDITION_STRING = 'Back'
DIFFICULTY_SELECTION_STRING = 'Difficulty:'
SIZE_SELECTION_STRING = 'Size:'
ALGORITHM_CONDITION_STRING = 'Algorithm for generator:'
MENU_CONDITION_STRING = 'Menu'
RESUME_CONDITION_STRING = 'Resume'
CHARACTER_SELECTION_STRING = 'Character:'
ANSWER_BUTTON_STRING = 'Show Answer'
SAVE_MAZE_STRING = 'Save'
NAME_MAZE_STRING = 'Name of the save:'
DEFAULT_NAME_FOR_SAVE = 'New_Save'
LOAD_STRING = 'Load'
CHOOSE_FILE_STRING = 'Choose file:'
PICK_SERVER_STRING = 'Pick a server'
CONNECT_BUTTON_STRING = 'Connect'

