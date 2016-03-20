import copyreg
import pickle

class GameState(object):
    # fix for unpickling issue -- default constructor args
    #def __init__(self, level=0, lives=4, points=0):
    #def __init__(self, level=0, lives=4, points=0, magic=5):
        #self.level = level
        #self.lives = lives
        #self.points = points
        #self.magic = magic

    def __init__(self):
        self.level = 0
        self.lives = 4

        # comment this in and loadSavedGame
        # point will be missing from unpickled object despite using new GameState object
        # self.points = 0

state_path = '/tmp/game_state.bin'

def playGameAndSave():
    state = GameState()
    state.level += 1 # Player beat a level
    state.lives -= 1 # Player died once while trying to beat the level

    #state.points += 1000

    # user quits
    with open (state_path, 'wb') as f:
        pickle.dump(state, f)
    print('saved state', state.__dict__)

def loadSavedGame():
    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)
    print('restored state', state_after.__dict__)


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    #kwargs['vesion'] = 2
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    # Use versioning to make backwards-incompatible changes (for example deleting or renaming a field)
    #if version == 1:
    #   kwargs.pop('magic')
    return GameState(**kwargs)

# register pickling wrappers with copyreg built-in module
#copyreg.pickle(GameState, pickle_game_state)

playGameAndSave()
loadSavedGame()
