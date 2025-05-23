# Snapchat Snapscore Booster PLUS

Boost your Snapchat Snapscore with ease using this automation script.

---
## ✨ Features

* Automates sending snaps to a selected Snapchat shortcut
* Adjustable delays between actions
* Mouse-movement pause control
* Resume, restart or quit from paused mode
* Snap counter included

---

## 🚀 Quick Start Options

Choose the setup method that suits you best:

---

### 🌐 Option 1: Snapchat Web or Microsoft Store App (Fast & Simple)

1. **Use Snapchat Web**  
   Go to [Snapchat Web](https://web.snapchat.com/), log in, and keep the window open.  
   This version has limited functionality but works for manual or automated Snapscore boosting.

2. **Use Snapchat from Microsoft Store**  
   Install [Snapchat from the Microsoft Store](https://apps.microsoft.com/store/detail/snapchat/9NL4J1B0Q61N).  
   This version is more stable than Android emulators and can be controlled using automation tools like AutoHotkey or this script (with slight adaptations).  
   > ⚠️ Calibration may need to be adjusted manually due to UI differences.
   Recommendation:
   - Because Snapchat web doesn't have an extra Chat site just use the first and second calibration on the shutter button, everything else should be the same as Android.
   

These alternatives are easier to set up than emulators and work well for simple Snapscore automation.

---

### 📱 Option 2: Android Device via USB Debugging (Recommended)

1. **Download this script**  
   Clone the repository or [download it as ZIP](https://github.com/FlazeIGuess/Snapchat-Snapscore-Booster-PLUS/archive/refs/heads/main.zip) and extract it.

2. **Install Python 3.9**  
   [Download here](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) and check **“Add Python to PATH”** during setup.

3. **Install dependencies**  
   Double-click `Install Requirements.bat` or run `pip install -r requirements.txt` in the script folder.

4. **Enable USB debugging on your Android phone**  
   - Go to *Settings → About phone → Tap Build number 7 times*  
   - Then enable *Developer options → USB debugging*  
   [Video guide](https://www.youtube.com/watch?v=G_Xw3336xLQ)

5. **Install ADB + scrcpy**  
   - ADB: `choco install adb` (Windows)  
   - scrcpy: `choco install scrcpy` (Windows), `brew install scrcpy` (macOS), or `sudo apt install scrcpy` (Linux)

6. **Connect your phone via USB** and allow debugging when prompted.

7. **Start scrcpy** to mirror your phone’s screen.

8. **Run the script**  
   Double-click `run.bat` or run `python main.py` in the script directory.

9. **Follow the on-screen setup**  
   - Stay on the *Chats* screen in Snapchat  
   - Hover the mouse over each button (Camera, Snap, Send To, Shortcut, Select All, Send) and press **F** to record positions  
   - Enter recipient count, click delay (ms), and rest delay (s)

10. **Script controls**
   - Move mouse → Pause  
   - Press **F** while paused → Resume  
   - Press **R** while paused → Restart calibration  
   - Press **Q** while paused → Quit

---

### ⚠️ Important Notice: Emulator Use is Unstable

Using Snapchat inside Android emulators like BlueStacks, NoxPlayer, or LDPlayer is **highly unreliable**. Snapchat actively detects and restricts virtual devices. Expect:
- Login errors
- Black screens
- App crashes

For best results, use a real Android phone.

---

### 🧪 Option 3: Android Emulator (Experimental / Not Recommended)

1. **Download this script** (see Option 2)

2. **Install Python 3.9** and dependencies  
   Use `Install Requirements.bat` or run `pip install -r requirements.txt`.

3. **Install an Android emulator**  
   e.g. [NoxPlayer](https://www.bignox.com/) or [LDPlayer](https://www.ldplayer.net/)

4. **Install and log in to Snapchat** inside the emulator

5. **Create a Snapchat Shortcut** with the recipients you want to automate

6. **Run the script**  
   Launch `run.bat` or run `python main.py`

7. **Follow the same calibration process** as described in Option 2

> ⚠️ Use at your own risk – emulator compatibility may break without notice.

---


## 📦 Helpful Downloads

| Purpose                    | Link                                                                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Python 3.9.2 (Windows x64) | [Download](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)                                                       |
| This Script (ZIP)          | [Download](https://github.com/FlazeIGuess/Snapchat-Snapscore-Booster-PLUS/archive/refs/heads/main.zip)                         |
| ADB platform tools         | [Google Platform Tools](https://developer.android.com/tools/releases/platform-tools)                                            |
| scrcpy                     | [GitHub - Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)                                                              |
| USB debugging tutorial     | [YouTube Guide](https://www.youtube.com/watch?v=G_Xw3336xLQ)                                                                     |

---

## ⚠️ Disclaimer

This script is provided **for educational purposes only**.  
Use it at your own risk. The developer assumes **no responsibility** for bans, data loss, or other consequences.

---

## 👨‍💻 Development

Created by **@FlazeIGuess** with support from **@useragents** on GitHub.  
Feel free to open issues or submit pull requests to improve the project.
