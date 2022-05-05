from skianima import *

anima=SkiAnima(width=400,height=200,max_frame=20)
black_paint=Paint(BLACK)
black_paint.setAntiAlias(True)
black_paint.setStrokeCap(Paint.Cap(5))
arc_paint=Paint(CYAN)
arc_paint.setStrokeWidth(600)


def test(canvas:Canvas,frame:int,phase:float):
    canvas.drawRect(
        Rect(move(10,200,phase,cubic),100),
        RED
    )

def test1(canvas:Canvas,frame:int,phase:float):
    canvas.drawArc(
        rect_at(1200,1200,center(anima)),
        move(-90,0,phase,ease_out_quint),move(0,180,phase,ease_out_quint),
        True,
        arc_paint
    )
    canvas.drawArc(
        rect_at(1200,1200,center(anima)),
        move(90,180,phase,ease_out_quint),move(0,180,phase,ease_out_quint),
        True,
        arc_paint
    )


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