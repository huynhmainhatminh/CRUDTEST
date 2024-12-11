from . import *


class Display:
    def __init__(self) -> None:
        self.layout: Layout = self.make_layout_home()