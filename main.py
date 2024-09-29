import tkinter as tk
from gui import VerbClassifierGUI # Import the GUI class from gui.py

def main():
    # Initialize the Tkinter window and launch the GUI
    root = tk.Tk()
    app = VerbClassifierGUI(root) # Create an instance of the VerbClassifierApp GUI
    root.geometry("400x200")
    root.mainloop()  # Start the Tkinter main event loop

if __name__ == "__main__":
    main()  # Call the main function to launch the program
