import os
import winreg as reg

def set_reg_wallpaper_path(path=os.path.expanduser('~/wallpaper.png')):
    key_path = r"Control Panel\Desktop"
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
    reg.SetValueEx(key, "Wallpaper", 0, reg.REG_SZ, path)
    reg.CloseKey(key)

if __name__ == "__main__":
    set_reg_wallpaper_path()