class Personage:
    def __init__(self, path_stat, num_stat, path_down, num_down, path_up, num_up, path_right, num_right, path_left,
                 num_left, path_icon, name, recom_freq=3):
        self.path_stat = path_stat
        self.num_stat = num_stat
        self.path_down = path_down
        self.num_down = num_down
        self.path_up = path_up
        self.num_up = num_up
        self.path_right = path_right
        self.num_right = num_right
        self.path_left = path_left
        self.num_left = num_left
        self.path_icon = path_icon
        self.name = name
        self.frequency = recom_freq


personages = []

skeleton = Personage("../tile_sets/tiles_for_chars/personages/skeleton/skeleton_down/sprite_", 1,
                     "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_down/sprite_", 9,
                     "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_up/sprite_", 9,
                     "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_right/sprite_", 9,
                     "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_left/sprite_", 9,
                     "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_0.png", "skeleton", 3)

personages.append(skeleton)

hooded_protogonist = Personage("../tile_sets/tiles_for_chars/personages/hooded_protogonist/stat/sprite_", 4,
                               "../tile_sets/tiles_for_chars/personages/hooded_protogonist/down/sprite_", 4,
                               "../tile_sets/tiles_for_chars/personages/hooded_protogonist/up/sprite_", 4,
                               "../tile_sets/tiles_for_chars/personages/hooded_protogonist/right/sprite_", 8,
                               "../tile_sets/tiles_for_chars/personages/hooded_protogonist/left/sprite_", 8,
                               "../tile_sets/tiles_for_chars/personages/hooded_protogonist/hooded_protogonist.png",
                               "hooded_protogonist", 10)

personages.append(hooded_protogonist)

wizard = Personage("../tile_sets/tiles_for_chars/personages/wizard/stat/sprite_", 8,
                   "../tile_sets/tiles_for_chars/personages/wizard/right/sprite_", 7,
                   "../tile_sets/tiles_for_chars/personages/wizard/left/sprite_", 7,
                   "../tile_sets/tiles_for_chars/personages/wizard/right/sprite_", 7,
                   "../tile_sets/tiles_for_chars/personages/wizard/left/sprite_", 7,
                   "../tile_sets/tiles_for_chars/personages/wizard/wizard.png", "wizard", 10)

personages.append(wizard)

knight = Personage("../tile_sets/tiles_for_chars/personages/knight/stat/sprite_", 15,
                   "../tile_sets/tiles_for_chars/personages/knight/right/sprite_", 8,
                   "../tile_sets/tiles_for_chars/personages/knight/left/sprite_", 8,
                   "../tile_sets/tiles_for_chars/personages/knight/right/sprite_", 8,
                   "../tile_sets/tiles_for_chars/personages/knight/left/sprite_", 8,
                   "../tile_sets/tiles_for_chars/personages/knight/knight.png", "knight", 5)

personages.append(knight)

magic_wizard = Personage("../tile_sets/tiles_for_chars/personages/magic_wizard/stat/sprite_", 6,
                         "../tile_sets/tiles_for_chars/personages/magic_wizard/down/sprite_", 8,
                         "../tile_sets/tiles_for_chars/personages/magic_wizard/up/sprite_", 10,
                         "../tile_sets/tiles_for_chars/personages/magic_wizard/right/sprite_", 6,
                         "../tile_sets/tiles_for_chars/personages/magic_wizard/left/sprite_", 6,
                         "../tile_sets/tiles_for_chars/personages/magic_wizard/magic_wizard.png",
                         "magic_wizard", 6)

personages.append(magic_wizard)
