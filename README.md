# Snapchat Snapscore Booster PLUS v1.2

Boost your Snapchat Snapscore with ease using this automation script.

---
## ✨ Features

* Automates sending snaps to a selected Snapchat shortcut
* Adjustable delays between actions
* Mouse-movement pause control
* Resume, restart or quit from paused mode
* Snap counter included
* **Configurable Settings:** Use `config.ini` to set default values for shortcut users, delays, and target snaps.
* **Detailed Logging:** All actions and important events are logged to `snapscore_booster.log` for easy troubleshooting.
* **Countdown Timers:** Visual countdowns are displayed during delays for better user feedback.
* **Target Snap Count:** Set a specific number of snaps to send, and the script will automatically stop once reached.

---
## Script controls
   - Press **CTRL+Q** → Pause (global hotkey, works anytime)
   - Press **F** while paused → Resume  
   - Press **R** while paused → Restart calibration  
   - Press **Q** while paused → Quit (works only when paused)
   - Press **CTRL+C** → Force quit (works anytime by closing console or sending interrupt signal)

## 🚀 Quick Start Options

Choose the setup method that suits you best:

---

### 🌐 Option 1: Snapchat Web or Microsoft Store App (Simple & Accessible)

1. **Download this script**  
   Clone the repo or [download it as ZIP](https://github.com/FlazeIGuess/SnapscoreBoosterPlus/releases/tag/Release) and extract it.

2. **Install Python 3.9**  
   [Download for Windows](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)  
   During setup, make sure to check **"Add Python to PATH"**.

3. **Install Python dependencies**  
   Double-click `Install Requirements.bat` or run `pip install -r requirements.txt` inside the script folder.

4. **Choose your Snapchat platform**:
   - **Snapchat Web**: Go to [web.snapchat.com](https://web.snapchat.com/), log in, and leave the window open.
   - **Microsoft Store App**: Install Snapchat from the [Microsoft Store](https://apps.microsoft.com/store/detail/snapchat/9NL4J1B0Q61N).

5. **Run the script**  
   Launch `run.bat` or run `python main.py`.

6. **Calibrate mouse positions**  
   Hover the cursor over the required buttons in the Snapchat interface (Camera, Snap, Send To, etc.) and press **F** to save each position.

7. **Follow the prompts**  
   You will be asked if you want to load settings from `config.ini` or enter them manually. Then, enter the number of recipients, timing preferences, and target snaps. Begin boosting your Snapscore.
   > ⚠️ Calibration may need to be adjusted manually due to UI differences.
   Recommendation:
   - Because Snapchat web doesn't have an extra Chat site just use the first and second calibration on the shutter button, everything else should be the same as Android.
   

These alternatives are easier to set up than emulators and work well for simple Snapscore automation.

---

### 📱 Option 2: Android Device via USB Debugging (Recommended) or Emulator (Not Recommended)

1. **Download this script**  
   Clone the repository or [download it as ZIP](https://github.com/FlazeIGuess/Snapchat-Snapscore-Booster-PLUS/archive/refs/heads/main.zip) and extract it.

2. **Install Python 3.9**  
   [Download here](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) and check **"Add Python to PATH"** during setup.

3. **Install dependencies**  
   Double-click `Install Requirements.bat` or run `pip install -r requirements.txt` in the script folder.

4. **Enable USB debugging on your Android phone** (if using a real device)  
   - Go to *Settings → About phone → Tap Build number 7 times*  
   - Then enable *Developer options → USB debugging*  
   [Video guide](https://www.youtube.com/watch?v=G_Xw3336xLQ)

5. **Install ADB + scrcpy**  
   - ADB: `choco install adb` (Windows)  
   - scrcpy: `choco install scrcpy` (Windows), `brew install scrcpy` (macOS), or `sudo apt install scrcpy` (Linux)

6. **Connect your phone via USB** and allow debugging when prompted (if using a real device).

7. **Start scrcpy** to mirror your phone's screen (if using Android).

8. **Run the script**  
   Double-click `run.bat` or run `python main.py` in the script directory.

9. **Follow the on-screen setup**  
   - Choose your platform (Android for this option).
   - Stay on the *Chats* screen in Snapchat  
   - Hover the mouse over each button (Camera [Android only], Snap, Send To, Shortcut, Select All, Send) and press **F** to record positions  
   - Enter recipient count, click delay (ms), and rest delay (ms), and target snaps.

---
## 🖱️ Mouse Position Management

To ensure the script interacts correctly with your Snapchat interface, you need to set up mouse positions. You have several options at the start of the script:

*   **0: Calibrate new positions:** Follow the on-screen prompts to move your mouse to each required button (Camera [Android only], Take Picture, Send To, Shortcut, Select All, Send Snap) and press **F** to record its coordinates. These positions will be automatically saved to `config.ini` for future use.
*   **1: Load saved positions from `config.ini`:** If you have previously calibrated and saved your positions, you can load them directly from `config.ini`. This skips the manual calibration step.
*   **2: Show markers for saved positions:** This option is helpful to verify if your saved positions are still accurate after resizing or moving your Snapchat window. The script will temporarily move your mouse cursor to each saved position, allowing you to visually confirm they align with the correct buttons. After showing the markers, you can choose to continue with the loaded positions or recalibrate if needed.
*   **3: Skip (continue without positions):** This will proceed without loading or calibrating positions. Use this only if you are confident your setup does not require precise mouse control or if you plan to manually handle mouse movements during the script's operation.

---

### ⚠️ Important Notice: Emulator Use is Unstable

Using Snapchat inside Android emulators like BlueStacks, NoxPlayer, or LDPlayer is **highly unreliable**. Snapchat actively detects and restricts virtual devices. Expect:
- Login errors
- Black screens
- App crashes

For best results, use a real Android phone.

---

## �� Helpful Downloads

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

## 🧪 Option 3: Android Emulator (Experimental / Not Recommended)

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

## ⚙️ Configuration (`config.ini`)

The script can load settings from `config.ini` to avoid manual input each time. A default `config.ini` is provided:

```ini
[Settings]
shortcut_users = 10         ; Default number of users in your Snapchat shortcut
delay_ms = 1300             ; Default delay between clicks in milliseconds
post_snap_delay_ms = 4000   ; Default delay after sending a batch of snaps in milliseconds (0 for no delay, or leave blank to use same as click delay)
target_snaps = 0            ; Target number of snaps to send (0 for no limit)
```

**To use `config.ini`:**
1. Ensure `config.ini` is in the same directory as `main.py`.
2. When running the script, select option `1` to load settings from `config.ini`.
3. You can modify these values directly in the file.

---
## 📝 Logging

The script generates a log file named `snapscore_booster.log` in the same directory. This file records:
* Script start and end times
* Important actions and events
* Errors and warnings

This log file is useful for debugging and tracking the script's activity over time.

---
## ✨ Enhanced User Experience

*   **Dynamic Snap Count:** The total number of snaps sent is now displayed dynamically in a visually appealing ASCII art format, updating on the same line without spamming the console.
