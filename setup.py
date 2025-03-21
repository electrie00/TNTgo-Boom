"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['TNTgo Boom.py']
DATA_FILES = ['serialread.py','battery_icon.png','rumps','kext']
OPTIONS = {'includes':['serial','re','time','PIL','datetime','threading','subprocess','AppKit','Foundation','os','PyObjCTools','pickle','traceback']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

#python3 setup.py py2app             