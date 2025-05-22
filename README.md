# Snapchat Snapscore PLUS

Boost your Snapchat Snapscore with ease using this automation script.

## Features

- Automates sending snaps to a selected Snapchat shortcut.
- Customizable delay between actions.
- Pause and resume the script by moving the mouse.
- Reset or quit the script from the paused state.
- Tracks and displays the number of snaps sent.

## How to Use

<details>
<summary>Using with Android Phone via USB Debugging</summary>

1.  **Install Python:** Download and install Python from the official website. Make sure to check the option 'Add Python to PATH' during installation.
2.  **Install ADB:** Follow a guide online to install ADB for your operating system. Ensure the `adb` command is accessible from your terminal.
3.  **Install scrcpy:** Install scrcpy. You can usually install it via package managers (e.g., `choco install scrcpy` on Windows, `brew install scrcpy` on macOS, `sudo apt install scrcpy` on Debian/Ubuntu).
4.  **Enable USB Debugging:** On your Android phone, go to `Settings` -> `About Phone` and tap 'Build number' seven times to enable Developer Options. Then go back to `Settings`, find `Developer Options`, and enable 'USB debugging'.
5.  **Connect your phone:** Connect your Android phone to your computer via USB.
6.  **Verify ADB connection:** Open a terminal or command prompt and run `adb devices`. You should see your device listed. If prompted on your phone, allow USB debugging from your computer.
7.  **Start scrcpy:** Run `scrcpy` in your terminal. This should open a window displaying your phone screen.
8.  **Install Dependencies:** Navigate to the script's directory in your terminal. Run the following command to install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
9.  **Run the Script:** Execute the main Python script:
    ```bash
    python main.py
    ```
10. **Follow On-Screen Instructions:** The script will guide you through the setup:
    *   Ensure Snapchat is open on your phone (displayed via scrcpy) and you are on the chats page.
    *   During the calibration phase, the script will ask you to move your mouse to specific buttons (Camera, Take Picture, Send To, Shortcut, Select All, Send Snap Button) displayed in the scrcpy window and press `F` to record their positions.
    *   Enter the number of people in your Snapchat shortcut.
    *   Select or enter the desired delay in milliseconds between click actions.
    *   Enter the delay in seconds to wait after sending a batch of snaps.
11. **Start Sending:** Navigate to your chats page in Snapchat (via the scrcpy window) and press `F` when prompted to start sending snaps.
12. **Pause/Resume/Control:**
    *   The script will automatically pause if you move your mouse.
    *   Press `F` while paused to resume.
    *   Press `R` while paused to reset the script (starts calibration again).
    *   Press `Q` while paused to quit the script.

</details>

<details>
<summary>Using with Android Emulator</summary>

1.  **Install Python:** Download and install Python from the official website. Make sure to check the option 'Add Python to PATH' during installation.
2.  **Install Dependencies:** Navigate to the script's directory. Run the `Install Requirements.bat` file (for Windows) or `pip install -r requirements.txt` (for other OS) to install the required Python libraries.
3.  **Install Android Emulator:** Download and install an Android emulator like NoxPlayer.
4.  **Install and Login to Snapchat:** Download and install the Snapchat app within the emulator and log in to your account.
5.  **Create Shortcut:** On the Snapchat app within the emulator, create a shortcut with the people you want to send snaps to.
6.  **Run the Script:** Execute the main Python script:
    ```bash
    python main.py
    ```
7.  **Follow On-Screen Instructions:** The script will guide you through the setup:
    *   Ensure Snapchat is open in the emulator and you are on the chats page.
    *   During the calibration phase, the script will ask you to move your mouse to specific buttons (Camera, Take Picture, Send To, Shortcut, Select All, Send Snap Button) displayed in the emulator window and press `F` to record their positions.
    *   Enter the number of people in your Snapchat shortcut.
    *   Select or enter the desired delay in milliseconds between click actions.
    *   Enter the delay in seconds to wait after sending a batch of snaps.
8.  **Start Sending:** Navigate to your chats page in Snapchat (within the emulator) and press `F` when prompted to start sending snaps.
9.  **Pause/Resume/Control:**
    *   The script will automatically pause if you move your mouse.
    *   Press `F` while paused to resume.
    *   Press `R` while paused to reset the script (starts calibration again).
    *   Press `Q` while paused to quit the script.

</details>

## Disclaimer

This script was created for educational purposes. Use at your own risk. The developer is not responsible for any consequences resulting from the use of this script.

## Development

Developed by @FlazeIGuess with help of @useragents on Github.
