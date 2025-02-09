import json
import os
from moviepy.editor import VideoClip, TextClip, ImageClip, CompositeVideoClip

# File paths
SCRIPT_PATH = "scripts/script.json"
LOGO_PATH = "C:\Users\KIIT\Desktop\Forgetube\79008924.jpeg"
OUTPUT_PATH = "video_output/intro.mp4"

# Load JSON script
with open(SCRIPT_PATH, "r") as file:
    script_data = json.load(file)

title = script_data.get("title", "Default Title")

# Video settings
duration = 5  # seconds
resolution = (1920, 1080)  # Full HD
fps = 24

# Create a black screen
def make_frame(t):
    return (0, 0, 0)  # Black background

black_screen = VideoClip(make_frame, duration=duration).set_fps(fps)

# Add title text
title_clip = TextClip(title, fontsize=80, color="white", font="Arial-Bold")
title_clip = title_clip.set_position("center").set_duration(duration)

# Add MLSA logo
logo = ImageClip(LOGO_PATH).set_duration(duration).resize(height=150)
logo = logo.set_position(("right", "top"))

# Combine elements
final_clip = CompositeVideoClip([black_screen, title_clip, logo])

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Export the video
final_clip.write_videofile(OUTPUT_PATH, fps=24)