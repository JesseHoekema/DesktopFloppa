import pyautogui
import random
import time
import sys
from math import sqrt

# Ensure safe exit
pyautogui.FAILSAFE = True  # Move mouse to corner to stop

def get_screen_size():
    """Get the screen dimensions"""
    width, height = pyautogui.size()
    return width, height

def get_random_point(max_width, max_height, margin=50):
    """Generate random coordinates within screen bounds with margin"""
    x = random.randint(margin, max_width - margin)
    y = random.randint(margin, max_height - margin)
    return x, y

def calculate_steps(start_x, start_y, end_x, end_y, num_steps=30):
    """Calculate intermediate points for smooth movement"""
    x_step = (end_x - start_x) / num_steps
    y_step = (end_y - start_y) / num_steps
    
    steps = []
    for i in range(num_steps + 1):
        x = start_x + (x_step * i)
        y = start_y + (y_step * i)
        steps.append((x, y))
    return steps

def smooth_move(start_pos, end_pos, duration=0.5):
    """Move mouse smoothly from start to end position"""
    # Calculate number of steps based on distance
    distance = sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
    num_steps = int(max(30, min(distance / 5, 100)))  # More steps for longer distances
    
    steps = calculate_steps(start_pos[0], start_pos[1], end_pos[0], end_pos[1], num_steps)
    step_delay = duration / num_steps
    
    for step in steps:
        pyautogui.moveTo(step[0], step[1])
        time.sleep(step_delay)

def main():
    # Disable pyautogui pause between actions
    pyautogui.PAUSE = 0
    screen_width, screen_height = get_screen_size()
    
    print("Moving mouse randomly. Move mouse to any screen corner to stop.")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            # Get current mouse position
            current_x, current_y = pyautogui.position()
            
            # Get random destination
            dest_x, dest_y = get_random_point(screen_width, screen_height)
            
            # Move mouse smoothly
            smooth_move((current_x, current_y), (dest_x, dest_y))
            
            # Random pause between movements
            time.sleep(random.uniform(0.5, 2.0))
            
    except KeyboardInterrupt:
        print("\nScript terminated by user")
        sys.exit()

if __name__ == "__main__":
    main()