import cv2 
import socket
import pickle
import os
import numpy as np


server_ip = "0.0.0.0"
server_port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

def main():
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        success, frame = camera.read()  # read the camera frame
        ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
        x_as_bytes = pickle.dumps(buffer);
        s.sendto((x_as_bytes), (server_ip, server_port))
        
    
if __name__ == '__main__':
   main(); 
