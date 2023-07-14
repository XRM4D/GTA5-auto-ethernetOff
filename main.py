import os
import time
import numpy as np
import dxcam
import cv2


class Detection:

    def __init__(self):
        self.grabber = dxcam.create()

    def search_alert(self):
        frame = self.grabber.grab(region=[1420, 730, 1920, 1080])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = cv2.Canny(gray, 10, 250)
        conturs = cv2.findContours(frame, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

        return True

    def EthernetOff(self):
        os.system("ipconfig/release")

    def EthernetOn(self):
        os.system("ipconfig/renew")


def main():
    det = Detection()
    next_time = 0
    fps = 0

    contin = True
    while contin:
        current_time = time.time() * 1000
        contin = det.search_alert()
        fps += 1

        if current_time >= next_time:
            print(fps)
            fps = 0
            next_time = current_time + 1000

    det.EthernetOff()
    print('OFF')
    time.sleep(15)
    det.EthernetOn()

    print("end!")

if __name__ == "__main__":
    main()