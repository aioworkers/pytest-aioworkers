from typing import MutableSet, NamedTuple

__version__ = "0.0.0"


class Groups(NamedTuple):
    include: MutableSet[str]
    exclude: MutableSet[str]


class Plugins(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.default = False


class AioWorkers(NamedTuple):
    plugins: Plugins
    groups: Groups
