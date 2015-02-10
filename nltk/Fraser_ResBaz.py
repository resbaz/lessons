# <headingcell level=1>
# Session 3: The Fraser Speech Corpus

# <markdowncell>
# <br>

# <headingcell level=2>
# Malcolm Fraser and his speeches

# <codecell>
# this code allows us to display images and webpages in our notebook
from IPython.display import display
from IPython.display import display_pretty, display_html, display_jpeg, display_png, display_svg
from IPython.display import Image
from IPython.display import HTML

# <codecell>
Image(url='http://www.unimelb.edu.au/malcolmfraser/photographs/family/105~36fam6p9.jpg')

# <markdowncell>
# Because our project here is *corpus driven*, we don't necessarily need to know about Malcolm Fraser and his speeches. Even so, it's nice to know a bit about him.

# <markdowncell>
# Malcolm Fraser was a member of Australian parliament between 1955 and 1983, holding the seat of Wannon in western Victoria. He held a number of ministries, including Education and Science, and Defence. 
# He became leader of the Liberal Party in March 1975 and Prime Minister of Australia in December 1975, following the dismissal of the Whitlam government in November 1975.
# He retired from parliament following the defeat of the Liberal party at the 1983 election and in 2009 resigned from the Liberal party after becoming increasingly critical of some of its policies
# He can now be found on Twitter as **@MalcolmFraser12**

# <codecell>
HTML('<iframe src=http://en.wikipedia.org/wiki/Malcolm_Fraser width=700 height=350></iframe>')

# <markdowncell>
# In 2004, Malcolm Fraser made the University of Melbourne the official custodian of his personal papers. The collection consists of a large number of photographs, speeches and personal papers, including Neville Fraser's WWI diaries and materials relating to CARE Australia, which Mr Fraser helped to found in 1987. 

# <codecell>
HTML('<iframe src=http://www.unimelb.edu.au/malcolmfraser/ width=700 height=350></iframe>')

# <markdowncell>
# Every week, between 1954 until 1983, Malcolm Fraser made a talk to his electorate that was broadcast on Sunday evening on local radio.  
# The speeches were transcribed years ago. Optical Character Recognition (OCR) was used to digitise the transcripts. This means that the texts are not of perfect quality. 
# Some have been manually corrected, which has removed extraneous characters and mangled words, but even so there are still some quirks in the formatting. 

# <headingcell level=2>
# Cleaning the corpus

# <markdowncell>
# A common part of corpus building is corpus cleaning. Reasons for cleaning include:

# 1. Not break the code with unexpected input
# 2. Ensure that searches match as many examples as possible
# 3. Increasing the accuracy of taggers, stemmers, parsers

# The level of kind of cleaning depends on your data and the aims of your project. In the case of very clean data (lucky you!), there may be little that needs to be done. With messy data, you may need to go as far as to correct variant spellings (online conversation, very old books).

# <headingcell level=3>
# Discussion

# <markdowncell>
# *What are the characterisitics of clean and messy data? Any personal experiences? Discuss with your neighbours.* 

# It will be important to bear these characteristics in mind once you start building your own datasets and corpora. 

# <headingcell level=2>
# Exploring the corpus

# <markdowncell>
# First of all, let's load in our text.
# Via file management, open and inspect one file. What do you see? Are there any potential problems?

# <codecell>
import os
# import tokenizers
from nltk import word_tokenize
from nltk.text import Text

# <codecell>
#access items in the directory 'UMA_Fraser_Radio_Talks' and view the first 3
os.listdir('corpora/UMA_Fraser_Radio_Talks')[:3]

# <headingcell level=3>
# Exploring further: splitting up text

# <markdowncell>
# We've had a look at one file, but the real strength of NLTK is to be able to explore large bodies of text. 
# When we manually inspected the first file, we saw that it contained a metadata section, before the body of the text. 
# We can ask Python to show us the start of the file. For analysing the text, it is useful to split the metadata section off, so that we can interrogate it separately but also so that it won't distort our results when we analyse the text.

# <codecell>
# Let's set the path to our corpus as a variable:
# This makes our code easier to use on other projects
corpus_path = 'corpora/UMA_Fraser_Radio_Talks'

# <codecell>
# open the first file, read it and then split it into two parts, metadata and body
data = open(os.path.join(corpus_path, os.listdir(corpus_path)[0])).read().split("<!--end metadata-->")
# notice that many different commands can be strung together in one line!

# <codecell>
# view the first part
data[0]

# <codecell>
# split into lines, add '*' to the start of each line
# \r is a carriage return, like on a typewriter.
# \n is a newline character
for line in data[0].split('\r\n'):
    print '*', line

# <codecell>
# skip empty lines and any line that starts with '<'
for line in data[0].split('\r\n'):
    if not line:
        continue
    if line[0] == '<':
        continue
    print '*', line

 # <codecell>
 # split the metadata items on ':' so that we can interrogate each one
for line in data[0].split('\r\n'):
    if not line:
        continue
    if line[0] == '<':
        continue
    element = line.split(':')
    print '*', element

#<codecell>
# actually, only split on the first colon
for line in data[0].split('\r\n'):
    if not line:
        continue
    if line[0] == '<':
        continue
    element = line.split(':', 1)
    print '*', element

# <headingcell level=3>
# # **Challenge**: Building a Dictionary

# <markdowncell>
# Let's build a dictionary called *metadata*, so that we can interrogate the files.
# To create a dictionary, use braces '{}'. Your first line will look like this:

#       metadata = {}

# <codecell>
metadata = {}
for line in data[0].split('\r\n'):
    if not line:
        continue
    if line[0] == '<':
        continue
    element = line.split(':', 1)
    metadata[element[0]] = element[-1]
print metadata

# <codecell>
# look up the date
print metadata['Date']

# <headingcell level=3>
# Building functions

# <codecell>
#open the first file, read it and then split it into two parts, metadata and body
data = open(os.path.join(corpus_path, 'UDS2013680-100-full.txt')
data = data.read().split("<!--end metadata-->")

# <markdowncell>
# **Challenge**: define a function that creates a dictionary of the metadata for each file and gets rid of the whitespace at the start of each element
# Hint - to get rid of the whitespace use the *.strip()* command.

# <codecell>
def parse_metadata(text):
    metadata = {}
    for line in text.split('\r\n'):
        if not line:
            continue
        if line[0] == '<':
            continue
        element = line.split(':', 1)
        metadata[element[0]] = element[-1].strip(' ')
    return metadata

# <markdowncell>
# Test it out!

# <codecell>
parse_metadata(data[0])

# <markdowncell>
# Now that we're confident that the function works, let's find out a bit about the corpus.
# As a start, it would be useful to know which years the texts are from. Are they evenly distributed over time? A graph will tell us!

# <codecell>
#import conditional frequency distribution
from nltk.probability import ConditionalFreqDist
import matplotlib
% matplotlib inline
cfdist = ConditionalFreqDist()
for filename in os.listdir(corpus_path):
    text = open(os.path.join(corpus_path, filename)).read()
    #split text of file on 'end metadata'
    text = text.split("<!--end metadata-->")
    #parse metadata using previously defined function "parse_metadata"
    metadata = parse_metadata(text[0])
    #skip all speeches for which there is no exact date
    if metadata['Date'][0] == 'c':
        continue
    #build a frequency distribution graph by year, that is, take the final bit of the 'Date' string after '/'
    cfdist['count'][metadata['Date'].split('/')[-1]] += 1
cfdist.plot()

# <codecell>
# Now let's build another graph, but this time by the 'Description' field
cfdist2 = ConditionalFreqDist()
for filename in os.listdir(corpus_path):
    text = open(os.path.join(corpus_path, filename))).read()
    text = text.split("<!--end metadata-->")
    metadata = parse_metadata(text[0])
    if metadata['Date'][0] == 'c':
        continue
    cfdist2['count'][metadata['Description']] += 1
cfdist2.plot()

# <headingcell level=4>
# Discussion

# <markdowncell>
# We've got messy data! What's the lesson here?
# <br>
#
# <markdowncell>
# Bonus chellenge: Build a frequency distribution graph that includes speeches without an exact date.
# Hint: you'll need to tell Python to ignore the 'c' and just take the digits

# <codecell>
cfdist3 = ConditionalFreqDist()
for filename in os.listdir(corpus_path):
    text = open(os.path.join(corpus_path, filename)).read()
    text = text.split("<!--end metadata-->")
    metadata = parse_metadata(text[0])
    date = metadata['Date']
    if date[0] == 'c':
        year = date[1:]
    elif date[0] != 'c':
        year = date.split('/')[-1]
    cfdist3['count'][year] += 1
cfdist3.plot()

# <headingcell level=1>
# Additional resources

# <markdowncell>
# If we wanted to improve our stemming/keywording work, there are a number of things we could still do.

# 1. There are also issues with capitalisation. How might we fix those?
# 2. Keep in mind, at some point, it would become necessary to stem the reference corpus as well! How would we go about stemming every dictionary entry and adding their values? Is it worth it?

# <markdowncell>
# 