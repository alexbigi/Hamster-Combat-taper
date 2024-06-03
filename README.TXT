run terminal after clone repo:
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt

(need edit points for tap)

for this game we have two ways:
- connect via usb. using ADB
run terminal:
cd in project folder
. ./.venv/bin/activate
python app_with_adb.py

- open emulator. using pyautogui (run as root)
run terminal:
sudo su
cd to project folder
. ./.venv/bin/activate
python app_with_pyautogui

ctrl+c - multuple press for break