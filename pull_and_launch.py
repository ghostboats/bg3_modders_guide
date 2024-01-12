import subprocess
import shutil
import os
import pyautogui
import time
import pygetwindow as gw
import keyboard
#to make exe run this in the same dir as bg3_modders_guide
#C:\Users\vishal\AppData\Roaming\Python\Python312\Scripts\pyinstaller.exe --onefile --add-data "C:\Users\vishal\Desktop\bg3_mods\*.png;bg3_mods" pull_and_launch.py

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
        time.sleep(0.5)
        pyautogui.click(image_location)
        time.sleep(0.5)
    return image_location


def run_git_pull(repo_path):
    original_dir = os.getcwd()  # Save the original directory
    try:
        os.chdir(repo_path)  # Change to the repo directory
        subprocess.check_call(['git', 'pull'])
        os.chdir(original_dir)  # Change back to the original directory
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        os.chdir(original_dir)  # Ensure we change back even if there's an error
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        os.chdir(original_dir)  # Ensure we change back even if there's an unexpected error
        return False
    return True

def upload_mod_file(mod_folder, mods_dir):
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    divine_path = r"C:\Users\vishal\Desktop\bg3_mods\ExportTool-v1.18.7\Tools\divine.exe"
    pack_mod(os.path.abspath(__file__), divine_path, mod_folder)


def pack_mod(folder_path, divine_path, mod_dest_path):
    mod_name = os.path.basename(mod_dest_path)  # Assuming mod_dest_path is the mod name
    print('folder_path:' + str(folder_path))
    print('divine_path:' + str(divine_path))
    print('mod_dest_path:' + str(mod_dest_path))
    print(mod_name)

    # Use the absolute path for the Quickster directory
    quickster_path = r"C:\Users\vishal\Desktop\git repos\bg3_modders_guide\Quickster"
    pakpath = os.path.join(quickster_path, "temp", f"{mod_name}.pak")
    mod_dir = quickster_path  # Use the provided Quickster path

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
    temp_folder = os.path.join(quickster_path, "temp")
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)

def launch_bg3_mod_manager():
    mod_manager_path = r'C:\Users\vishal\Desktop\bg3_mods\BG3ModManager_Latest\BG3ModManager.exe'
    subprocess.Popen([mod_manager_path])
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

def launch_bg3_modders_multitool():
    multitool_path = r"C:\Users\vishal\Desktop\bg3_mods\bg3-modders-multitool\bg3-modders-multitool.exe"
    subprocess.Popen([multitool_path])


    rebuild_image_path = r'C:\Users\vishal\Desktop\bg3_mods\rebuild.png'
    find_image_on_screen(rebuild_image_path, click=1)

    # Additional steps if needed

def interact_with_game():
    time.sleep(10)
    
    # Activate Baldur's Gate 3 window
    bg3_window = gw.getWindowsWithTitle('Baldur\'s Gate 3')[0]
    bg3_window.activate()
    pyautogui.click()
    pyautogui.click()
    
    game_menu_path = r'C:\Users\vishal\Desktop\bg3_mods\game_menu.png'
    find_image_on_screen(game_menu_path, click=1, confidence=0.95)
    time.sleep(1)
    pyautogui.click()
    new_game_path = r'C:\Users\vishal\Desktop\bg3_mods\new_game_button.png'
    find_image_on_screen(new_game_path, click=2, confidence=0.76)
    pyautogui.moveTo(1,1)
    start_game_path = r'C:\Users\vishal\Desktop\bg3_mods\start_game_button.png'
    find_image_on_screen(start_game_path, click=1)
    #accept_button_path = r'C:\Users\vishal\Desktop\bg3_mods\accept_button.png'
    #find_image_on_screen(accept_button_path, click=0)
    time.sleep(8)
    keyboard.press_and_release('esc')
    #find_image_on_screen(accept_button_path, click=2)
    dont_reset_button_path = r'C:\Users\vishal\Desktop\bg3_mods\dont_reset_button.png'
    find_image_on_screen(dont_reset_button_path, click=1)
    time.sleep(0.5)
    class_button_path = r'C:\Users\vishal\Desktop\bg3_mods\class_button.png'
    find_image_on_screen(class_button_path, click=1)
    quickster_button_path = r'C:\Users\vishal\Desktop\bg3_mods\quickster_button.png'
    find_image_on_screen(quickster_button_path, click=1)
    class_passives_button_path = r'C:\Users\vishal\Desktop\bg3_mods\class_passives_button.png'
    find_image_on_screen(class_passives_button_path, click=1)
    proceed_button_path = r'C:\Users\vishal\Desktop\bg3_mods\proceed_button.png'
    find_image_on_screen(proceed_button_path, click=1)
    for _ in range(3):
        pyautogui.click()
        time.sleep(0.5)


if __name__ == "__main__":
    git_repo_path = 'C:\\Users\\vishal\\Desktop\\git repos\\bg3_modders_guide'
    if run_git_pull(git_repo_path):
        mod_file = 'Quickster.pak'
        mod_folder = 'Quickster'
        local_appdata_path = os.getenv('LOCALAPPDATA')
        mods_dir = os.path.join(local_appdata_path, 'Larian Studios\\Baldur\'s Gate 3\\Mods')
        upload_mod_file(mod_folder, mods_dir)

        launch_bg3_modders_multitool()  # Launch BG3 Modders Multitool
        time.sleep(1)
        launch_bg3_mod_manager()  # Launch BG3 Mod Manager
        interact_with_game()