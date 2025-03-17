# main.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui import start_gui

if __name__ == "__main__":
    start_gui()