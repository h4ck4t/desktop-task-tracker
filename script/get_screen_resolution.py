import tkinter as tk

def get_screen_resolution():
    # Create a Tkinter root window but do not display it
    root = tk.Tk()
    root.withdraw()  # This will hide the main window

    # Get the screen width and height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Destroy the window to free up resources
    root.destroy()

    return width, height

if __name__ == '__main__':
    # Use the function and print the result
    screen_width, screen_height = get_screen_resolution()
    print(f"Screen resolution: {screen_width}x{screen_height}")
