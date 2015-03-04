#!/usr/bin/python

#	Converting to and from iPython Notebook files
#	for ResBaz NLTK stream
#	Author: Daniel McDonald
#	More info: http://ipython.org/ipython-doc/1/interactive/nbconvert.html
#	https://github.com/ipython/ipython/blob/master/IPython/nbformat/v3/nbpy.py

#These are basic functions for converting to/from iPython Notebook files.

# Import these functions by either adding them to your script/notebook, or by importing them from this file, which could be either in your $PATH or in the current working directory. Import them both with:

#	from converters import *

#or individually with:

#	from converters import pytoipy
#or
#	from converters import ipyconverter

# It comes to my attention that encoding issues in your original files can break these functions spectacularly. Sorry!

def pytoipy(inputfile):
	"""A .py to .ipynb converter.

	This function converts .py files to ipynb, relying on the iPython API. Comments in the .py file can be used to delimit cells, headings, etc. For example:

	# <headingcell level=1>
	# A heading 
	# <markdowncell>
	# *This text is in markdown*
	# <codecell>
	# print 'hello'

	Example usage: pytoipy('filename.py')
	"""
	import os
	import IPython.nbformat.current as nbf
	outbasename = os.path.splitext(inputfile)[0]
	output = outbasename + '.ipynb'
	print 'Converting ' + inputfile + ' ---> ' + output + ' ...'
	nb = nbf.read(open(inputfile, 'r'), 'py')
	nbf.write(nb, open(output, 'w'), 'ipynb')
	print 'Done!'



def ipyconverter(inputfile, outextension):
	"""ipyconverter converts ipynb files to various formats.

	This function calls a shell script, rather than using an API. The first argument is the ipynb file. The second argument is the file extension of the output format, which may be 'py', 'html', 'tex' or 'md'.

	Example usage: ipyconverter('infile.ipynb', 'tex')

	This creates a .tex file called infile-converted.tex
	"""
	import os
	if outextension == 'py':
		outargument = '--to python ' # the trailing space is important!
	if outextension == 'tex':
		outargument = '--to latex '
	if outextension == 'html':
		outargument = '--to html '
	if outextension == 'md':
		outargument = '--to md '
	outbasename = os.path.splitext(inputfile)[0]
	output = outbasename + '-converted.' + outextension
	shellscript = 'ipython nbconvert ' + outargument + inputfile + ' --stdout > ' + output
	print "Shell command: " + shellscript
	os.system(shellscript)