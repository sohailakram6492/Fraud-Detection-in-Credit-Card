import pyautogui
import time

# Set the duration between each mouse movement (in seconds)
movement_interval = 10  # Adjust this value as needed
pyautogui.FAILSAFE = True

def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Temporarily disable fail-safe to move cursor to center
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(center_x, center_y)
    pyautogui.FAILSAFE = True

    print(f"Cursor moved to the center: ({center_x}, {center_y})")

def move_cursor():
    while True:
        try:
            # Move the mouse cursor slightly to avoid auto-lock
            pyautogui.moveRel(10, 1)
            pyautogui.moveRel(-10, -1)

            # Wait for the specified interval before moving the mouse again
            time.sleep(movement_interval)
            print("Cursor moved")

        except pyautogui.FailSafeException:
            # Handle the fail-safe exception
            print("Fail-safe triggered: Mouse moved to a corner of the screen.")
            move_cursor_to_center()
            time.sleep(10)

move_cursor()
