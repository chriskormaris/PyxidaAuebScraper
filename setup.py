import os
import sys

import cx_Freeze

from src.constants import *

base = None

if sys.platform == 'win64':
    base = 'Win64GUI'
elif sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable('pyxida_gui.py', base=base, icon=os.path.join(img_path, 'compass.ico'))]
include_files = [img_path + '\\' + file for file in ['compass.ico', 'info.ico']]
includes = []
excludes = ['tk']
packages = []
build_exe_options = {'includes': includes, 'packages': packages, 'excludes': excludes, 'include_files': include_files}

cx_Freeze.setup(
    name='pyxida',
    options={'build_exe': build_exe_options},
    version='1.0.0',
    description='Pyxida AUEB Scraper',
    executables=executables
)
