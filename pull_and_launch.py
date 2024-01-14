import subprocess
import shutil
import os
import pyautogui
import time
import pygetwindow as gw
import keyboard

SS = r'C:\\Users\\vishal\\Desktop\\git repos\\bg3_modders_guide\\screenshots\\'
#to make exe run this in the same dir as bg3_modders_guide
#C:\Users\vishal\AppData\Roaming\Python\Python312\Scripts\pyinstaller.exe --onefile --add-data "C:\Users\vishal\Desktop\bg3_mods\*.png;bg3_mods" pull_and_launch.py

def find_image_on_screen(screenshot_path, click = 0, search_time=0, confidence=0.8, instant = True):
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
        if instant == True:
            pyautogui.click(image_location)
            time.sleep(0.5)
        else:
            pyautogui.moveTo(image_location, duration = instant)
            pyautogui.click()
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

def launch_bg3_modders_multitool():
    multitool_path = r"C:\Users\vishal\Desktop\bg3_mods\bg3-modders-multitool\bg3-modders-multitool.exe"
    multitool_process = subprocess.Popen([multitool_path])
    find_image_on_screen(SS + 'rebuild.png', click=1)
    return multitool_process

def launch_bg3_mod_manager():
    mod_manager_path = r'C:\Users\vishal\Desktop\bg3_mods\BG3ModManager_Latest\BG3ModManager.exe'
    mod_manager_process = subprocess.Popen([mod_manager_path])
    find_image_on_screen(SS + 'inactive_mods.png',1)
    pyautogui.typewrite('Quickster')
    quickster_active_location=find_image_on_screen(SS + 'quickster_active.png', search_time=1)
    if quickster_active_location == None:
        find_image_on_screen(SS + 'quickster_location.png',1, confidence=0.99)
        pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'shift', 'g')  # Launch the game
    return mod_manager_process

def interact_with_game():
    time.sleep(10)
    # Activate Baldur's Gate 3 window
    bg3_window = gw.getWindowsWithTitle('Baldur\'s Gate 3')[0]
    bg3_window.activate()
    pyautogui.click()
    pyautogui.click()
    find_image_on_screen(SS + 'game_menu.png', click=1, confidence=0.95)
    time.sleep(3)
    find_image_on_screen(SS + 'new_game_button.png', click=1, confidence=0.83, instant=1.5)
    pyautogui.moveTo(1,1)
    find_image_on_screen(SS + 'start_game_button.png', click=1, instant=0.5)
    time.sleep(10)
    keyboard.press_and_release('esc')
    find_image_on_screen(SS + 'dont_reset_button.png', click=1, instant=0.5)
    find_image_on_screen(SS + 'class_button.png', click=1, instant=0.5)
    find_image_on_screen(SS + 'quickster_button.png', click=1, instant = 0.5)
    find_image_on_screen(SS + 'class_passives_button.png', click=1, instant = 0.5)
    find_image_on_screen(SS + 'gotta_run_button.png', click=1, instant=0.5)
    find_image_on_screen(SS + 'proceed_button.png', click=1, instant = 0.5)
    for _ in range(3):
        pyautogui.click()
        time.sleep(0.5)
    time.sleep(6)
    keyboard.press_and_release('esc')
    in_game_path = SS + 'in_game_button.png'
    in_game_button = None
    while in_game_button is None:
        in_game_button = find_image_on_screen(in_game_path, click=0)

    pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)

    while in_game_button != None:
        keyboard.press_and_release('space')
        time.sleep(0.3)
        try:
            in_game_button = pyautogui.locateOnScreen(in_game_path, confidence=0.8)
        except:
            in_game_button = None




if __name__ == "__main__":
    start_time = time.time()
    git_repo_path = 'C:\\Users\\vishal\\Desktop\\git repos\\bg3_modders_guide'
    divine_path = r"C:\Users\vishal\Desktop\bg3_mods\ExportTool-v1.18.7\Tools\divine.exe"
    if run_git_pull(git_repo_path):
        mod_file = 'Quickster.pak'
        mod_folder = 'Quickster'
        local_appdata_path = os.getenv('LOCALAPPDATA')
        mods_dir = os.path.join(local_appdata_path, 'Larian Studios\\Baldur\'s Gate 3\\Mods')
        if not os.path.exists(mods_dir):
            print('no dir found')
            quit()
        pack_mod(os.path.abspath(__file__), divine_path, mod_folder)

        modders_multitool_process = launch_bg3_modders_multitool()  # Launch BG3 Modders Multitool
        time.sleep(0.5)
        mod_manager_process = launch_bg3_mod_manager()  # Launch BG3 Mod Manager
        interact_with_game()
        if modders_multitool_process:
            modders_multitool_process.terminate()
        if mod_manager_process:
            mod_manager_process.terminate()
        
        end_time = time.time()  # Capture the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Script completed in {elapsed_time:.2f} seconds.")