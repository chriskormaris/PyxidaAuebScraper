import cx_Freeze
import sys

base = None

if sys.platform == 'win64':
    base = 'Win64GUI'
elif sys.platform == 'win32':
    base = 'Win32GUI'

img_path = 'img\\'
executables = [cx_Freeze.Executable('pyxida_gui.py', base=base, icon=img_path + 'compass.png')]
include_files = [img_path + x for x in ['compass.png', 'help.png']]
includes = []
excludes = ['Tkinter']
packages = []
build_exe_options = {'includes': includes, 'packages': packages, 'excludes': excludes, 'include_files': include_files}

cx_Freeze.setup(
    name='pyxida',
    options={'build_exe': build_exe_options},
    version='1.0.0',
    description='Pyxida AUEB Dissertations Scraper',
    executables=executables
)
