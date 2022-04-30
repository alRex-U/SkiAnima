from typing import Any, Callable
import skia
import skianima.drawer.animator as a
import skianima.drawer.painter as p
from skianima.utils.frame_range import FrameRange

def frame_in(start:int,end:int)->FrameRange:
    return FrameRange(start,end)

def anime(range:FrameRange,animator:Callable[[skia.Canvas,int,float],Any])->a.Animator:
    return a.Animator(range,animator)

def paint(painter:Callable[[skia.Canvas],Any])->p.Painter:
    return p.Painter(painter)