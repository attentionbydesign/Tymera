# tymera_1.0
Custom Scripts

Installation

in order for the Python2.7 shell to import modules in this plugin, you must add the path to it.

In the Chimera GUI, go to Tools > Additional Tools > Add third-party plugin location... which should open up a dialog where you can click the [Add...] button and find the folder ONE LEVEL ABOVE tymera_1.0/.  Clicking [Save] will add the path to the sys.path variable of of the Python2.7 shell.

Chimera will look for a ChimeraExtension.py file that
defines a class for the plugin.

Class attributes include the submenu under which
it will be located (e.g. Tools > '<submenu>' > '<plugin>')
the name of the plugin that will be displayed '<plugin>'
and the action that is performed when you click on it
In this case, the action is defined in tymera.py,
which defines a function tymera_init() that simply imports
all of the relevant packages in the plugin directory.

Each package directory (e.g., ColorBySeq) should have
its own __init__.py to be recognized as something
importable.  For ColorBySeq and some others, the __init__.py
also has instructions to import modules within that package.

For example, I believe color_by_seq() can be run in
the IDLE with colorbyseq.color_by_seq() after activating
tymera, since the colorbyseq.py module got imported. 

***in Python 2.7.14 Shell, enter the following reset the default path where scripts are opened to tymera/ if running on Windows:***

import tymera
os.chdir(os.path.dirname(tymera.__file__))