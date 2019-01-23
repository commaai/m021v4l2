#!/usr/bin/env python

'''
capture.py : capture frames from Leopard Imaging LI-USB30-M021 camera and display them using OpenCV

Copyright (C) 2016 Simon D. Levy

This file is part of M021_V4L2.

M021_V4L2 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
BreezySTM32 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with M021_V4L2.  If not, see <http://www.gnu.org/licenses/>.
'''

import cv2
import os
import threading
import subprocess
from m021v4l2 import Capture1280x720
from time import time
from subprocess import Popen, PIPE

start = time

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
	threading.Thread.__init__(self)
	self.previewName = previewName
        self.camID = camID
    def run(self):
	camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cap = Capture1280x720(cam_id=camID)
    if cap.getCount >= 1:
       rval, frame = cap.read()
    else:
       rval = False

    while rval:
        cv2.imshow(previewName, frame)
        key = cv2.waitKey(20)
        if key == 27:
           break
    cv2.destroyWindow(previewName)

# Use this to open threads
thread1 = camThread('LI-USB30-M021', 1)
#thread2 = camThread('LI-USB30-M021', 2)
#thread3 = camThread('LI-USB30-M021', 3)

thread1.start()
#thread2.start()
#thread3.start()
