# Snapchat Snapscore PLUS

Boost your Snapchat Snapscore with ease using this automation script.

---

## 🏁 Quick-Start (Windows)

1. **Install Python 3.9** – [Download the official installer](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) and tick **“Add Python to PATH”** during setup.
2. **Install all Python dependencies** – simply double-click **`Install Requirements.bat`** (this runs `pip install -r requirements.txt` for you).
3. **Enable USB debugging** on your Android phone (see the detailed guide below).
4. **Run the script** – double-click **`run.bat`** (it launches `python main.py` in the correct folder).

> **Tip for macOS / Linux users**
> *Install dependencies*: `pip install -r requirements.txt`
> *Run the script*: `python main.py`

---

## ⚠️  Important notice about Android emulators

Running Snapchat inside an Android emulator such as BlueStacks, NoxPlayer or LDPlayer **is extremely unreliable and often fails** – Snapchat actively blocks most virtual devices. Expect login errors, camera crashes or a black screen.
**Use a real device connected via USB whenever possible.** (ADB + scrcpy are lightweight and require zero installation on the handset.)

You can still try – the legacy instructions remain in a collapsed section below – but **there are no guarantees**.

---

## Features

* Automates sending snaps to a selected Snapchat shortcut.
* Customisable delay between actions.
* Pause and resume the script by moving the mouse.
* Reset or quit the script from the paused state.
* Tracks and displays the number of snaps sent.

---

## How to Use

<details>
<summary>Using a real Android phone via USB debugging (recommended)</summary>

1. **Install Python** (see Quick-Start above).
2. **Install ADB platform tools** – Download the latest package from Google and extract it, or install via e.g. Chocolatey: `choco install adb`.
3. **Install scrcpy** – e.g. `choco install scrcpy` (Windows), `brew install scrcpy` (macOS) or `sudo apt install scrcpy` (Debian/Ubuntu).
4. **Enable USB debugging** – On your phone go to *Settings → About phone* and tap *Build number* seven times, then enable *Developer options → USB debugging*.
   [Video guide](https://www.youtube.com/watch?v=G_Xw3336xLQ).
5. **Connect the phone** via USB and authorise the PC.
6. **Verify the connection**: `adb devices` should list your handset.
7. **Start scrcpy** to mirror the screen.
8. **Install dependencies** – double-click **`Install Requirements.bat`** **or** run `pip install -r requirements.txt`.
9. **Run the script** – double-click **`run.bat`** **or** run `python main.py`.
10. **Follow the on-screen instructions**:

    * Open Snapchat (mirrored in the scrcpy window) and stay on the *Chats* page.
    * During calibration move the mouse to each button (Camera, Take Picture, Send To, Shortcut, Select All, Send) and press **F** to record its position.
    * Enter the number of recipients in your Snapchat shortcut.
    * Choose the click delay (ms) and the rest delay (s) between batches.
11. **Control keys**:

    * Move the mouse → **pause**.
    * **F** while paused → resume.
    * **R** while paused → restart calibration.
    * **Q** while paused → quit.

</details>

<details>
<summary>Using an Android emulator (experimental / not recommended)</summary>

> **Warning:** Snapchat heavily restricts emulator usage – this may not work at all.

1. **Install Python** (see Quick-Start).
2. **Install dependencies** – double-click **`Install Requirements.bat`** **or** run `pip install -r requirements.txt`.
3. **Install an Android emulator** (e.g. NoxPlayer).
4. **Install & log in to Snapchat** inside the emulator.
5. **Create a Shortcut** in Snapchat with the desired recipients.
6. **Run the script** – double-click **`run.bat`** **or** run `python main.py`.
7. **Follow the same calibration and control steps** as described for a real device.

</details>

---

## Helpful Downloads

| Purpose                    | Link                                                                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Python 3.9.2 (Windows x64) | [https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) |
| ADB platform tools         | [https://developer.android.com/tools/releases/platform-tools](https://developer.android.com/tools/releases/platform-tools)       |
| scrcpy                     | [https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)                                                     |
| USB debugging tutorial     | [https://www.youtube.com/watch?v=G\_Xw3336xLQ](https://www.youtube.com/watch?v=G_Xw3336xLQ)                                      |

---

## Disclaimer

This script is provided **for educational purposes only**. Use it at your own risk. The developer accepts no responsibility for any account bans, data loss or other consequences arising from its use.

---

## Development

Created by **@FlazeIGuess** with help from **@useragents** on GitHub.

Feel free to open issues or pull requests to improve the project.
