import ctypes

def set_wallpaper(path):
    # SPI_SETDESKWALLPAPER is the system parameter info action to set the desktop background
    # 20 means SPI_SETDESKWALLPAPER
    # 0 means the action is being applied to all desktops
    # The third argument is the path to the wallpaper file
    # The last argument specifies how the system should use the uiParam parameter; 2 means update the user profile
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 2)

if __name__ == "__main__":
    # Replace 'your_wallpaper_path.jpg' with the path to your wallpaper image
    set_wallpaper('C:\\path\\to\\your\\wallpaper.jpg')
