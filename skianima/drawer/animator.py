import skia
from typing import Any, Callable
from skianima.utils.frame_range import FrameRange

class Animator:
    """A drawer which can draw animations"""
    def __init__(self,range:FrameRange,animation:Callable[[skia.Canvas,int,float],Any]) -> None:
        self.range=range
        self.animation=animation
        pass
    
    def animate(self,canvas:skia.Canvas,frame:int)->None:
        animating_frame=frame-self.range.start_frame
        animating_phase:float=animating_frame/(self.range.end_frame- self.range.start_frame)

        self.animation(canvas,animating_frame,animating_phase)

    def is_animating(self,frame:int)->bool:
        return self.range.contains(frame)