from typing import Any, Callable
import skia
from skianima.utils.interpolation import *
from skianima.utils.points import *
from skianima.utils.paints import *
from skianima.utils.primitive import *
from skianima.drawer.animator import Animator
from skianima.drawer.painter import Painter
from skianima.utils.frame_range import FrameRange

def frame_in(start:int,end:int)->FrameRange:
    return FrameRange(start,end)

def anime(range:FrameRange,animator:Callable[[skia.Canvas,int,float],Any])->Animator:
    return Animator(range,animator)

def paint(painter:Callable[[skia.Canvas],Any])->Painter:
    return Painter(painter)