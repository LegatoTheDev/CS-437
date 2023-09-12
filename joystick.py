from sense_hat import SenseHat

sense= SenseHat()
pxl = [3,3]
sense.clear()
while True:
    for event in sense.stick.get_events():
        print(event.direction,event.action)
        if event.action =="pressed":  ## check if the joystick was pressed
            if event.direction=="up":
                pxl[1] = max(pxl[1] - 1, 0)
            if event.direction=="down":
                pxl[1] = min(pxl[1] + 1, 7)
            if event.direction=="right":
                pxl[0] = min(pxl[0] + 1, 7)
            if event.direction=="left":
                pxl[0] = max(pxl[0] - 1, 0)
            sense.clear()
        if event.action == "held":
            if event.direction == "middle":
                sense.clear()
                exit(0)
    sense.set_pixel(pxl[0], pxl[1], (255,255,255))