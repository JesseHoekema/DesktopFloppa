import subprocess
import time
import random



def open_in_preview_with_animation(file_path):
    try:
        # Open the file in Preview
        subprocess.run(['open', '-a', 'Preview', file_path], check=True)
        
        # Use AppleScript to animate the window
        applescript = """
        tell application "Preview"
            activate
            set windowBounds to bounds of front window
            set screenWidth to (item 3 of windowBounds)
            set screenHeight to (item 4 of windowBounds)
            
            -- Move the window off-screen to the left
            set bounds of front window to {-screenWidth, 100, 0, screenHeight + 100}
            
            -- Animate sliding in to the center
            repeat with i from 0 to screenWidth by 20
                set bounds of front window to {i - screenWidth, 100, i, screenHeight + 100}
                delay 0.01
            end repeat
        end tell
        """
        
        # Run the AppleScript
        subprocess.run(['osascript', '-e', applescript], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open or animate the file in Preview: {e}")

# Example usage

def meme():
    file_paths = [
        "assets/meme1.jpeg",
        "assets/meme2.jpg",
        "assets/meme4.png"
    ]
    file_path = random.choice(file_paths)
    open_in_preview_with_animation(file_path)