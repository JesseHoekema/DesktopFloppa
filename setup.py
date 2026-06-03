from setuptools import setup

APP = ['main.py']
DATA_FILES = [('assets', ['assets/sound.mp3', 'assets/sound2.mp3', 'assets/sound3.mp3', 'assets/background.wav', 'assets/floppa.png'])]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'],
    'excludes': ['PyQt5', 'PyInstaller', 'IPython', 'jupyter', 'numpy'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)