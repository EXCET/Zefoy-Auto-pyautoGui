import pyautogui
import time
import pydirectinput

time.sleep(1)

#EXCET#4508

count = 0
while (count < 999999):
  pyautogui.click()
  pyautogui.click(x=986, y=273)
  pyautogui.write("https://www.tiktok.com/@exc3t/video/7106225446177623302?is_from_webapp=1&sender_device=pc&web_id=7047354921838970373")
  pyautogui.press('enter')
  pyautogui.click(x=870, y=320)
  time.sleep(1)
  pyautogui.click()
  pyautogui.click(x=108, y=129)
  time.sleep(1)
  pyautogui.click(x=648, y=413)
  time.sleep(160)
