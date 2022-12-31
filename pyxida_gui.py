# -*- coding: utf-8 -*-

import os
import tkinter as tk

__author__ = 'c.kormaris'

img_path = 'img\\'

# create window and set title
root = tk.Tk(className='Pyxida AUEB Dissertations Scraper and Downloader')

# change window size
root.geometry("800x600")
# change icon
icon = tk.PhotoImage(file=img_path + 'compass.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

departments = [1, 2, 3, 4, 5, 6, 7, 8]
department_names = ['Department of Informatics',
                    'Department of Statistics',
                    'Department of Business Administration',
                    'Department of Accounting and Finance',
                    'Department of Marketing and Communication',
                    'Department of Management Science and Technology',
                    'Department of Economics',
                    'Department of International and European Economic Studies']
PhDOrMSc = ['phd', 'msc']

# Frames #
departmentsFrame = tk.Frame(root)
PhDOrMScFrame = tk.Frame(root)
buttonsFrame = tk.Frame(root)

department_var = tk.StringVar(departmentsFrame, 1)
PhDOrMScFrame_var = tk.StringVar(PhDOrMScFrame, 'phd')
variables = [department_var, PhDOrMScFrame_var]


def run_scraper():
    arguments = []
    for variable in variables:
        arguments.append(variable.get())
    arguments = ' '.join(arguments)
    # print(arguments)
    python_script = 'pyxida_aueb_scraper.py'
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
    python_script = 'pyxida_aueb_downloader.py'
    print('Running ' + python_script + '...')
    # os.environ('PATH')
    os.system('python ' + python_script + ' ' + arguments)
    print('')


def about_window():
    window = tk.Toplevel(root)
    # change title
    window.wm_title('About')
    creator = tk.Label(window, text='© Created by: Christos Kormaris')
    creator.pack()
    date = tk.Label(window, text='Date: March 2018')
    date.pack()
    # change icon
    icon = tk.PhotoImage(file=img_path + 'help.png')
    window.tk.call('wm', 'iconphoto', window._w, icon)
    window.geometry('300x100')
    window.resizable(False, False)

    okButton = tk.Button(
        window,
        text='Ok',
        fg='#000000',
        bg="#458BAB",
        height=2,
        width=6,
        command=window.destroy
    )
    okButton.pack(side=tk.BOTTOM)

    center(window)


# 1. departmentsFrame Widgets #
departments_label = tk.Label(departmentsFrame, text="departments: ")
departments_label.pack()
for i in range(len(departments)):
    tk.Radiobutton(departmentsFrame,
                   text=department_names[i],
                   padx=2,
                   variable=department_var,
                   value=departments[i]).pack(anchor=tk.CENTER)

empty_line_label = tk.Label(departmentsFrame, text="\n")
empty_line_label.pack()

departmentsFrame.pack()

# 2. PhDOrMScFrame Widgets #
PhDOrMScFrame_label = tk.Label(PhDOrMScFrame, text="PHD or MSc: ")
PhDOrMScFrame_label.pack()
for value in PhDOrMSc:
    tk.Radiobutton(PhDOrMScFrame,
                   text=value,
                   padx=2,
                   variable=PhDOrMScFrame_var,
                   value=value).pack(anchor=tk.CENTER)

empty_line_label = tk.Label(PhDOrMScFrame, text="\n")
empty_line_label.pack()

PhDOrMScFrame.pack()

# 3. buttonsFrame Widgets #
runScraperButton = tk.Button(
    buttonsFrame,
    text='Run Scraper',
    fg='#000000',
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
    fg='#000000',
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


center(root)
root.mainloop()
