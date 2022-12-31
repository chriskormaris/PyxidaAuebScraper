# PyxidaAuebDissertationsScraper
A web scrapper tool to easily extract links from the Pyxida Institutional Repository.
The urls extracted contain MSc and PhD dissertations, in `.pdf` format, from all the departments of AUEB.

Visit:
[http://www.pyxida.aueb.gr](http://www.pyxida.aueb.gr)


## How to run


**Step 1**
Run:
```shell
python pyxida_aueb_scraper.py
```

**Step 2**
Run:
```shell
python pyxida_aueb_downloader.py
```

## GUI

![screenshot](screenshots/1.png)

You can simply open and run the GUI application.
Run:
```shell
python pyxida_gui.py
```

or

You can make an executable file for the gui.
First, install the required library `pyinstaller`:
```shell
pip install pyinstaller
```

Then, run:
```shell
pyinstaller pyxida_gui.spec
```

And then run the created file `pyxida_gui.exe`!
Now, you can download all the dissertations you want easily!
