from moviepy.editor import *

# Load the mp4 file
video = VideoFileClip("VIDEO2.mp4")

# Extract audio from video
video.audio.write_audiofile("VIDEO2.mp3")
