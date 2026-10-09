import os
import subprocess

class BlindCutApp:
    def __init__(self):
        print("BlindCut App Started")

    def trim_media(self, input_path, start_time, end_time, output_path):
        command = [
            'ffmpeg', '-y',
            '-ss', str(start_time),
            '-to', str(end_time),
            '-i', input_path,
            '-c', 'copy',
            output_path
        ]
        subprocess.run(command, check=True)

    def extract_audio(self, video_path, output_mp3_path):
        command = [
            'ffmpeg', '-y',
            '-i', video_path,
            '-vn',
            '-q:a', '2',
            output_mp3_path
        ]
        subprocess.run(command, check=True)

    def add_background_music(self, video_path, music_path, output_path, music_volume=0.3):
        filter_str = f"[0:a]volume=1.0[a0];[1:a]volume={music_volume}[a1];[a0][a1]amix=inputs=2:duration=first[aout]"
        command = [
            'ffmpeg', '-y',
            '-i', video_path,
            '-i', music_path,
            '-filter_complex', filter_str,
            '-map', '0:v',
            '-map', '[aout]',
            '-c:v', 'copy',
            output_path
        ]
        subprocess.run(command, check=True)

if __name__ == "__main__":
    app = BlindCutApp()
