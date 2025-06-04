try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time, platform
   from datetime import datetime
   import sys
   import configparser
   import logging 
   import tkinter as tk
   import threading
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """

     _______  __    _  _______  _______    _______  ___      __   __  _______ 
    |       ||  |  | ||   _   ||       |  |       ||   |    |  | |  ||       |
    |  _____||   |_| ||  |_|  ||    _  |  |    _  ||   |    |  | |  ||  _____|
    | |_____ |       ||       ||   |_| |  |   |_| ||   |    |  |_|  || |_____ 
    |_____  ||  _    ||       ||    ___|  |    ___||   |___ |       ||_____  |
     _____| || | |   ||   _   ||   |      |   |    |       ||       | _____| |
    |_______||_|  |__||__| |__||___|      |___|    |_______||_______||_______| v1.2
    
    by @FlazeIGuess with help of @useragents on Github                                                                                        
"""


active_marker_windows = []

class PositionMarker:
    def __init__(self, master, x, y, marker_id, name):
        self.master = master
        self.x = x
        self.y = y
        self.marker_id = marker_id
        self.name = name
        
        self.window = tk.Toplevel(master)
        self.window.attributes('-topmost', True) 
        self.window.attributes("-transparentcolor", "red") 
        self.window.overrideredirect(True) 
        self.window.geometry(f'100x100+{x-50}+{y-50}') 
        self.window.config(bg='red') 
        self.window.lift() 

        
        self.canvas = tk.Canvas(self.window, width=100, height=100, bg='red', highlightthickness=0)
        self.canvas.pack()

        
        
        self.canvas.create_line(10, 10, 90, 90, fill='white', width=2) 
        self.canvas.create_line(10, 90, 90, 10, fill='white', width=2) 

        active_marker_windows.append(self.window)

    def destroy(self):
        self.window.destroy()
        if self.window in active_marker_windows:
            active_marker_windows.remove(self.window)

def onLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

class snapchat:

    ASCII_NUMBERS = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }

    @staticmethod
    def _get_ascii_number_lines(number):
        s_number = str(number)
        lines = ["", "", ""] 
        for digit in s_number:
            if digit in snapchat.ASCII_NUMBERS:
                for i in range(3):
                    lines[i] += snapchat.ASCII_NUMBERS[digit][i] + " " 
        return lines

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3
        self.post_snap_delay = 4 
        self.paused = False
        self.last_mouse_pos = pyautogui.position()
        self._should_quit = False
        self._should_reset = False
        self.platform_mode = None
        self._current_status_message = "" 
        self.config = configparser.ConfigParser() 

        
        self.switch_to_camera = pyautogui.Point(x=0, y=0)
        self.take_picture = pyautogui.Point(x=0, y=0)
        self.send_to = pyautogui.Point(x=0, y=0)
        self.shortcut = pyautogui.Point(x=0, y=0)
        self.select_all = pyautogui.Point(x=0, y=0)
        self.send_snap_button = pyautogui.Point(x=0, y=0)

        self.last_mouse_pos = pyautogui.position() 

        
        self.marker_root = tk.Tk() 
        self.marker_root.withdraw() 
        self._tk_thread = threading.Thread(target=self.marker_root.mainloop, daemon=True)
        self._tk_thread.start()
        
        self._setup_logging() 

    def _setup_logging(self):
        log_file = 'snapscore_booster.log'
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Snapscore Booster PLUS started.")

    def _load_config(self):
        config_file = 'config.ini'
        try:
            
            
            self.delay = int(self.config.get('Settings', 'delay_ms')) / 1000.0
            self.post_snap_delay = int(self.config.get('Settings', 'post_snap_delay_ms')) / 1000.0
            self._config_shortcut_users = int(self.config.get('Settings', 'shortcut_users'))
            self._config_target_snaps = int(self.config.get('Settings', 'target_snaps'))
            self.print_console("Settings loaded from config.ini", status="Info")
            return True
        except (configparser.Error, ValueError) as e:
            self.print_console(f"Error reading config file: {e}. Please check config.ini format.", status="Error")
            return False

    def _save_config(self):
        config_file = 'config.ini'
        try:
            with open(config_file, 'w') as configfile:
                self.config.write(configfile)
            self.print_console("Settings saved to config.ini", status="Info")
        except IOError as e:
            self.print_console(f"Error saving config file: {e}", status="Error")

    def _load_positions(self):
        position_names = ["switch_to_camera", "take_picture", "send_to", "shortcut", "select_all", "send_snap_button"]
        loaded_successfully = True
        try:
            if not self.config.has_section('Positions'):
                self.print_console(f"DEBUG: Sections found by configparser: {self.config.sections()}", status="DEBUG")
                self.print_console("No [Positions] section found in config.ini. Please calibrate positions.", status="Warning")
                return False

            for name in position_names:
                x = int(self.config.get('Positions', f'{name}_x'))
                y = int(self.config.get('Positions', f'{name}_y'))
                setattr(self, name, pyautogui.Point(x=x, y=y))
            self.print_console("Mouse positions loaded from config.ini", status="Info")
            return True
        except (configparser.Error, ValueError) as e:
            self.print_console(f"Error loading mouse positions: {e}. Please recalibrate.", status="Error")
            return False

    def _save_positions(self):
        if not self.config.has_section('Positions'):
            self.config.add_section('Positions')

        positions_to_save = {
            "switch_to_camera": self.switch_to_camera,
            "take_picture": self.take_picture,
            "send_to": self.send_to,
            "shortcut": self.shortcut,
            "select_all": self.select_all,
            "send_snap_button": self.send_snap_button,
        }

        for name, pos_obj in positions_to_save.items():
            if pos_obj is not None: 
                self.config.set('Positions', f'{name}_x', str(pos_obj.x))
                self.config.set('Positions', f'{name}_y', str(pos_obj.y))
            else:
                
                self.config.set('Positions', f'{name}_x', '0')
                self.config.set('Positions', f'{name}_y', '0')
        
        self._save_config() 
        self.print_console("Mouse positions saved to config.ini", status="Info")

    def _destroy_all_markers(self):
        global active_marker_windows
        for window in list(active_marker_windows): 
            try:
                window.destroy()
            except tk.TclError: 
                pass
        active_marker_windows = []
        self.print_console("All markers destroyed.", status="Info")

    def _show_position_markers(self):
        self.print_console("Displaying saved mouse position markers. Please observe your screen.", status="Info")
        
        
        
        
        if not hasattr(self, 'marker_root') or not self.marker_root.winfo_exists():
            self.marker_root = tk.Tk()
            self.marker_root.withdraw() 

        position_list = [
            ("Camera Button", self.switch_to_camera),
            ("Take Picture Button", self.take_picture),
            ("Send To Button", self.send_to),
            ("Shortcut Button", self.shortcut),
            ("Select All in Shortcut", self.select_all),
            ("Send Snap Button", self.send_snap_button),
        ]

        marker_count = 0
        for name, pos in position_list:
            if pos is not None and (pos.x != 0 or pos.y != 0): 
                marker_count += 1
                marker = PositionMarker(self.marker_root, pos.x, pos.y, marker_count, name)
            elif name == "Camera Button" and self.platform_mode == "web":
                self.print_console(f"Skipping marker for '{name}' (not needed for Web platform).", status="Marker")
            else:
                self.print_console(f"Position '{name}' not set (0,0). Skipping marker.", status="Warning")
        
        if marker_count > 0:
            self.print_console("Markers are displayed. Press F to destroy markers and continue.", status="Marker")
            
            
            while not keyboard.is_pressed("f"):
                self.marker_root.update_idletasks() 
                self.marker_root.update() 
                time.sleep(0.05) 
            self._destroy_all_markers()
            
            while keyboard.is_pressed("f"):
                time.sleep(0.05)
        else:
            self.print_console("No valid positions found to display markers.", status="Warning")

    def get_positions(self):
        self.print_console("Make sure your snapchat is open and you are on the chats page.", status="Setup")
        if self.platform_mode == "android":
            self.print_console("Move your mouse to the camera button, then press F", status="Setup")
            while True:
                if keyboard.is_pressed("f"):
                    self.switch_to_camera = pyautogui.position()
                    break
            time.sleep(0.5)
        else: 
            self.switch_to_camera = None 
        self.print_console("Move your mouse to the take picture button, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
    
        self.print_console("Move your mouse to the Send To button, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to your shortcut, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to select all in shortcut, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.select_all = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to send snap button, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.send_snap_button = pyautogui.position()
                break
    
        self._save_positions() 
        self.print_console("All positions calibrated and saved.", status="Setup")

    def send_snap(self, shortcut_users):
        self.sent_snaps += shortcut_users 
        
        self.update_title(shortcut_users)
        self._refresh_console_display() 

        
        if self.platform_mode == "android":
            pyautogui.moveTo(self.switch_to_camera)
            if not self.interruptible_sleep(self.delay): return False 
            pyautogui.click()

        pyautogui.moveTo(self.take_picture)
        if not self.interruptible_sleep(self.delay): return False
        pyautogui.click()
    
        pyautogui.moveTo(self.send_to)
        if not self.interruptible_sleep(self.delay): return False
        pyautogui.click()

        pyautogui.moveTo(self.shortcut)
        if not self.interruptible_sleep(self.delay): return False
        pyautogui.click()

        pyautogui.moveTo(self.select_all)
        if not self.interruptible_sleep(self.delay): return False
        pyautogui.click()

        pyautogui.moveTo(self.send_snap_button)
        if not self.interruptible_sleep(self.delay): return False
        pyautogui.click()

        return True 
    
    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps
        if onLinux() == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Snapchat Score PLUS v1.2| Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @FlazeIGuess with help of @useragents on Github")

    def print_console(self, arg, status = "Console"):
        log_message = f"[{status}] {arg}"
        if status == "Error":
            self.logger.error(log_message)
        elif status == "Warning":
            self.logger.warning(log_message)
        elif status == "Info" or status == "Console" or status == "Setup" or status == "Settings" or status == "Delay Selection" or status == "Post-Snap Delay Selection" or status == "Platform Selection" or status == "Status":
            self.logger.info(log_message)
        
        
        
        
        
        
        if status != "Progress": 
            lines = arg.split('\n')
            
            indentation_len = 7 + len(f"[{status}] ") 
            
            print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {lines[0]}") 

            for i in range(1, len(lines)):
                
                print(f"{ ' ' * indentation_len}{lines[i]}")

    def _refresh_console_display(self):
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        
        print(Fore.RED + ascii_text)

        
        print(f"\n       {Fore.WHITE}[{Fore.RED}Info{Fore.WHITE}] You can pause the script at any time by pressing CTRL+Q (even if this window is not focused).")
        
        
        ascii_count_lines = snapchat._get_ascii_number_lines(self.sent_snaps)
        print(f"\n       {Fore.WHITE}[{Fore.RED}Progress{Fore.WHITE}] Sent Snaps:")
        for line in ascii_count_lines:
            print(f"       {Fore.WHITE} {line}") 

        
        if self._current_status_message:
            self.print_console(self._current_status_message, status="Status")
        
        sys.stdout.flush() 

    def main(self):
        if onLinux() == False:
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score PLUS v1.2| Developed by @FlazeIGuess with help of @useragents on Github")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        
        config_file = 'config.ini'
        if os.path.exists(config_file):
            self.config.read(config_file)
            self.print_console(f"Successfully read config file '{config_file}'.", status="Info")
        else:
            self.print_console(f"Config file '{config_file}' not found. Will use default/manual settings.", status="Warning")

        while True:
            try:
                self.print_console("Select your Snapchat platform:", status="Platform Selection")
                self.print_console("0: Snapchat Web/Microsoft Store App", status="Platform Selection")
                self.print_console("1: Android Device via USB Debugging (scrcpy) |Recommended| or Emulator |Not Recommended|", status="Platform Selection")
                platform_choice = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Platform Selection{Fore.WHITE}] Enter choice (0 or 1): "))
                if platform_choice not in [0, 1]:
                    raise ValueError
                self.platform_mode = "web" if platform_choice == 0 else "android"
                break
            except ValueError:
                self.print_console("Invalid input. Please enter 0 for Web/Microsoft Store App or 1 for Android.", status="Platform Selection")

        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)

        
        if self._has_saved_positions():
            while True:
                try:
                    self.print_console("Mouse Positions Setup:", status="Setup")
                    self.print_console("0: Calibrate new positions", status="Setup")
                    self.print_console("1: Load saved positions from config.ini", status="Setup")
                    self.print_console("2: Show markers for saved positions", status="Setup")
                    position_choice = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Setup{Fore.WHITE}] Enter choice (0, 1 or 2): "))
                    if position_choice not in [0, 1, 2]:
                        raise ValueError
                    break
                except ValueError:
                    self.print_console("Invalid input. Please enter 0, 1 or 2.", status="Setup")
        else:
            self.print_console("No saved positions found. You must calibrate new positions.", status="Setup")
            self.print_console("0: Calibrate new positions", status="Setup")
            position_choice = 0 

        if position_choice == 0: 
            self.get_positions()
        elif position_choice == 1: 
            if not self._load_positions():
                self.print_console("Failed to load positions. Please calibrate new positions.", status="Warning")
                self.get_positions()
        elif position_choice == 2: 
            if self._load_positions():
                self._show_position_markers()
                time.sleep(0.5) 

                while True:
                    self.print_console("Markers shown. Do you want to: ", status="Setup")
                    self.print_console("0: Continue with loaded positions", status="Setup")
                    self.print_console("1: Recalibrate positions", status="Setup")
                    marker_action_choice = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Setup{Fore.WHITE}] Enter choice (0 or 1): "))
                    if marker_action_choice == 0:
                        break
                    elif marker_action_choice == 1:
                        self.get_positions()
                        break
                    else:
                        self.print_console("Invalid input. Please enter 0 or 1.", status="Error")
            else:
                self.print_console("No positions loaded to show markers. Please calibrate or load first.", status="Warning")
                self.get_positions() 

        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)

        
        while True:
            try:
                self.print_console("Do you want to load settings from config.ini?", status="Settings")
                self.print_console("0: No, enter manually", status="Settings")
                self.print_console("1: Yes, use config.ini", status="Settings")
                self.print_console("2: Exit", status="Settings")
                config_choice = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Settings{Fore.WHITE}] Enter choice (0, 1 or 2): "))
                if config_choice not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                self.print_console("Invalid input. Please enter 0, 1 or 2.", status="Settings")

        if config_choice == 2:
            self.print_console("Exiting script.", status="Console")
            self._should_quit = True
            return 

        use_config = (config_choice == 1)
        config_loaded_successfully = False

        
        if not self.config.has_section('Settings'):
            self.config.add_section('Settings')

        if use_config:
            config_loaded_successfully = self._load_config()
            if not config_loaded_successfully:
                self.print_console("Falling back to manual input due to config file error.", status="Warning")
                use_config = False 

        if not use_config:
            while True: 
                try:
                    shortcut_users_input = input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut ({self._config_shortcut_users if use_config and config_loaded_successfully else 'e.g. 100'}): ")
                    if shortcut_users_input.strip() == "" and use_config and config_loaded_successfully:
                        shortcut_users = self._config_shortcut_users
                    else:
                        shortcut_users = int(shortcut_users_input)
                    break
                except ValueError:
                    print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] There was an error with that input, please try again :) ")

            
            self.config.set('Settings', 'shortcut_users', str(shortcut_users))

            if onLinux() == False:
                os.system("cls")
            else:
                os.system("clear")
            print(Fore.RED + ascii_text)
            
            while True:
                try:
                    self.print_console("This delay sets the time between each click action.", status="Delay Explanation")
                    print(f"\n")
                    self.print_console("Fast PC/Smartphone -> 400 / 500", status="Delay Selection")
                    self.print_console("Mid PC/Smartphone -> 800 / 1000", status="Delay Selection")
                    self.print_console("Slow PC/Smartphone -> 1300 / 1500", status="Delay Selection")
                    print(f"\n")
                    self.print_console("This delay sets the time between each click action.", status="Delay Explanation")
                    self.print_console(f"Enter delay in milliseconds (e.g., 1300 for 1.3 seconds) ({int(self.delay * 1000) if use_config and config_loaded_successfully else '1300'}):", status="Delay Selection")
                    delay_input = input(f"\n       {Fore.WHITE}[{Fore.RED}Delay Selection{Fore.WHITE}] Input: ")
                    if delay_input.strip() == "" and use_config and config_loaded_successfully:
                        delay_ms = int(self.delay * 1000)
                    else:
                        delay_ms = int(delay_input)
                    if delay_ms < 400:
                        self.print_console("Delays under 400ms may not be accurately recognized by the system.", status="Warning")
                    self.delay = delay_ms / 1000.0
                    break
                except ValueError:
                    print(f"\n       {Fore.WHITE}[{Fore.RED}Delay Selection{Fore.WHITE}] Invalid input. Please enter a valid number for delay.")

            
            self.config.set('Settings', 'delay_ms', str(int(self.delay * 1000)))

            if onLinux() == False:
                os.system("cls")
            else:
                os.system("clear")
            print(Fore.RED + ascii_text)
            while True:
                try:
                    
                    self.print_console("This delay sets the time to wait after sending a batch of snaps.", status="Post-Snap Delay Explanation")
                    
                    print(f"\n")
                    self.print_console(f"Enter delay after sending snaps in milliseconds (e.g., 4000 for 4 seconds) ({int(self.post_snap_delay * 1000) if use_config and config_loaded_successfully else '4000'}) or leave blank:", status="Post-Snap Delay Selection")
                    self.print_console("Leave blank to use the same delay as between clicks.", status="Post-Snap Delay Info")
                    post_snap_delay_input = input(f"\n       {Fore.WHITE}[{Fore.RED}Post-Snap Delay Selection{Fore.WHITE}] Input: ")
                    if post_snap_delay_input.strip() == "" and use_config and config_loaded_successfully:
                        self.post_snap_delay = self.post_snap_delay 
                    elif post_snap_delay_input.strip() == "":
                        self.post_snap_delay = self.delay
                    else:
                        post_snap_delay_ms = int(post_snap_delay_input)
                        if post_snap_delay_ms < 0:
                            raise ValueError
                        self.post_snap_delay = post_snap_delay_ms / 1000.0
                    break
                except ValueError:
                    print(f"\n       {Fore.WHITE}[{Fore.RED}Post-Snap Delay Selection{Fore.WHITE}] Invalid input. Please enter a non-negative number or leave blank.")
            
            
            self.config.set('Settings', 'post_snap_delay_ms', str(int(self.post_snap_delay * 1000)))

            if onLinux() == False:
                os.system("cls")
            else:
                os.system("clear")
            print(Fore.RED + ascii_text)
            while True:
                try:
                    self.print_console(f"Enter target number of snaps to send (0 for no limit) ({self._config_target_snaps if use_config and config_loaded_successfully else '0'}):", status="Target Snaps")
                    target_snaps_input = input(f"\n       {Fore.WHITE}[{Fore.RED}Target Snaps{Fore.WHITE}] Input: ")
                    if target_snaps_input.strip() == "":
                        self.target_snaps = 0
                    else:
                        self.target_snaps = int(target_snaps_input)
                    if self.target_snaps < 0:
                        raise ValueError
                    break
                except ValueError:
                    print(f"\n       {Fore.WHITE}[{Fore.RED}Target Snaps{Fore.WHITE}] Invalid input. Please enter a non-negative number.")

            
            self.config.set('Settings', 'target_snaps', str(self.target_snaps))

            self._save_config() 

        else: 
            shortcut_users = self._config_shortcut_users
            self.target_snaps = self._config_target_snaps 

        self.print_console("Please navigate to your chats and ensure Snapchat is open. Press F when you're ready.", status="Console")

        while True:
            if keyboard.is_pressed("f"):
                break
        time.sleep(0.5)
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        self.print_console("Sending snaps...")
        self.started_time = time.time()
        self.last_mouse_pos = pyautogui.position()
        self._current_status_message = "Sending snaps..." 
        self._refresh_console_display()
        while True:
            if self._should_quit or self._should_reset:
                break

            current_mouse_pos = pyautogui.position()
            if self.last_mouse_pos is not None:

                move_threshold = 5
                if not self.paused and (abs(current_mouse_pos.x - self.last_mouse_pos.x) > move_threshold or abs(current_mouse_pos.y - self.last_mouse_pos.y) > move_threshold):
                    self.paused = True
                    self._current_status_message = "Mouse moved. Script paused. Press F to resume, R to reset, or Q to quit."
                    self._refresh_console_display() 
                
                    while self.paused:
                        time.sleep(0.1) 
            self.last_mouse_pos = current_mouse_pos

            
            if not self.paused:
                
                
                if not self.send_snap(shortcut_users): 
                    continue 
                
                if self.target_snaps > 0 and self.sent_snaps >= self.target_snaps:
                    self.print_console(f"Target of {self.target_snaps} snaps reached. Script stopping.", status="Info")
                    self._should_quit = True
                    break 

                if not self.interruptible_sleep(self.post_snap_delay):
                    continue 
                self.last_mouse_pos = pyautogui.position() 
            else:
                
                time.sleep(0.1) 

            
        self.print_console(f"Finished sending {self.sent_snaps} snaps.")

    def interruptible_sleep(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            
            if self._should_quit or self._should_reset or self.paused:
                return False  
            time.sleep(0.05)  
        
        return True  

    def global_pause(self):
        if not self.paused:
            self.paused = True
            self._current_status_message = "Global pause hotkey (CTRL+Q) detected. Script paused. Press F to resume, R to reset, or Q to quit."
            self._refresh_console_display()

    def resume_script(self):
        if self.paused:
            time.sleep(0.1) 
            self.paused = False
            self._current_status_message = "Sending snaps..." 
            self._refresh_console_display()
            self.last_mouse_pos = pyautogui.position() 
            
            while keyboard.is_pressed("f"):
                time.sleep(0.05)

    def reset_script(self):
        if self.paused:
            time.sleep(0.1) 
            self.paused = False
            self._should_reset = True
            self._current_status_message = "Resetting script..."
            self._refresh_console_display()

    def quit_script(self):
        if self.paused:
            time.sleep(0.1) 
            self.paused = False
            self._should_quit = True
            self._current_status_message = "Quitting script..."
            self._refresh_console_display()
            self._destroy_all_markers() 

    def _has_saved_positions(self):
        if not self.config.has_section('Positions'):
            return False
        
        position_names = ["switch_to_camera", "take_picture", "send_to", "shortcut", "select_all", "send_snap_button"]
        for name in position_names:
            try:
                x = int(self.config.get('Positions', f'{name}_x'))
                y = int(self.config.get('Positions', f'{name}_y'))
                if x != 0 or y != 0:
                    return True 
            except (configparser.NoOptionError, ValueError):
                continue 
        return False 

obj = snapchat()


keyboard.add_hotkey('ctrl+q', obj.global_pause)
keyboard.add_hotkey('f', obj.resume_script)
keyboard.add_hotkey('r', obj.reset_script)
keyboard.add_hotkey('q', obj.quit_script)

while True:
    obj.main()
    if not obj._should_reset:
        break 
    

if obj._should_quit:
    obj._destroy_all_markers() 
    obj.marker_root.quit() 
    sys.exit()
