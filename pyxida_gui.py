# -*- coding: utf-8 -*-

import os
import tkinter as tk


img_path = 'img\\'

# create window and set title
root = tk.Tk(className='Pyxida AUEB Scraper')

# change window size
root.geometry("800x600")

# change icon
root.iconbitmap(img_path + 'compass.ico')

departments = [1, 2, 3, 4, 5, 6, 7, 8]
department_names = [
    'Department of Informatics',
    'Department of Statistics',
    'Department of Business Administration',
    'Department of Accounting and Finance',
    'Department of Marketing and Communication',
    'Department of Management Science and Technology',
    'Department of Economics',
    'Department of International and European Economic Studies'
]
phd_or_msc = ['phd', 'msc']

# Frames #
departmentsFrame = tk.Frame(root)
phd_or_msc_frame = tk.Frame(root)
buttonsFrame = tk.Frame(root)

department_var = tk.StringVar(departmentsFrame, '1')
phd_or_msc_var = tk.StringVar(phd_or_msc_frame, 'phd')
variables = [department_var, phd_or_msc_var]


def run_scraper():
    arguments = []
    for variable in variables:
        arguments.append(variable.get())
    arguments = ' '.join(arguments)
    # print(arguments)
    python_script = 'pyxida_scraper.py'
    print('Running ' + python_script + '...')
    # os.environ('PATH')
    os.system('python ' + python_script + ' ' + arguments)
    print('')


def run_downloader():
    arguments = []
    for variable in variables:
        arguments.append(variable.get())
    arguments = ' '.join(arguments)
    # print(arguments)
    python_script = 'pyxida_downloader.py'
    print('Running ' + python_script + '...')
    # os.environ('PATH')
    os.system('python ' + python_script + ' ' + arguments)
    print('')


def about_window():
    window = tk.Toplevel(root)
    # change title
    window.wm_title('About')
    creator = tk.Label(window, text='© Created by Christos Kormaris')
    creator.pack()
    date = tk.Label(window, text='Athens, March 2018')
    date.pack()

    # change icon
    window.iconbitmap(img_path + 'info.ico')

    window.geometry('300x100')
    window.resizable(False, False)

    ok_button = tk.Button(window, text='Ok', fg='white', bg='#458BAB', height=2, width=6, command=window.destroy)
    ok_button.pack()

    center(window)


# 1. departmentsFrame Widgets #
departments_label = tk.Label(departmentsFrame, text='departments: ')
departments_label.pack()
for i in range(len(departments)):
    tk.Radiobutton(
        departmentsFrame,
        text=department_names[i],
        padx=2,
        variable=department_var,
        value=departments[i]
    ).pack(anchor=tk.CENTER)

empty_line_label = tk.Label(departmentsFrame, text="\n")
empty_line_label.pack()

departmentsFrame.pack()

# 2. PhDOrMScFrame Widgets #
phd_or_msc_label = tk.Label(phd_or_msc_frame, text='PhD or MSc: ')
phd_or_msc_label.pack()
for value in phd_or_msc:
    tk.Radiobutton(
        phd_or_msc_frame,
        text=value,
        padx=2,
        variable=phd_or_msc_var,
        value=value
    ).pack(anchor=tk.CENTER)

empty_line_label = tk.Label(phd_or_msc_frame, text="\n")
empty_line_label.pack()

phd_or_msc_frame.pack()

# 3. buttonsFrame Widgets #
runScraperButton = tk.Button(
    buttonsFrame,
    text='Run Scraper',
    fg='white',
    bg='#458BAB',
    height=2,
    width=12,
    command=run_scraper
)
runScraperButton.pack(side=tk.TOP)

empty_line_label = tk.Label(buttonsFrame, text="\r")
empty_line_label.pack()

runDownloaderButton = tk.Button(
    buttonsFrame,
    text='Run Downloader',
    fg='white',
    bg='#458BAB',
    height=2,
    width=12,
    command=run_downloader
)
runDownloaderButton.pack(side=tk.BOTTOM)

buttonsFrame.pack()

# Menus #

menu = tk.Menu(root)
root.config(menu=menu)

aboutMenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='About', menu=aboutMenu)  # adds drop-down menu
aboutMenu.add_command(label='About', command=about_window)


#####


# center the window on screen
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


#####

if __name__ == '__main__':
    center(root)
    root.mainloop()
