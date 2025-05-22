try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time, platform
   from datetime import datetime
   import sys
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """

     _______  __    _  _______  _______    _______  ___      __   __  _______ 
    |       ||  |  | ||   _   ||       |  |       ||   |    |  | |  ||       |
    |  _____||   |_| ||  |_|  ||    _  |  |    _  ||   |    |  | |  ||  _____|
    | |_____ |       ||       ||   |_| |  |   |_| ||   |    |  |_|  || |_____ 
    |_____  ||  _    ||       ||    ___|  |    ___||   |___ |       ||_____  |
     _____| || | |   ||   _   ||   |      |   |    |       ||       | _____| |
    |_______||_|  |__||__| |__||___|      |___|    |_______||_______||_______|
    
    by @FlazeIGuess with help of @useragents on Github                                                                                        
"""
                       
def onLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

class snapchat:

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3
        self.post_snap_delay = 4 # Default value
        self.paused = False
        self.last_mouse_pos = None
        self._should_quit = False
        self._should_reset = False

    def get_positions(self):
        self.print_console("Make sure your snapchat is open and you are on the chats page.", status="Setup")
        self.print_console("Move your mouse to the camera button, then press F", status="Setup")
        while True:
            if keyboard.is_pressed("f"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(0.5)
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
    
    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)
        pyautogui.moveTo(self.switch_to_camera)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        self.sent_snaps += shortcut_users
        self.update_title(shortcut_users)
        self.print_console(f"Sent {self.sent_snaps} total snaps so far.", status="Progress")
    
    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps
        if onLinux() == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Snapchat Score PLUS| Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @FlazeIGuess with help of @useragents on Github")

    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        if onLinux() == False:
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score PLUS| Developed by @FlazeIGuess with help of @useragents on Github")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        self.get_positions()

        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        while True: 
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut: "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] There was an error with that input, please try again :) ")


        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        
        while True:
            try:
                
                self.print_console("", status="Select the delay for your PC/Smartphone")
                print(f"\n")
                self.print_console("Fast PC/Smartphone -> 400 / 500", status="Delay Selection")
                self.print_console("Mid PC/Smartphone -> 800 / 1000", status="Delay Selection")
                self.print_console("Slow PC/Smartphone -> 1300 / 1500", status="Delay Selection")
                print(f"\n")
                self.print_console("This delay sets the time between each click action.", status="Delay Explanation")
                delay_ms = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Delay Selection{Fore.WHITE}] Enter delay in milliseconds (e.g., 1300 for 1.3 seconds): "))
                if delay_ms < 400:
                    raise ValueError
                self.delay = delay_ms / 1000.0
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Delay Selection{Fore.WHITE}] Invalid input. Please enter a number 400 or higher.")
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        while True:
            try:
                
                self.print_console("This delay sets the time to wait after sending a batch of snaps.", status="Post-Snap Delay Explanation")
                print(f"\n")
                post_snap_delay_s = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Post-Snap Delay Selection{Fore.WHITE}] Enter delay after sending snaps in seconds (e.g., 4): "))
                if post_snap_delay_s < 0:
                    raise ValueError
                self.post_snap_delay = post_snap_delay_s
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Post-Snap Delay Selection{Fore.WHITE}] Invalid input. Please enter a non-negative number.")
        

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
        while True:
            if keyboard.is_pressed("f"):
                break
            current_mouse_pos = pyautogui.position()
            if self.last_mouse_pos is not None:

                move_threshold = 5
                if not self.paused and (abs(current_mouse_pos.x - self.last_mouse_pos.x) > move_threshold or abs(current_mouse_pos.y - self.last_mouse_pos.y) > move_threshold):
                    self.paused = True
                    self.print_console("Mouse moved. Script paused. Press F to resume, R to reset, or Q to quit.", status="Paused")
                
                    while self.paused:
                        if keyboard.is_pressed("f"):
                    
                            time.sleep(0.5)
                            self.paused = False
                            self.print_console("Resuming script.", status="Resuming")
                            break
                        elif keyboard.is_pressed("r"):
                            time.sleep(0.5)
                            self.paused = False
                            self._should_reset = True
                            self.print_console("Resetting script...", status="Console")
                            break
                        elif keyboard.is_pressed("q"):
                            time.sleep(0.5)
                            self.paused = False
                            self._should_quit = True
                            self.print_console("Quitting script...", status="Console")
                            break
                        time.sleep(0.1) 
            self.last_mouse_pos = current_mouse_pos

            
            if not self.paused:
                self.send_snap(shortcut_users)
                time.sleep(self.post_snap_delay) 

            
            if self._should_quit or self._should_reset:
                break #

        self.print_console(f"Finished sending {self.sent_snaps} snaps.")

obj = snapchat()

while True:
    obj.main()
    if not obj._should_reset:
        break 
    

if obj._should_quit:
    sys.exit()
