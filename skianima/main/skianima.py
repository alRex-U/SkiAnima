import typing
import os

from skianima.drawer.animator import Animator
from skianima.drawer.painter import Painter

import skia

class SkiAnima:
    def __init__(self,width:int,height:int,max_frame:int) -> None:
        self.width=width
        self.height=height
        self.max_frame=max_frame
        self.renderers:typing.List[Animator|Painter] =list()
        self.canvas_init=None
        return
    
    def add(self,drawer:Animator|Painter)->None:
        """Add new renderers to the list"""
        self.renderers.append(drawer)
        return self

    def run(self)->None:
        self.run_with(skia.EncodedImageFormat.kPNG)

    def run_with(self,format:skia.EncodedImageFormat)->None:
        """Render images and save or overwrite them to './output/'"""
        images=self.__draw()
        if not os.path.exists("output"): os.makedirs("output")
        for i in range(len(images)):
            filepath="output/"+str(i+1)+".png"
            print(filepath)
            images[i].save(filepath,format)
        
    def setCanvasInit(self,initializer)->None:
        self.canvas_init=initializer

    def __draw(self)->list[skia.Image]:
        images=list[skia.Image]()
        for frame in range(1,self.max_frame+1):
            surface=skia.Surface(self.width,self.height)
            with surface as canvas:
                if self.canvas_init!=None:
                    self.canvas_init(canvas)
                for renderer in self.renderers:
                    if isinstance(renderer,Painter):
                        renderer.render(canvas)
                    elif renderer.is_animating(frame):
                        renderer.animate(canvas,frame)
            images.append(surface.makeImageSnapshot())
        return images
    