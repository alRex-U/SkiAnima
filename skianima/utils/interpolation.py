import math
from typing import Any, Callable, overload
import skia

def linear(factor:float)->float:
    return factor

def ease_in(factor:float)->float:
    return 1-math.pow(factor-1,2)

def ease_out(factor:float)->float:
    return math.pow(factor,2)

def ease_out_quint(factor:float)->float:
    return math.pow(factor,4)

def ease_in_quint(factor:float)->float:
    return 1-math.pow(factor-1,4)

def cubic(factor:float)->float:
    return -2*math.pow(factor,3)+3*math.pow(factor,2)

def move(start:float,end:float,factor:float,easing_func:Callable[[float],float])->float:
    diff=end-start
    return start+diff*easing_func(factor)

def move_points(start:skia.Point,end:skia.Point,factor:float,easing_func:Callable[[float],float])->skia.Point:
    offset= skia.Point(end.fX-start.fX,end.fY-start.fX).scale(easing_func(factor))
    return skia.Point(start.fX+offset.fX,start.fY+offset.fY)