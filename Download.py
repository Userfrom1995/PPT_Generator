import subprocess

def download_youtube_video(url, output_path=None):
    try:
        # Build the command
        command = ['youtube-dl', '-f', 'bestvideo+bestaudio', '--merge-output-format', 'mp4', url]

        if output_path:
            command.extend(['-o', output_path])

        # Run the command
        subprocess.run(command, check=True)
        
        print("Download completed!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = 'https://youtu.be/eVIuzh5VMVA?si=KXZoGCpNxolHJAGl'  # Replace with your YouTube video URL
    download_youtube_video(video_url, 'output.mp4')
