# Auto Typer GUI

## Overview
This Python program provides a simple graphical user interface (GUI) for automating typing tasks. It allows users to load a text file and simulate typing the content of that file onto the screen.

## Features
- **File Loading:** Users can browse and select a text file containing the content they want to type.
- **Error Handling:** If the selected file cannot be read due to Unicode decoding issues, an error message is displayed.
- **Typing Simulation:** Once a file is loaded, users can initiate the typing simulation. The program waits for a few seconds to allow the user to position the cursor in the desired input field before starting the typing process.
- **Customizable Typing Speed:** The interval between each character's typing can be adjusted.

## Libraries Used
- **Tkinter:** Tkinter is used for creating the GUI components, such as buttons and windows.
- **filedialog:** This module from Tkinter is used to provide a file browsing dialog for selecting text files.
- **messagebox:** Another module from Tkinter, messagebox is used to display error messages.
- **pyautogui:** PyAutoGUI is used for simulating keyboard typing actions. It allows programmatically controlling the mouse and keyboard to automate interactions with other applications.

## How to Use
1. Run the program.
2. Click on the "Browse" button to select a text file containing the content you want to type.
3. If the file is successfully loaded, the "Start Typing" button becomes enabled.
4. Position your cursor in the desired input field.
5. Click on the "Start Typing" button to initiate the typing simulation.

## Notes
- Ensure that the selected text file is in a readable format.
- Depending on the application or website, you may need to adjust the typing speed interval for optimal performance.

## Disclaimer
This program is intended for educational and automation purposes only. Users are responsible for complying with all relevant laws and regulations when using this software. The developer assumes no liability for any misuse or unlawful use of this program.
