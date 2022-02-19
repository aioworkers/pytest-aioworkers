from collections import namedtuple


try:
    from .version import __version__
except ImportError:
    __version__ = "dev"


AioWorkers = namedtuple("AioWorkers", "plugins groups")
Groups = namedtuple("Groups", "include exclude")


class Plugins(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.default = False