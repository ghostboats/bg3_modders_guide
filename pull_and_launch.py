import subprocess
import shutil
import os
import pyautogui
import time

def find_image_on_screen(screenshot_path, click = 0, search_time=0, confidence=0.8):
    print("Starting function find_image_on_screen. Looking for: " + str(screenshot_path))
    image_location = None
    moved = False
    if search_time == 0:
        while image_location is None:
            try:
                image_location = pyautogui.locateOnScreen(screenshot_path, confidence=confidence)
            except:
                if moved == True:
                    print('mouse has been moved off screne already')
                else:
                    print('image not found, moving mouse off screen to avoid issues reading screen')
                    pyautogui.moveTo(pyautogui.size().width + 100, pyautogui.size().height / 2)
                    moved = True
                image_location = None
    else:
        start_time = time.time()
        end_time = start_time + search_time
        while image_location is None and time.time() < end_time:
            try:
                image_location = pyautogui.locateOnScreen(screenshot_path, confidence=confidence)
            except:
                if moved == True:
                    print('mouse has been moved off screne already')
                else:
                    print('image not found, moving mouse off screen to avoid issues reading screen')
                    pyautogui.moveTo(pyautogui.size().width + 100, pyautogui.size().height / 2)
                    moved = True
                image_location = None
    if image_location != None and click != 0:
        print('clicking location')
        pyautogui.click(image_location)
    return image_location


def run_git_pull():
    try:
        subprocess.check_call(['git', 'pull'])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

def upload_mod_file(mod_folder, mods_dir):
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    divine_path = r"C:\Users\vishal\Desktop\bg3_mods\ExportTool-v1.18.7\Tools\divine.exe"
    pack_mod(os.path.abspath(__file__), divine_path, mod_folder)


def pack_mod(folder_path, divine_path, mod_dest_path):
    root_dir = os.path.dirname(folder_path)
    mod_name = os.path.basename(mod_dest_path)  # Assuming mod_dest_path is the mod name
    print('folder_path:' + str(folder_path))
    print('divine_path:' + str(divine_path))
    print('mod_dest_path:' + str(mod_dest_path))
    print(mod_name)

    pakpath = os.path.join(root_dir, "temp", f"{mod_name}.pak")
    mod_dir = os.path.join(root_dir, mod_dest_path)  # Corrected to point to mod folder
    print('pakpath_dir:' + str(pakpath))
    print('mod_dir:' + str(mod_dir))

    result = subprocess.run([divine_path, "-g", "bg3", "--action", "create-package", "--source", mod_dir, "--destination", pakpath, "-l", "all"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    if os.path.exists(pakpath):
        shutil.move(pakpath, os.path.join(mods_dir, f"{mod_name}.pak"))
        print("Mod files moved to", mods_dir)
    else:
        print("Error: .pak file not created.")
    
    # Clean up temp folder
    temp_folder = os.path.join(root_dir, "temp")
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)

def launch_bg3_mod_manager():
    mod_manager_path = r'C:\Users\vishal\Desktop\bg3_mods\BG3ModManager_Latest\BG3ModManager.exe'
    subprocess.Popen([mod_manager_path])
    time.sleep(5)  # Wait for the mod manager to launch
    inactive_mods_path = r'C:\Users\vishal\Desktop\bg3_mods\inactive_mods.png'
    quickster_active_path = r'C:\Users\vishal\Desktop\bg3_mods\quickster_active.png'
    image_path = r'C:\Users\vishal\Desktop\bg3_mods\quickster_location.png'

    find_image_on_screen(inactive_mods_path,1)
    pyautogui.typewrite('Quickster')
    quickster_active_location=find_image_on_screen(quickster_active_path, search_time=1)
    if quickster_active_location == None:
        find_image_on_screen(image_path,1, confidence=0.99)
        pyautogui.press('enter')
    

    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'shift', 'g')  # Launch the game

if __name__ == "__main__":
    if run_git_pull():
        mod_file = 'Quickster.pak'
        mod_folder = 'Quickster'
        local_appdata_path = os.getenv('LOCALAPPDATA')
        mods_dir = os.path.join(local_appdata_path, 'Larian Studios\\Baldur\'s Gate 3\\Mods')
        upload_mod_file(mod_folder, mods_dir)
        launch_bg3_mod_manager()
