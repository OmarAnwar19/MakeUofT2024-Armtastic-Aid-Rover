import taipy as tp
import cv2

class VideoCapture(tp.Component):
    def __init__(self, binding):
        super().__init__(binding)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError("Cannot open camera")
    
    def update(self):
        ret, frame = self.cap.read()
        if not ret: return
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        _, image = cv2.imencode('.jpg', frame)
        image = image.tobytes()
        self.binding.update(image)
