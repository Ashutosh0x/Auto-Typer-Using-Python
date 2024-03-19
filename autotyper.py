import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time

class AutoTyperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer GUI")

        # Create a button to browse for the file
        self.browse_button = tk.Button(root, text="Browse", command=self.load_file)
        self.browse_button.pack()

        # Create a button to start typing
        self.type_button = tk.Button(root, text="Start Typing", command=self.start_typing, state=tk.DISABLED)
        self.type_button.pack()

        # Variable to store the content of the file
        self.file_content = ""

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.file_content = file.read()
                self.type_button['state'] = tk.NORMAL
            except UnicodeDecodeError as e:
                messagebox.showerror("Error", "Unicode Decode Error: the file you are trying to open cannot be read.")
                self.file_content = ""
                self.type_button['state'] = tk.DISABLED

    def start_typing(self):
        # Wait a few seconds to allow the user to place the cursor in the correct input field
        time.sleep(5)
        pyautogui.write(self.file_content, interval=0.05)

# Create the main window
root = tk.Tk()
app = AutoTyperGUI(root)
root.mainloop()
