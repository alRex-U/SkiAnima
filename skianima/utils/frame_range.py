class FrameRange:
    # contains start_frame and end_frame
    def __init__(self,start_frame:int,end_frame:int) -> None:
        self.start_frame=start_frame
        self.end_frame=end_frame

    def contains(self,frame:int)->bool:
        return self.start_frame<=frame & frame<=self.end_frame
