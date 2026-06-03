import os
import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import pygame
import sys
import subprocess

sys.stdout = sys.stderr = None  # Avoid delay with `--noconsole`
geld = 0


def set_bedrag(bedrag):
    geld = bedrag
    


def get_bedrag():
    resultaat = geld
    # Als er geen saldo is opgeslagen, geef dan 0 terug
    return int(resultaat[0]) if resultaat else 0

# Function to get the correct asset path
def get_asset_path(filename):
    try:
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, 'assets', filename)
    except Exception as e:
        print(f"Error finding asset: {e}")
        return None

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
def play_sound_effect(file_name):
    try:
        sound_choice = file_name
        sound_file = get_asset_path(sound_choice)
        if sound_file and os.path.exists(sound_file):
            sound = pygame.mixer.Sound(sound_file)
            pygame.mixer.Channel(1).play(sound)
    except Exception as e:
        print(f"Error playing sound: {e}")
   
def drop_poop(x, y):
    try:
        poop_window = tk.Toplevel(root)
        poop_window.geometry(f"30x30+{int(x)}+{int(y)}")
        poop_window.attributes('-topmost', False)
        poop_window.lower(root)  # Places below the main window
        poop_window.configure(bg='blue')
        poop_window.overrideredirect(True)
        def on_poop_click(event):
            poop_sound('ding.mp3')
            poop_window.destroy()

        def poop_sound(file_name):
            try:
                sound_choice = file_name
                sound_file = get_asset_path(sound_choice)
                if sound_file and os.path.exists(sound_file):
                    pygame.mixer.music.load(sound_file)
                    pygame.mixer.music.play()
            except Exception as e:
                print(f"Error playing sound: {e}")

        poop_path = get_asset_path('poop.png')
        if poop_path and os.path.exists(poop_path):
            poop_image = Image.open(poop_path)
            poop_image = poop_image.resize((30, 30))
            poop_photo = ImageTk.PhotoImage(poop_image)
            poop_sound('poop.wav')

            poop_label = tk.Label(poop_window, image=poop_photo, bg='#744630')
            poop_label.image = poop_photo  # Keep reference
            poop_label.pack()
            poop_label.bind("<Button-1>", on_poop_click)
            
            # Make the label take up the full window space
            poop_label.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        print(f"Error dropping poop: {e}")

def leave_money(x, y):
    try:
        money_window = tk.Toplevel(root)
        money_window.geometry(f"30x30+{int(x)}+{int(y)}")
        money_window.attributes('-topmost', False)
        money_window.lower(root)  # Plaatst onder het hoofdvenster
        money_window.overrideredirect(True)
    
        def on_money_click(event):
            global geld
            geld += 1
            uit_bedrag = geld


            set_bedrag(uit_bedrag)
            # Speel het geluid af
            money_sound('money.mp3')
            update_money_menu(uit_bedrag, menubar)
            # Sluit het geldvenster
            money_window.destroy()


        def money_sound(file_name):
            try:
                sound_choice = file_name
                sound_file = get_asset_path(sound_choice)
                if sound_file and os.path.exists(sound_file):
                    sound = pygame.mixer.Sound(sound_file)
                    pygame.mixer.Channel(2).play(sound)
            except Exception as e:
                print(f"Error playing sound: {e}")

        money_path = get_asset_path('money.jpg')
        if money_path and os.path.exists(money_path):
            money_image = Image.open(money_path)
            money_image = money_image.resize((30, 30))
            money_photo = ImageTk.PhotoImage(money_image)
            money_sound('money.mp3')

            money_label = tk.Label(money_window, image=money_photo)
            money_label.image = money_photo  # Behoud referentie
            money_label.pack()
            money_label.bind("<Button-1>", on_money_click)
        
            # Maak de label die de volledige venster ruimte inneemt
            money_label.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        print(f"Error dropping money: {e}")

def meme():
    file_paths = [
        "meme1.jpeg",
        "meme2.jpg",
        "meme4.png"
    ]
    file_path = random.choice(file_paths)
    open_in_preview_with_animation(get_asset_path(file_path))

# Function to play a sound randomly (sound1 or sound2)
def play_random_sound():
    try:
        sound_choice = random.choice(['sound.mp3', 'sound2.mp3'])
        sound_file = get_asset_path(sound_choice)
        if sound_file and os.path.exists(sound_file):
            sound = pygame.mixer.Sound(sound_file)
            pygame.mixer.Channel(4).play(sound)
    except Exception as e:
        print(f"Error playing sound: {e}")

def play_sound():
    try:
        sound_choice = 'sound3.mp3'
        sound_file = get_asset_path(sound_choice)
        if sound_file and os.path.exists(sound_file):
            sound = pygame.mixer.Sound(sound_file)
            pygame.mixer.Channel(5).play(sound)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to move the window smoothly
def move_window_smoothly(target_x, target_y, steps=50, delay=10):
    try:
        global current_x, current_y, window_height
        current_x = int(root.geometry().split('+')[1])
        current_y = int(root.geometry().split('+')[2])

        delta_x = (target_x - current_x) / steps
        delta_y = (target_y - current_y) / steps

        for _ in range(steps):
            current_x += delta_x
            current_y += delta_y
            root.geometry(f'{window_width}x{window_height}+{int(current_x)}+{int(current_y)}')
            root.update()
            time.sleep(delay / 800)


        # Randomly decide if this movement should drag the mouse (20% chance)
        # After moving the window, randomly drop poop
        if random.randint(1, 100) <= 30:
            drop_poop(current_x, current_y)

        # After moving the window, wait a random time between 1000 and 5000 seconds to play sound
        if random.randint(1, 100) <= 35:
            play_random_sound()
        
        if random.randint(1, 100) <= 20:
            meme()

        root.after(random.randint(3000, 9000), move_window)
    except Exception as e:
        print(f"Error moving window: {e}")

# Function to move the window
def move_window():
    try:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        target_x = random.randint(0, screen_width - window_width)
        target_y = random.randint(0, screen_height - window_height)

        move_window_smoothly(target_x, target_y)
    except Exception as e:
        print(f"Error in move_window: {e}")

# Function to create music toggle window
def toggle_music_window():
    try:
        music_window = tk.Toplevel(root)
        music_window.title("Settings")
        music_window.geometry("250x150")
        music_window.config(padx=20, pady=20)

        def toggle_music():
            try:
                if music_on.get():
                    bg_music = get_asset_path('background.wav')
                    if bg_music and os.path.exists(bg_music):
                        sound = pygame.mixer.Sound(bg_music)
                        pygame.mixer.Channel(6).play(sound, loops=-1)
                else:
                    pygame.mixer.music.stop()
            except Exception as e:
                print(f"Error toggling music: {e}")

        toggle_button = tk.Checkbutton(music_window, text="Background Music", variable=music_on, command=toggle_music)
        toggle_button.pack()

        close_button = tk.Button(music_window, text="Close App", command=root.quit)
        close_button.pack(pady=10)
    except Exception as e:
        print(f"Error creating music window: {e}")

def update_money_menu(moneyamount, menubalk):
    # Maak een menu aan
    app_menu = tk.Menu(menubalk, tearoff=2)
    
    # Voeg het menu toe aan de menubalk met het dynamische label
    menubalk.delete(1)
    menubalk.add_cascade(label=f"Money: {moneyamount}", menu=app_menu)
    
    # Stel de menubalk in als het menu van het hoofdvenster
    root.config(menu=menubalk)

# Function to handle clicks
def on_click(event):
    try:
        global last_click_time
        current_time = time.time()

        leave_money(current_x, current_y)

        last_click_time = current_time
    except Exception as e:
        print(f"Error handling click: {e}")

# Main execution block
if __name__ == "__main__":
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        root = tk.Tk()
        root.title('Big Floppa')
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        global floppa_photo
        floppa_path = get_asset_path('floppa.png')
        if floppa_path and os.path.exists(floppa_path):
            floppa_image = Image.open(floppa_path)

            new_width = 70
            width_percent = (new_width / float(floppa_image.size[0]))
            new_height = int((float(floppa_image.size[1]) * float(width_percent)))
            floppa_image = floppa_image.resize((new_width, new_height))

            window_width, window_height = floppa_image.size
            floppa_photo = ImageTk.PhotoImage(floppa_image)

            canvas = tk.Canvas(root, width=window_width, height=window_height, bg='white', highlightthickness=0)
            canvas.pack()
            canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=floppa_photo)
            canvas.config(bg='systemTransparent')

            # Add focus handling to prevent image disappearing
            def handle_focus(event):
                canvas.update_idletasks()
                toggle_music_window()

            # Bind focus events

            global menubar
            menubar = tk.Menu(root)
            root.config(menu=menubar)
            app_menu = tk.Menu(menubar, name='apple')
            menubar.add_cascade(label='Settings', menu=app_menu)
            app_menu.add_command(label='Open Settings', command=toggle_music_window)
            bedrag = get_bedrag()
            update_money_menu(bedrag, menubar)

            music_on = tk.BooleanVar(value=False)
            canvas.bind("<Button-1>", on_click)

            last_click_time = time.time()

            move_window()
            root.mainloop()
        else:
            print("Error: Could not find floppa.png")
            sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
