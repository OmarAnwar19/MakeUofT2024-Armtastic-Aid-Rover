import taipy
import robot
import picamera

app = taipy.App()
page = taipy.Page()

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

output = camera.StreamingOutput()
camera.start_recording(output, format='mjpeg')

page.add_title("Armazing-Bot.com")

page.add_image("http://raspberrypi.local:8000/stream.mjpg", width=300, height=200, x=150, y=50)
page.add_button("Forward", "/forward")
page.add_button("Backward", "/backward")
page.add_button("Left", "/left")
page.add_button("Right", "/right")
page.add_button("Stop", "/stop")


rest = taipy.REST()

@rest.post("/forward")
def forward_endpoint():
    robot.forward()
    return "Moving forward"

@rest.post("/backward")
def backward_endpoint():
    robot.backward()
    return "Moving backward"

@rest.post("/left")
def left_endpoint():
    robot.left()
    return "Turning left"

@rest.post("/right")
def right_endpoint():
    robot.right()
    return "Turning right"

@rest.post("/stop")
def stop_endpoint():
    robot.stop()
    return "Stopping"


app.add_page(page)
app.add_rest(rest)

if __name__ == "__main__":
    address = ('', 8000)
    cam_server = camera.StreamingServer(address, camera.StreamingHandler)
    cam_server.serve_forever()

    app.run(port=3000)