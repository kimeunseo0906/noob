import ffmpeg
import os
os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"

input_path="APT.mp4.mp4"
output_path="APT.mp4_louder.mp4"

ffmpeg.input(input_path).output(
    output_path,
    af="volume=1.25",
    **{'c:v':'copy'}
).run()