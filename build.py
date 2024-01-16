import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'pyinstaller',
    'main.py', # your main file with ui.run()
    '--name', 'GPACalc', # name of your app
    #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui',
    '--hiddenimport', 'sklearn.ensemble'

]
subprocess.call(cmd)
