import tkinter as tk

from src.pyxida_downloader import *
from src.pyxida_scraper import *


def about_window():
    window = tk.Toplevel(root)
    # change title
    window.wm_title('About')
    creator = tk.Label(window, text=f'© Created by {author}')
    creator.pack()

    date = tk.Label(window, text='Athens, March 2018')
    date.pack()

    version_label = tk.Label(window, text=f'Version: {version}')
    version_label.pack()

    # change icon
    window.iconbitmap(os.path.join(img_path, 'info.ico'))

    window.geometry('300x120')
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
    win.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == '__main__':
    # create window and set title
    root = tk.Tk()
    root.title('Pyxida AUEB Scraper & Downloader')

    # change window size
    root.geometry('800x600')

    # change icon
    root.iconbitmap(os.path.join(img_path, 'compass.ico'))

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

    department_var = tk.IntVar(departments_frame, 1)
    phd_or_msc_var = tk.StringVar(phd_or_msc_frame, 'phd')

    # 1. departments_frame widgets #
    departments_label = tk.Label(departments_frame, text='Department: ')
    departments_label.pack()
    for i in range(len(department_names)):
        tk.Radiobutton(
            departments_frame,
            text=department_names[i],
            padx=2,
            variable=department_var,
            value=i + 1
        ).pack(anchor=tk.CENTER)

    empty_line_label = tk.Label(departments_frame, text="\n")
    empty_line_label.pack()

    departments_frame.pack()

    # 2. phd_or_msc_frame widgets #
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
        command=lambda: pyxida_scraper(department_var.get(), phd_or_msc_var.get())
    )
    run_scraper_button.pack(side=tk.TOP)

    empty_line_label = tk.Label(buttons_frame, text="\r")
    empty_line_label.pack()

    run_downloader_button = tk.Button(
        buttons_frame,
        text='Run Downloader',
        fg='white',
        bg='#458BAB',
        height=2,
        width=12,
        command=lambda: pyxida_downloader(department_var.get(), phd_or_msc_var.get())
    )
    run_downloader_button.pack(side=tk.BOTTOM)

    buttons_frame.pack()

    # Menus #
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='File', menu=file_menu)  # adds drop-down menu
    file_menu.add_command(label='Exit', command=root.destroy)

    help_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Help', menu=help_menu)  # adds drop-down menu
    help_menu.add_command(label='About', command=about_window)

    center(root)
    root.mainloop()
