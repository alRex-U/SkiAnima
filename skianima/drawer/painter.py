import skia
from typing import Any, Callable

class Painter:
    """A drawer which draw somethings"""
    def __init__(self,painter:Callable[[skia.Canvas],Any]) -> None:
        self.animation=painter
        pass
    def render(self,canvas:skia.Canvas)->None:
        self.animation(canvas)
        skia.Size()
        pass