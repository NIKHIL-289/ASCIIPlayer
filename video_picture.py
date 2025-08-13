import cv2
import os
import time
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    height, width = image.shape[:2]
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return cv2.resize(image, (new_width, new_height))

def grayify(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def pixels_to_ascii(image):
    ascii_str = ""
    for pixel in image.flatten():
        index = int(pixel / 256 * len(ASCII_CHARS))
        ascii_str += ASCII_CHARS[index]
    return ascii_str

def frame_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    gray_image = grayify(image)
    ascii_str = pixels_to_ascii(gray_image)
    pixel_count = len(ascii_str)
    return "\n".join(ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width))

def play_ascii_video(video_path, width=120):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30
    delay = 1 / fps

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        ascii_frame = frame_to_ascii(frame, new_width=width)
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_frame)
        time.sleep(delay)

    cap.release()

play_ascii_video("Picture.png Or video.mp4", width=120)
