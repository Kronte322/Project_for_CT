import src.back.menus as menus
import src.back.Game


class OnStartProcess:
    def __init__(self, display):
        self.display = display
        self.menu = menus.StartMenu(self.display, self)
        self.menu.ProcessMenu()

    def MoveToCharacterSelection(self):
        self.menu.Close()
        CharacterSelectionProcess(self.display)


class CharacterSelectionProcess:
    def __init__(self, display):
        self.display = display
        self.menu = menus.CharacterSelectionMenu(self.display, self)
        self.menu.ProcessMenu()
        self.character = 1

    def SetCharacter(self, character):
        self.character = character

    def StartGameSession(self):
        src.back.Game.Game.StartGameSession(self.character)

    def MoveToOnStartProcess(self):
        self.menu.Close()
        OnStartProcess(self.display)
