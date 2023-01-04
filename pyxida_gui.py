import tkinter as tk

from pyxida_downloader import *
from pyxida_scraper import *


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


# center the window on screen
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == '__main__':
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
    departments_frame = tk.Frame(root)
    phd_or_msc_frame = tk.Frame(root)
    buttons_frame = tk.Frame(root)

    department_var = tk.StringVar(departments_frame, '1')
    phd_or_msc_var = tk.StringVar(phd_or_msc_frame, 'phd')

    # 1. departments_frame widgets #
    departments_label = tk.Label(departments_frame, text='departments: ')
    departments_label.pack()
    for i in range(len(departments)):
        tk.Radiobutton(
            departments_frame,
            text=department_names[i],
            padx=2,
            variable=department_var,
            value=departments[i]
        ).pack(anchor=tk.CENTER)

    empty_line_label = tk.Label(departments_frame, text="\n")
    empty_line_label.pack()

    departments_frame.pack()

    # 2. phd_or_msc_label widgets #
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

    # 3. buttons_frame widgets #
    run_scraper_button = tk.Button(
        buttons_frame,
        text='Run Scraper',
        fg='white',
        bg='#458BAB',
        height=2,
        width=12,
        command=lambda: pyxida_scraper(int(department_var.get()), phd_or_msc_var.get())
    )
    run_scraper_button.pack(side=tk.TOP)

    empty_line_label = tk.Label(buttons_frame, text="\r")
    empty_line_label.pack()

    runDownloaderButton = tk.Button(
        buttons_frame,
        text='Run Downloader',
        fg='white',
        bg='#458BAB',
        height=2,
        width=12,
        command=lambda: pyxida_downloader(int(department_var.get()), phd_or_msc_var.get())
    )
    runDownloaderButton.pack(side=tk.BOTTOM)

    buttons_frame.pack()

    # Menus #
    menu = tk.Menu(root)
    root.config(menu=menu)

    aboutMenu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='About', menu=aboutMenu)  # adds drop-down menu
    aboutMenu.add_command(label='About', command=about_window)

    center(root)
    root.mainloop()
