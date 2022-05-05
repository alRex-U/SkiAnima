from typing import Any, Callable, overload
import skia
from skianima.main.skianima import SkiAnima

def center(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width/2,skianima.height/2)

def right_top(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width,0)

def right_bottom(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width,skianima.height)

def left_top(skianima:SkiAnima)->skia.Point:
    return skia.Point(0,0)

def left_bottom(skianima:SkiAnima)->skia.Point:
    return skia.Point(0,skianima.height)

def top(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width/2,0)

def left(skianima:SkiAnima)->skia.Point:
    return skia.Point(0,skianima.height/2)

def right(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width,skianima.height/2)

def bottom(skianima:SkiAnima)->skia.Point:
    return skia.Point(skianima.width/2,skianima.height)
