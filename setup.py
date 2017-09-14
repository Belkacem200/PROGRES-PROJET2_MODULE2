import tkinter.tix
import sys
import os
import glob
import os.path
import matplotlib
from distutils.core import setup
import py2exe
from pygal import *
sys.setrecursionlimit(5000)
import pygal

sys.argv.append('py2exe')
"""
setup(
    options = {'py2exe': { 'compressed': True}},
    windows = [{'script': "D:\Users\u156726\PycharmProjects\SFR_APP\SFR_APP_BIG_DATA.py"}],
    zipfile = None,
)
"""
"""""
import matplotlib
import glob

setup(console=['D:\Users\u156726\PycharmProjects\SFR_APP\SFR_APP_BK.py'],options={
               'py2exe': {
                          'packages' :  ['matplotlib', 'pytz'],

                          }
                },
      data_files=matplotlib.get_py2exe_datafiles(),)

"""
includes = ['matplotlib','datetime','lxml.etree', 'lxml._elementpath', 'gzip','pygal','matplotlib.pyplot','ttk','lxml', 'numpy', 'Tkinter', 'Tkconstants', 'pygal','Tix','matplotlib.backends.backend_qt4agg','matplotlib.ticker','PyQt4','datetime','tkFileDialog','ttk','threading' ,'csv','re','numpy','os','tkinter.tix']
excludes = ['_gtkagg', '_tkagg', 'curses', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs' ]
packages = []
dll_excludes = []
import Tix
import lxml
lxml.get_include()

def files(folder):
    for path in glob.glob(folder+'/*'):
         if os.path.isfile(path):
            yield path



class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "1.0.0.0"
        self.company_name = "SFR"
        self.copyright = "Copyright (c) 2017 KAID Belkacem."
        self.name = "SFR_Perf_DataAnalyser"

target = Target(
    description = "Analyseur de remontees SFR Perf",
    script = "D:\Users\u156726\PycharmProjects\SFR_APP\SFR_APP.py", #---->LE CHEMIN VERS LE CODE SOURCE EST A MODIFIER
    icon_resources = [(1, "myicon.ico")],
    dest_base = "SFR_Perf_DataAnalyser")


data_files=[('.', glob.glob(sys.prefix+'/DLLs/tix81*.dll')),
            ('.', matplotlib.get_py2exe_datafiles()),
            ('.', 'D:\Users\u156726\AppData\Local\Continuum\Anaconda2\Lib\lib-tk'),
             ('tcl/tix8.1', files(sys.prefix+'/tcl/tix8.1')),
            ('tcl/tix8.1/bitmaps', files(sys.prefix+'/tcl/tix8.1/bitmaps')),
             ('tcl/tix8.1/pref', files(sys.prefix+'/tcl/tix8.1/pref')),
           ]

setup(
    options = {"py2exe": {"compressed": 0,
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "dist_dir": ".",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                            "skip_archive": True,
                         }
              },
    windows = [target],
    data_files=matplotlib.get_py2exe_datafiles(),
)
