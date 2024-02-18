import taipy as tp
import robot
import numpy as np
# from camera import VideoCapture

# Create a Taipy app
app = tp.App()
page = tp.Page()
# Add a title to the page
page.add_title("Armazing-Bot.com")
image = tp.Binding()
page.add_image(image, width=300, height=200, x=150, y=50)
page.add_button("Forward", "/forward")
page.add_button("Backward", "/backward")
page.add_button("Left", "/left")
page.add_button("Right", "/right")
page.add_button("Stop", "/stop")

rest = tp.REST()

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

# video = VideoCapture(image)

# Run the app
if __name__ == "__main__":
    app.run(port=3000)
    print("Server running on port 3000...")
