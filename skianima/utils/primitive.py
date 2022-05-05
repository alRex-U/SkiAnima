import skia

def rect_at(width:float,height:float,at:skia.Point)->skia.Rect:
    return skia.Rect(at.fX-width/2,at.fY-height/2,at.fX+width/2,at.fY+height/2)