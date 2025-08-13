# ASCIIPlayer

ASCII Video Player in Python 🎥➡️🔡
ASCII Video Player is a Python-based terminal application that plays videos as animated ASCII art directly in your command line.
It converts each video frame into a matrix of text characters, mapping pixel brightness to symbols like @, %, #, and . for a retro, hacker-style cinematic experience.

✨ Features
* 🎬 Play any MP4 or AVI video in your terminal as ASCII art

* ⚡ Auto FPS detection for smooth playback

* 🖥 Adjustable output width for your terminal size

* 🌓 Brightness-to-character mapping for realistic shading

* 🛠 Cross-platform support (macOS, Linux, Windows)

🔧 How it Works
* OpenCV reads the video frame-by-frame

* Frames are resized to fit your terminal

* Converted to grayscale

* Each pixel’s brightness is mapped to a character from the ASCII set

* Frames are printed sequentially, creating a motion picture effect in pure text

