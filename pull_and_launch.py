import subprocess
import shutil
import os
import pyautogui
import time

def run_git_pull():
    try:
        subprocess.check_call(['git', 'pull'])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

def upload_mod_file(mod_file, mods_dir):
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    pack_mod()
    shutil.copy(mod_file, mods_dir)

def pack_mod(folder_path, divine_path, mod_dest_path):
    root_dir = os.path.dirname(folder_path)
    mod_name = os.path.basename(folder_path)
    print('folder_path:' + str(folder_path))
    print('divine_path:' + str(divine_path))
    print('mod_dest_path:' + str(mod_dest_path))
    quit()
    pakpath = os.path.join(os.path.dirname(root_dir), "temp", f"{mod_name}.pak")
    mod_dir = os.path.join(os.path.dirname(root_dir), "bg3_mod_template_tool", mod_name)
    print('pakpath_dir:' + str(pakpath))
    print('mod_dir:' + str(mod_dir))
    # Use the provided divine.exe path
    
    subprocess.run([divine_path, "-g", "bg3", "--action", "create-package", "--source", mod_dir, "--destination", pakpath, "-l", "all"])
    if mod_dest_path:
        shutil.move(pakpath, os.path.join(mod_dest_path, f"{mod_name}.pak"))
        print("Mod files moved to", mod_dest_path)
        temp_folder = os.path.join(os.path.dirname(root_dir), "temp")
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)
        return
    else:
        print("Mod Destination Folder not provided. Please provide it in the Configuration tab.")
        return

def launch_bg3_mod_manager():
    mod_manager_path = r'C:\Users\vishal\Desktop\bg3_mods\BG3ModManager_Latest\BG3ModManager.exe'
    subprocess.Popen([mod_manager_path])
    time.sleep(5)  # Wait for the mod manager to launch
    pyautogui.hotkey('ctrl', 'shift', 'g')  # Launch the game

if __name__ == "__main__":
    if run_git_pull():
        mod_file = 'Quickster.pak'
        appdata_path = os.getenv('APPDATA')  # This gets the value of the APPDATA environment variable
        mods_dir = os.path.join(appdata_path, 'Larian Studios\\Baldur\'s Gate 3\\Mods')
        upload_mod_file(mod_file, mods_dir)
        launch_bg3_mod_manager()
