import os
import subprocess

files = os.listdir("DSA Videos")

for file in files:
    input_file = os.path.join("DSA Videos", file)
    output_file = os.path.join("audios", os.path.splitext(file)[0] + ".mp3")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-vn",
        output_file
    ]

    print(cmd)      # <-- IMPORTANT
    subprocess.run(cmd, check=True)