from skianima.utils.paints import *
from skianima import *

anima=SkiAnima(width=400,height=200,max_frame=20)
black_paint=Paint(BLACK)

def test(canvas:Canvas,anim_frame:int,anim_phase:float):
    canvas.drawRect(Rect(100+100*anim_phase,100),RED)

def test1(canvas:Canvas,anim_frame:int,anim_phase:float):
    canvas.drawCircle(200,100,1+50*anim_phase,BLUE)

def init_canvas(canvas:skia.Canvas):
    canvas.clear(Color4f(0,0,0,0))

anima.setCanvasInit(init_canvas)
anima.add(anime(frame_in(1,10),test))
anima.add(anime(frame_in(1,20),test1))
anima.add(paint(
    lambda canvas:canvas.drawLine(
        Point(0,0),
        Point(100,100),
        Paint(Color=ColorBLACK,StrokeWidth=10.)
        )
    ))

anima.run()