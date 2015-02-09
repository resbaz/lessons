#!/anaconda/bin/python

# This script converts .py file to .ipynb and runs in browser.
# It's intended for use in a Sublime Text build system
# usage: python builder.py filename
# Author: Daniel McDonald

# For the sake of completeness, here's the Build System, in packages/user/pytoipy.sublime-build:

# it probably needs the customcss ipython profile to work properly.

# {
#     "cmd": ["st3build", "$file"],
#     "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
#     "selector": "source.python"
# }

import os
import sys
import IPython.nbformat.current as nbf # API converter
arg = str(sys.argv[1]) # get filename argument
outbasename = os.path.splitext(arg)[0] # get input file basename
output = outbasename + '.ipynb' # create output name
print 'Converting ' + arg + ' ---> ' + output + ' ...' # print status
nb = nbf.read(open(arg, 'r'), 'py') # read and convert .py file
nbf.write(nb, open(output, 'w'), 'ipynb') # create .ipynb file
print 'Done!'
#shellscript = '/anaconda/bin/ipython notebook --profile customcss ' + output # create shell command to open iPython in browser
shellscript = '/anaconda/bin/ipython notebook ' + output # create shell command to open iPython in browser

os.system(shellscript) # issue command
