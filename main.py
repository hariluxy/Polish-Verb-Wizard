from GUI.ui import PolishVerbWizard
from tkinter import Tk

def main():
    # Start the GUI
    window = Tk()
    app = PolishVerbWizard(window)
    window.mainloop()

if __name__ == "__main__":
    main()
