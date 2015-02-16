# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Session 4: The Fraser Speech Corpus

# <markdowncell>
# **Welcome back!**

# So, what did we learn yesterday? A brief recap:

# * The **IPython** Notebook
# * **Python**: syntax, variables, functions, etc.
# * **NLTK**: manipulating linguistic data
# * **Corpus linguistic tasks**: tokenisation, keywords, collocation, stemming, concordances

# Today's focus will be on **developing more advanced NLTK skills** and using these skills to **investigate the Fraser Speeches Corpus**. In the final session, we will discuss **how to use what you have learned here in your own research**.

# *Any questions or anything before we dive in?*

# <headingcell level=2>
# Malcolm Fraser and his speeches

# <markdowncell>
# So, for much of the next two sessions, we are going to be working with a corpus of speeches made by Malcolm Fraser. 

# <codecell>
# this code allows us to display images and webpages in our notebook
from IPython.display import display
from IPython.display import display_pretty, display_html, display_jpeg, display_png, display_svg
from IPython.display import Image
from IPython.display import HTML
import nltk

# <codecell>
Image(url='http://www.unimelb.edu.au/malcolmfraser/photographs/family/105~36fam6p9.jpg')

# <markdowncell>
# Because our project here is *corpus driven*, we don't necessarily need to know about Malcolm Fraser and his speeches in order to analyse the data: we may be happy to let things emerge from the data themselves. Even so, it's nice to know a bit about him.

# Malcolm Fraser was a member of Australian parliament between 1955 and 1983, holding the seat of Wannon in western Victoria. He held a number of ministries, including Education and Science, and Defence. 

# He became leader of the Liberal Party in March 1975 and Prime Minister of Australia in December 1975, following the dismissal of the Whitlam government in November 1975.

# He retired from parliament following the defeat of the Liberal party at the 1983 election and in 2009 resigned from the Liberal party after becoming increasingly critical of some of its policies.

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

# For much of this session, we are going to manipulate the corpus data, and use the data to restructure the corpus. 

# <headingcell level=2>
# Cleaning the corpus

# <markdowncell>
# A common part of corpus building is corpus cleaning. Reasons for cleaning include:

# 1. Not break the code with unexpected input
# 2. Ensure that searches match as many examples as possible
# 3. Increasing readability, the accuracy of taggers, stemmers, parsers, etc.

# The level of kind of cleaning depends on your data and the aims of your project. In the case of very clean data (lucky you!), there may be little that needs to be done. With messy data, you may need to go as far as to correct variant spellings (online conversation, very old books).

# <headingcell level=3>
# Discussion

# <markdowncell>
# *What are the characteristics of clean and messy data? Any personal experiences? Discuss with your neighbours.* 

# It will be important to bear these characteristics in mind once you start building your own datasets and corpora. 

# <headingcell level=2>
# Exploring the corpus

# <markdowncell>
# First of all, let's load in our text.

# Via file management, open and inspect one file in *corpora/UMA_Fraser_Radio_Talks*. What do you see? Are there any potential problems?

# We can also look at file contents within the IPython Notebook itself:

# <codecell>
import os
# import tokenizers
from nltk import word_tokenize
from nltk.text import Text

# <codecell>
# make a list of files in the directory 'UMA_Fraser_Radio_Talks'
files = os.listdir('corpora/UMA_Fraser_Radio_Talks')
files[:3]

# <markdowncell>
# Actually, since we'll be referring to this path quite a bit, let's make it into a variable. This makes our code easier to use on other projects (and saves typing)

# <codecell> 
corpus_path = 'corpora/UMA_Fraser_Radio_Talks'

# <markdowncell>
# We can now tell Python to get the contents of a file in the file list and print it:

# <codecell>
# print file contents
# change zero to something else to print a different file
f = open(os.path.join(corpus_path, files[0]), "r")
text = f.read()
print text

# <headingcell level=3>
# Exploring further: splitting up text

# <markdowncell>
# We've had a look at one file, but the real strength of NLTK is to be able to explore large bodies of text. 

# When we manually inspected the first file, we saw that it contained a metadata section, before the body of the text. 

# We can ask Python to show us just the start of the file. For analysing the text, it is useful to split the metadata section off, so that we can interrogate it separately but also so that it won't distort our results when we analyse the text.

# <codecell>
# open the first file, read it and then split it into two parts, metadata and body
data = open(os.path.join(corpus_path, os.listdir(corpus_path)[0])).read().split("<!--end metadata-->")
# notice that many different commands can be strung together in one line!

# <codecell>
# view the first part
data[0]
# put print before this to change the way you see it!

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

# <codecell>
# actually, only split on the first colon
for line in data[0].split('\r\n'):
    if not line:
        continue
    if line[0] == '<':
        continue
    element = line.split(':', 1)
    print '*', element

# <headingcell level=3>
# **Challenge**: Building a Dictionary

# <markdowncell>
# We've already worked with strings, integers, and lists. Another kind of data structure in Python is a *dictionary*.

# Here is how a simple dictionary works:

# <codecell>
# create a dictionary
commonwords = {'the': 4023, 'of': 3809, 'a': 3098}
# search the dictionary for 'of'
commonwords['of']

# <codecell>
type(commonwords)

# <markdowncell>
# The point of dictionaries is to store a *key* (the word) and a *value* (the count). When you ask for the key, you get its value.

# Notice that you use curly braces for dictionaries, but square brackets for lists.

# Dictionaries are a great way to work with the metadata in our corpus. Let's build a dictionary called *metadata*:

# Your first line will look like this:

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

# <markdowncell>
# **Challenge**: define a function that creates a dictionary of the metadata for each file and gets rid of the whitespace at the start of each element

# **Hint**: to get rid of the whitespace use the *.strip()* command.

# <codecell>
# open the first file, read it and then split it into two parts, metadata and body
data = open(os.path.join(corpus_path, 'UDS2013680-100-full.txt'))
data = data.read().split("<!--end metadata-->")

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

# <markdowncell>
# Now let's build another graph, but this time by the 'Description' field:

# <codecell>
cfdist2 = ConditionalFreqDist()
for filename in os.listdir(corpus_path):
    text = open(os.path.join(corpus_path, filename)).read()
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
# **Bonus chellenge**: Build a frequency distribution graph that includes speeches without an exact date.
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

# <headingcell level=3>
# Structuring our data by metadata feature

# <markdowncell>
# Because our data samples span a long stretch of time, we thought we'd investigate the ways in which Malcolm Fraser's language changes over time. This will be the key focus of the next session.

# In order to study this, it is helpful to structure our data according to the year of the sample. This simply means creating folders for each sample year, and moving each text into the correct one.

# We can use our metadata parser to help with this task. Then, after structuring our corpus by date, we want the metadata gone, so that when we count language features in the files, we are not also counting the metadata.

# So, let's try this:

# <codecell>
import re
# a path to our soon-to-be organised corpus
newpath = 'corpora/fraser-annual'
#if not os.path.exists(newpath):
    #os.makedirs(newpath)
files = os.listdir(corpus_path)
# define a regex to match year portion of date
yearfinder = re.compile('[0-9]{4}')
for filename in files:
    # split file contents at end of metadata
    data = open(os.path.join(corpus_path, filename)).read().split("<!--end metadata-->")
    # get date from data[0]
    # use our metadata parser to get metadata
    metadata = parse_metadata(data[0])
    #look up date field of dict entry
    date = metadata.get('Date')
    # search date for year
    yearmatch = re.search(yearfinder, str(date))
    #get the year as a string
    year = str(yearmatch.group())
    # make a directory with the year name
    if not os.path.exists(os.path.join(newpath, year)):
        os.makedirs(os.path.join(newpath, year))
    # make a new file with the same name as the old one in the new dir
    fo = open(os.path.join(newpath, year, filename),"w")
    # write the content portion, without metadata
    fo.write(data[1])
    fo.close()

# <markdowncell>
# Did it work? How can we check?

# <codecell>
# print os.listdir(newpath)
# print os.listdir(newpath + '/1981')

# <headingcell level=3>
# Keywords in Fraser's speeches

# <markdowncell>
# So, we now have a structured, metadata-free corpus.

# <markdowncell>
# Last time we tried keywording, we simply looked for keywords in a single text file corpus.

# A bit part of the power of programming is that we can perform a very similar operation again and again. We should be able to generate the keywords for each subcorpus, one after the other. Using a GUI (*graphical user interface*) tool for keywording would mean that you have to reload the tool with every subcorpus, run the keyworder, save the result, unload the subcorpus, and repeat.

# So, let's do it a much more sustainable way.

# <codecell>
import os
# path to our new corpus
corpus = 'corpora/fraser-annual'
# and make an empty list to store all our output:
all_text = []
for subcorpus in os.listdir(corpus):
    subcorpus_text = []
    for txtfile in os.listdir(os.path.join(corpus, subcorpus)):
        filepath = os.path.join(corpus, subcorpus, txtfile)
        data = open(filepath).read()
        data = data.lower() # make it lowercase!
        # add the data from each file to subcorpus text
        subcorpus_text.append(data)
    # after going through each file, turn all the texts into a string
    subcorpus_text = '\n'.join(subcorpus_text)
    all_text.append(subcorpus_text)

# <markdowncell>
# So now we have each subcorpus as a list item in *all_text*. We can generate keywords for each:

# <codecell>
# reimport keyworder
import sys
sys.path.insert(0, 'spindle-code-master/keywords')
from keywords import keywords_and_ngrams 
results = []
for text in all_text:
    print all_text.index(text)
    result = keywords_and_ngrams(text)
    results.append(result[0])

# <markdowncell>
# ... and do whatever we like with our results. In the cell below, why don't you try to develop a way of printing some useful results?

# **Challenge**: print the year of each subcorpus before printing its top n keywords.

# <codecell>
# print top 10 keywords and bigrams from each subcorpus, maybe?
subcorpora = os.listdir(corpus)
for index, result in enumerate(results):
    print subcorpora[index]
    for keyword in result[:10]:
        print keyword

# <headingcell level=2>
# Adding information to the corpus

# <markdowncell>
# So far, the kinds of tasks we've done have involved meaningfully reducing data into numbers, or words into stems, etc.

# At this point in the course, we begin to add additional data to the corpora. This allows us to 'go deeper' into the texts.

# Before we start annotating our own corpora, let's just quickly play with a pre-annotated corpus.

# <codecell>
from nltk.corpus import brown
print(brown.words())
print(brown.tagged_words())

# <markdowncell>
# So, each word in the 1961 *Brown Corpus* is tagged for its part of speech, as well as some additional information. The tag descriptions are available here:

# <codecell>
HTML('<iframe src=http://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used width=700 height=350></iframe>')

# <markdowncell>
# So, we can pretty easily make lists containing all words of a given type. Below, we'll print the first 50 adverbs. Try changing the 'RB' to another kind of tag (in the list above), and see what results turn up. 

# > JJ and RB are shorthand for adjective and adverb. It's linguistics jargon from the 50s that we're stuck with now.

# <codecell>
from nltk.corpus import brown
adverbs = []
for tup in brown.tagged_words():
    # get any word whose tag is adverb
    if tup[1] == 'RB':
        adverbs.append(tup[0])
adverbs[:50]

# <markdowncell>
# It's easy to grasp the potential power of annotation: think how difficult it would be to write regular expressions that locate all adverbs!

# > **Note:** John Sinclair, an early proponent of corpus linguistics generally, was famously resistant to the use of annotation and parsing. He felt that the corpus alone should be used to build theory, rather than using existing theories (grammars) to annotate data (e.g. [2004](#ref:sinclair)). Though this is an uncommon viewpoint today, it is still useful to remember that the process of 'value-adding' is never free of theory or interpretation.

# <headingcell level=2>
# Part-of-speech tagging

# <markdowncell>
# Part-of-speech (POS) tagging is the process of assigning each token a label. Often, these labels are similar to what was used to tag the Brown Corpus.

# > **Note:** It is generally considered good practice to train your tagger by exposing it to well-annotated language of a similar variety. For reasons of scope, however, training taggers and parsers is not covered in these sessions.

# <codecell>
text = word_tokenize("We can put any text we like here, and NLTK will tag each word with its part of speech.")
tagged = nltk.pos_tag(text)
tagged

# <markdowncell>
# We could use this to search text by part of speech:

# <codecell>
for word, tag in tagged:
    if tag == 'NN':
        print word

# > In the legal profession, during the discovery process, a legal team may receive hundreds of thousands of pages of text. Searching of POS-tagged data can locate documents likely to contain important information, or at the very least, can sort texts in order of their relevance. This can save countless hours of work.

# Part of speech tagging still has some limitations, though. The problem is that words in a sentence are related in complicated ways. If we are interested in modal auxiliaries that modify the verb *tag*, we would like our search to match:

# * it **will** tag ...
# * it **could** potentially tag
# * it **can**'t always easily tag
# * and so on...

# In order to match these examples, we have to develop annotations not only of words, but groups of words. If we recognise *will tag*, *could potentially tag*, and *can't always easily tag* as verb phrases (VPs), it makes it much easier to search for the modal auxiliaries within them.

# The idea of mapping out the grammatical relationships between words in a sentence is a very, very old idea indeed. Hundreds of different models of grammar have been proposed. Right now, we'll focus on a very influential and well-known model of language called *phrase structure grammar*.

# <headingcell level=3>
# Phrase structure grammar

# <markdowncell>
# Phrase structure grammar is the tree-style representation of popularised by generative grammarians (i.e. [Chomsky 1965](#ref:chomsky)):

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/wooltree.png" />
# <br>

# <codecell>
HTML('<iframe src=http://en.wikipedia.org/wiki/Phrase_structure_grammar width=700 height=350></iframe>')

# <markdowncell>
# Originally, generative grammarians were attempting to write rules that could account for any well-formed sentence in a language. The assumption was that we could do this for many languages, and then compare grammars in order to find *linguistic universals*---things common to all languages.

# These days, people aren't so interested in this task. Phrase structure grammars, however, are still common within natural language processing. *Automatic text comprehension* and *text generation* are two tasks that are commonly approached with phrase-structure as an underlying theory.

# The task of automatically annotating this level of information is called *parsing*.

# <headingcell level=2>
# Parsing

# <markdowncell>
# Parsing involves determining parts of speech for each word, but also the underlying grammatical structure of a sentence. There are many different grammars for a language like English, and accordingly, many different parsers. There is no way of determining which parser is objectively *the best*: some work well for multiple languages, or for certain genres of communication like journalism. Speed and portability may in some contexts be very important values (think *Siri*).

# NLTK as a library contains many different kinds of parsers. It also provides interfaces to work with a number of popular parsers such as *BLLIP*, *MaltParser* or *Stanford CoreNLP*. Unfortunately for us, NLTK as a library is largely oriented toward *building* parsers, rather than simply *using* them. Building parsers is a *very* complicated thing. To build a parser, you need to write out a grammar, and train a machine to learn this grammar by feeding it a corpus of correctly annotated clauses. This kind of task is well beyond the scope of our short course.

# > If you're interested in the idea of developing a grammar, you can head [here](http://www.nltk.org/book/ch08.html) for NLTK's documentation.

# What we're going to do is use a parser that works 'out of the box', without any training. One of the simplest to use within NLTK/Python is *pyStatParser*. First, we have to get it from the web and install it.

# <codecell>
# copy the parser files
! git clone https://github.com/emilmont/pyStatParser.git
import os
# go to parser directory
os.chdir('pyStatParser')
# install parser
! python setup.py install
# back to original directory
os.chdir('..')

# <codecell>
#import parser
from stat_parser import Parser
# name and load the parser
parser = Parser()
# parse and print a sentence
tree = parser.parse("We act to prevent a wider war, to diffuse a powder keg at the heart of Europe "
    "that has exploded twice before in this century with catastrophic results.")
print tree

# <markdowncell>
# NLTK provides a *draw()* function for graphically representing these bracketted trees. With a bit of hacking, we can get IPython to show us the tree:

# <codecell>
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
cf = CanvasFrame()
# draw the tree
tc = TreeWidget(cf.canvas(),tree)
cf.add_widget(tc,10,10) # (10,10) offsets
# print it to file
cf.print_to_file('tree.ps')
# don't show it on screen (yet!)
cf.destroy()
# convert to displayable form
! convert tree.ps tree.png
# remove the old file
! rm tree.ps
# show the image
Image(filename='tree.png')

# <markdowncell>
# Below is a simple function that uses the code above to turn a sentence into a visualised tree. Insert whatever text you like as a string, and see what happens!

# <codecell>
def quicktree(sentence):
    """Parse a sentence and return a visual representation"""
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    from stat_parser import Parser
    from IPython.display import display
    from IPython.display import Image
    parser = Parser()
    parsed = parser.parse(sentence)
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(),parsed)
    cf.add_widget(tc,10,10) # (10,10) offsets
    cf.print_to_file('tree.ps')
    cf.destroy()
    ! convert tree.ps tree.png
    ! rm tree.ps
    return Image(filename='tree.png')
    ! rm tree.png

# <codecell>
quicktree("It depends upon what the meaning of the word is is.")

# <markdowncell>
# If we've got any spare time, you might like to try to build some functionality into *quicktree()*. Maybe it would be nice to be able to provide a filename, and not to delete the file after loading it ... ?

# <codecell>
# Use these cells to visualise some sentences, if you like!

# <codecell>
# 

# <codecell>
# 

# <headingcell level=2>
# Summary

# <markdowncell>
# So, that's the end of Session 4. Now, we're able to do some pretty complex stuff!

# In this session, we've generated real insights into the Fraser Corpus using corpus linguistic/distant reading techniques (keywording, ngrams, and collocation).

# We've also learned about some more advanced computational linguistic ideas, like tagging and parsing. It's good to keep in mind, however, that any kind of POS tagging or parsing is an act of interpretation. Just because it's being done by a computer doesn't mean it's objective. Certain kinds of meaning can be systematically missed by processes like parsing.

# In the next lesson, we'll use a fully parsed version of the Fraser Corpus to look for longitudinal change in his use of language. The only reason we didn't all parse the texts ourselves is that the process is computationally intensive, and takes a few hours to complete. For this reason, you actually downloaded the parsed version of the corpus at the start of the first session.

# *See you soon!*

# <headingcell level=1>
# Session 5: Charting change in Fraser's speeches

# <markdowncell>
#
# In this lesson, we investigate a fully-parsed version of the Fraser Corpus. We do this using purpose-built tools.

# In the first part of the session, we will go through how to use each of the tools. Later, you'll be able to use the tools to navigate the data and visualise results in any way you like.

# The Fraser Speeches have been parsed for part of speech and grammatical structure by [*Stanford CoreNLP*](http://nlp.stanford.edu/software/corenlp.shtml), a parser that can be loaded within NLTK. We rely on [*Tregex*](http://nlp.stanford.edu/~manning/courses/ling289/Tregex.html) to interrogate the parse trees. Tregex allows very complex searching of parsed trees, in combination with [Java Regular Expressions](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html), which are very similar to the regexes we've been using thus far.

# If you plan to work more with parsed corpora later, it's definitely worthwhile to learn the Tregex syntax in detail. For now, though, we'll use simple queries, and explain the query construction syntax as we go.

# Before we get started, we have to install Java, as some of our tools rely on some Java code. You'll very likely have Java installed on your local machine, but we need it on the cloud. To make it work, you should run the following line of code in the cloud Terminal:

#      sudo yum install java

# <markdowncell>
# OK, that's out of the way. Next, let's import the functions we'll be using to investigate the corpus. These functions have been designed specifically for our investigation, but they will work with any parsed dataset.

# We'll take a look at the code used in this session a little later on, if there's time. Much of the code is derived from things we've learned here, combined with a lot of Google and Stack Overflow searching. All our code is on GitHub too, remember. It's open-source, so you can do whatever you like with it.

# Here's an overview of the functions we'll be using, and their purpose:

# | **Function name** | Purpose                            | |
# | ----------------- | ---------------------------------- | |
# | *searchtree()*  | find things in a parse tree         | |
# | *interrogator()*  | interrogate parsed corpora         | |
# | *plotter()*       | visualise *interrogator()* results | |
# | *quickview()*     | view *interrogator()* results      | |
# | *tally()*       | get total frequencies for *interrogator()* results      | |
# | *surgeon()*       | edit *interrogator()* results      | |
# | *merger()*       | merge *interrogator()* results      | |
# | *conc()*          | complex concordancing of subcopora | |

# We can import them using IPython Magic:

# <codecell>
import os # for joining paths
from IPython.display import display, clear_output # for clearing huge lists of output
# import functions to be used here:
%run corpling_tools/interrogator.ipy
%run corpling_tools/resbazplotter.ipy
%run corpling_tools/additional_tools.ipy

# <markdowncell>
# We also need to set the path to our corpus as a variable. If you were using this interface for your own corpora, you would change this to the path to your data.

# <codecell>
path = 'corpora/fraser-corpus-annotated' # path to corpora from our current working directory.

# <headingcell level=3>
# Interrogating the corpus

# <markdowncell>
# To interrogate the corpus, we need a crash course in parse labels and Tregex syntax. Let's define a tree (from the Fraser Corpus, 1956), and have a look at its visual representation.

#      Melbourne has been transformed over the let 18 months in preparation for the visitors.

# <codecell>
melbtree = (r'(ROOT (S (NP (NNP Melbourne)) (VP (VBZ has) (VP (VBN been) (VP (VBN transformed) '
           r'(PP (IN over) (NP (NP (DT the) (VBN let) (CD 18) (NNS months)) (PP (IN in) (NP (NP (NN preparation)) '
           r'(PP (IN for) (NP (DT the) (NNS visitors)))))))))) (. .)))')

# <markdowncell>
# Notice that an OCR error caused a parsing error. Oh well. Here's a visual representation, drawn with NLTK:

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/melbtree.png" />
# <br>
# <markdowncell>
# The data is annotated at word, phrase and clause level. Embedded here is an elaboration of the meanings of tags *(ask Daniel if you need some clarification!)*:

# <codecell>
HTML('<iframe src=http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html width=700 height=350></iframe>')

# <markdowncell>
# Note that the tags are a little bit different from the last parser we were using:

# <codecell>
quicktree("Melbourne has been transformed over the let 18 months in preparation for the visitors")

# <markdowncell>
# Neither parse is perfect, but the one we just generated has a major flaw: *Melbourne* is parsed as an adverb! Stanford CoreNLP correctly identifies it as a proper noun, and also, did a better job of handling the 'let' mistake.

# <markdowncell>
# *searchtree()* is a tiny function that searches a syntax tree. We'll use the sample sentence and *searchtree()* to practice our Tregex queries. We can feed it either *tags* (S, NP, VBZ, DT, etc.) or *tokens* enclosed in forward slashes.

# <codecell>
# any plural noun
query = r'NNS'
searchtree(melbtree, query)

# <codecell>
# A token matching the regex *Melb.?\**
query = r'/Melb.?/'
searchtree(melbtree, query)

# <codecell>
query = r'NP'
searchtree(melbtree, query)

# <markdowncell>
# To make things more specific, we can create queries with multiple criteria to match, and specify the relationship between each criterion we want to match. Tregex will print everything matching **the leftmost criterion**.

# <codecell>
# NP with 18 as a descendent
query = r'NP << /18/'
searchtree(melbtree, query)

# <markdowncell>
# Using an exclamation mark negates the relationship. Try producing a query for a *noun phrase* (NP) without a *Melb* descendent:

# <codecell>
query = r'NP !<< /Melb.?/'
searchtree(melbtree, query)

# <markdowncell>
# The dollar specifies a sibling relationship between two parts of the tree---that is, two words or tags that are horizontally aligned.

# <codecell>
# NP with a sister VP
# This corresponds to 'subject' in many grammars
query = r'NP $ VP'
searchtree(melbtree, query)

# <markdowncell>
# Try changing the **more than** symbols to **less than**, and see how it affects the results.

# <codecell>
# Prepositional phrase in other prepositional phrases
query = r'PP >> PP'
searchtree(melbtree, query)

# <markdowncell>
# There is also a double underscore, which functions as a wildcard.

# <codecell>
# anything with any kind of noun tag
query = r'__ > /NN.?/'
searchtree(melbtree, query)

# <markdowncell>
# Using brackets, it's possible to create very verbose queries, though this goes well beyond our scope. Just know that it can be done!

# <codecell>
# particle verb in verb phrase with np sister headed by Melb.
# the particle verb must also be in a verb phrase with a child preposition phrase
# and this child preposition phrase must be headed by the preposition 'over'.
query = r'VBN >> (VP $ (NP <<# /Melb.?/)) > (VP < (PP <<# (IN < /over/)))'
searchtree(melbtree, query)

# <markdowncell>
# Here are two more trees for you to query, from 1969 and 1973.

#      We continue to place a high value on economic aid through the Colombo Plan, involving considerable aid to Asian students in Australia.

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/colombotree.png" />
# <br>

# <codecell>
colombotree = r'(ROOT (S (NP (PRP We)) (VP (VBP continue) (S (VP (TO to) (VP (VB place) (NP (NP (DT a) (JJ high) '
    r'(NN value)) (PP (IN on) (NP (JJ economic) (NN aid)))) (PP (IN through) (NP (DT the) (NNP Colombo) (NNP Plan))) '
    r'(, ,) (S (VP (VBG involving) (NP (JJ considerable) (NN aid)) (PP (TO to) (NP (NP (JJ Asian) (NNS students)) 
        r'(PP (IN in) (NP (NNP Australia))))))))))) (. .)))'

# <markdowncell>
#      As a result, wool industry and the research bodies are in a state of wonder and doubt about the future.

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/wooltree.png" />
# <br>

# <codecell>
wooltree = r'(ROOT (S (PP (IN As) (NP (DT a) (NN result))) (, ,) (NP (NP (NN wool) (NN industry)) (CC and) '
                 r'(NP (DT the) (NN research) (NNS bodies))) (VP (VBP are) (PP (IN in) (NP (NP (DT a) (NN state)) '
                    r'(PP (IN of) (NP (NN wonder) (CC and) (NN doubt))))) (PP (IN about) (NP (DT the) (NN future)))) (. .)))'

# <markdowncell>
# Try a few queries in the cells below.

# > If you need help constructing a Tregex query, ask Daniel. He writes them all day long for fun.

# <codecell>
query = '?'
searchtree(colombotree, query)

# <codecell>
# 

# <codecell>
#

# <codecell>
#

# <markdowncell>
# So, now we understand the basics of a Tregex query (don't worry---many queries have already been written for you. We can start our investigation of the Fraser Corpus by generating some general information about it. First, let's define a query to find every word in the corpus. Run the cell below to define the *allwords_query* as the Tregex query.

# > *When writing Tregex queries or Regular Expressions, remember to always use **r'...'** quotes!*

# <codecell>
# any token containing letters or numbers (i.e. no punctuation):
# we specify here that it cannot have any descendants,
# just to be sure we only get tokens, not tags.
allwords_query = r'/[A-Za-z0-9]/ !< __' 

# <markdowncell>
# Next, we perform interrogations with *interrogator()*. Its most important arguments are:
#
# 1. **path to corpus** (the *path* variable)
#
# 2. Tregex **options**:
#   * **'-t'**: return only words
#   * **'-C'**: return a count of matches
#
# 3. the **Tregex query**

# We only need to count tokens, so we can use the **-C** option (it's often faster than getting lists of matching tokens). The cell below will run *interrogator()* over each annual subcorpus and count the number of matches for the query.

# <codecell>
allwords = interrogator(path, '-C', allwords_query) 

# <markdowncell>
# When the interrogation has finished, we can view the total counts by getting the *totals* branch of the *allwords* interrogation:

# <codecell>
# from the allwords results, print the totals
print allwords.totals

# <markdowncell>
# If you want to see the query and options that created the results, you can print the *query* branch.

# <codecell>
print allwords.query

# <headingcell level=3>
# Plotting results

# <markdowncell>
# Lists of years and totals are pretty dry. Luckily, we can use the *plotter()* function to visualise our results. At minimum, *plotter()* needs two arguments:

# 1. a title (in quotation marks)
# 2. a list of results to plot

# <codecell>
plotter('Word counts in each subcorpus', allwords.totals)

# <markdowncell>
# Great! So, we can see that the number of words per year varies quite a lot. That's worth keeping in mind.

# Next, let's plot something more specific, using the **-t** option.

# <codecell>
query = r'/(?i)\baustral.?/' # australia, australian, australians, etc.
aust = interrogator(path, '-t', query) # -t option to get matching words, not just count

# <markdowncell>
# We now have a list of words matching the query stores in the *aust* variable's *results* branch:

# <codecell>
aust.results[:3] # just the first few entries

# <markdowncell>
# *Your turn!* Try this exercise again with a different term. 

# <markdowncell>
# We can use a *fract_of* argument to plot our results as a percentage of something else. This helps us deal with the issue of different amounts of data per year.

# <codecell>
# as a percentage of all aust* words:
plotter('Austral*', aust.results, fract_of = aust.totals)
# as a percentage of all words (using our previous interrogation)
plotter('Austral*', aust.results, fract_of = allwords.totals)

# <markdowncell>
# Great! So, we now have a basic understanding of the *interrogator()* and *plotter()* functions.

# <headingcell level=3>
# Customising visualisations

# <markdowncell>
# By default, *plotter()* plots the absolute frequency of the seven most frequent results.

#  We can use other *plotter()* arguments to customise what our chart shows. *plotter()*'s possible arguments are:

#  | plotter() argument | Mandatory/default?       |  Use          | Type  |
#  | :------|:------- |:-------------|:-----|
#  | *title* | **mandatory**      | A title for your plot | string |
#  | *results* | **mandatory**      | the results you want to plot | *interrogator()* total |
#  | *fract_of* | None      | results for plotting relative frequencies/ratios etc. | list (interrogator(-C) form) |
#  | *num_to_plot* | 7     | number of top results to display     |   integer |
#  | *multiplier* | 100     | result * multiplier / total: use 1 for ratios | integer |
#  | *x_label* | False    | custom label for the x-axis     |  string |
#  | *y_label* | False    | custom label for the y-axis     |  string |
#  | *yearspan* | False    | plot a span of years |  a list of two int years |
#  | *justyears* | False    | plot specific years |  a list of int years |
#  | *csvmake* | False    | make csvmake the title of csv output file    |  string |

# You can easily use these to get different kinds of output. Try changing some parameters below:

# <codecell>
# maybe we want to get rid of all those non-words?
plotter('Austral*', aust.results, fract_of = allwords.totals, num_to_plot = 3, y_label = 'Percentage of all words')

# <codecell>
# or see only the 1960s?
plotter('Austral*', aust.results, fract_of = allwords.totals, num_to_plot = 3, yearspan = [1960,1969])

# <markdowncell>
# **Your Turn**: mess with these variables, and see what you can plot. Try using some really infrequent results, if you like!

# <codecell>
#

# <codecell>
#

# <headingcell level=3>
# Viewing and editing results

# <markdowncell>
# Aside from *interrogator()* and *plotter()*, there are also a few simple functions for viewing and editing results.

# <headingcell level=4>
# quickview()

# <markdowncell>
# *quickview()* is a function that quickly shows the n most frequent items in a list. Its arguments are:
#
# 1. an *interrogator()* result
# 2. number of results to show (default = 50)
#
# We can see the full glory of bad OCR here:

# <codecell>
quickview(aust.results, n = 20)

# <markdowncell>
# The number shown next to the item is its index. You can use this number to refer to an entry when editing results.

# <headingcell level=4>
# tally()

# <markdowncell>
# *tally()* displays the total occurrences of results. Its first argument is the list you want tallies from. For its second argument, you can use:

# * a list of indices for results you want to tally
# * a single integer, which will be interpreted as the index of the item you want
# * a string, 'all', which will tally every result. This could be very many results, so it may be worth limiting the number of items you pass to it with [:n],

# <codecell>
tally(aust.results, [0, 3])

# <markdowncell> 
# **Your turn**: Use 'all' to tally the result for the first 11 items in aust.results

# <codecell>
tally(aust.results[:10], 'all')


# <headingcell level=4>
# surgeon()

# <markdowncell>
# Results lists can be edited quickly with *surgeon()*. *surgeon()*'s arguments are:

# 1. an *interrogator()* results list
# 2. *criteria*: either a regex or a list of indices.
# 3. *remove = True/False*

# By default, *surgeon()* removes anything matching the regex/indices criteria, but this can be inverted with a *remove = False* argument. Because you are duplicating the original list, you don't have to worry about deleting *interrogator()* results.

# We can use it to remove some obvious non-words.

# <codecell>
non_words_removed = surgeon(aust.results, [5, 9], remove = True)
plotter('Some non-words removed', non_words_removed, fract_of = allwords.totals)

# <markdowncell>
# Note that you do not access surgeon lists with *aust.non_words_removed* syntax, but simply with *non_words_removed*.

# <headingcell level=4>
# merger()

# <markdowncell>
# *merger()* is for merging items in a list. Like *surgeon()*, it duplicates the old list. Its arguments are:

# 1. the list you want to modify
# 2. the indices of results you want to merge, or a regex to match
# 3. newname = *str/int/False*: 
#   * if string, the string becomes the merged item name.
#   * if integer, the merged entry takes the name of the item indexed with the integer.
#   * if not specified/False, the most most frequent item in the list becomes the name.

# In our case, we might want to collapse *Australian* and *Australians*, because the latter is simply the plural of the former.

# <codecell>
# before:
plotter('Before merging Australian and Australians', aust.results, num_to_plot = 3)
# after:
merged = merger(aust.results, [1, 2],  newname = 'australian(s)')
plotter('After merging Australian and Australians', merged, num_to_plot = 2)

# <headingcell level=4>
# conc()

# <markdowncell>
# The final function is *conc()*, which produces concordances of a subcorpus based on a Tregex query. Its main arguments are:

# 1. A subcorpus to search *(remember to put it in quotation marks!)*
# 2. A Tregex query

# <codecell>
# here, we use a subcorpus of politics articles,
# rather than the total annual editions.
conc(os.path.join(path,'1966'), r'/(?i)\baustral.?/') # adj containing a risk word

# <markdowncell>
# You can set *conc()* to print *n* random concordances with the *random = n* parameter. You can also store the output to a variable for further searching.

# <codecell>
randoms = conc(os.path.join(path,'1963'), r'/(?i)\baustral.?/', random = 5)
randoms

# <markdowncell>
# *conc()* takes another argument, window, which alters the amount of co-text appearing either side of the match.

# <codecell>
conc(os.path.join(path,'1981'), r'/(?i)\baustral.?/', random = 5, window = 50)

# <markdowncell>
# *conc()* also allows you to view parse trees. By default, it's false:

# <codecell>
conc(os.path.join(path,'1954'), r'/(?i)\baustral.?/', random = 5, window = 30, trees = True)

# Now you're familiar with the corpus and functions, it's time to explore the corpus in a more structured way. To do this, we need a little bit of linguistic knowledge, however.

# <headingcell level=3>
# Some linguistics...

# <markdowncell>
# *Functional linguistics* is a research area concerned with how *realised language* (lexis and grammar) work to achieve meaningful social functions.

# One functional linguistic theory is *Systemic Functional Linguistics*, developed by Michael Halliday (Prof. Emeritus at University of Sydney).

# Central to the theory is a division between **experiential meanings** and **interpersonal meanings**.

# * Experiential meanings communicate what happened to whom, under what circumstances.
# * Interpersonal meanings negotiate identities and role relationships between speakers 

# Halliday argues that these two kinds of meaning are realised **simultaneously** through different parts of English grammar.

# * Experiential meanings are made through **transitivity choices**.
# * Interpersonal meanings are made through **mood choices**

# Here's one visualisation of it. We're concerned with the two left-hand columns. Each level is an abstraction of the one below it.

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/interrogator/sfl_corpling/master/cmc-2014/images/egginsfixed.jpg" />
# <br>

# Transitivity choices include fitting together configurations of:

# * Participants (*a man, green bikes*)
# * Processes (*sleep, has always been, is considering*)
# * Circumstances (*on the weekend*, *in Australia*)

# Mood features of a language include:

# * Mood types (*declarative, interrogative, imperative*)
# * Modality (*would, can, might*)
# * Lexical density---the number of words per clause, the number of content to non-content words, etc.

# Lexical density is usually a good indicator of the general tone of texts. The language of academia, for example, often has a huge number of nouns to verbs. We can approximate an academic tone simply by making nominally dense clauses: 

#       The consideration of interest is the potential for a participant of a certain demographic to be in Group A or Group B*.

# Notice how not only are there many nouns (*consideration*, *interest*, *potential*, etc.), but that the verbs are very simple (*is*, *to be*).

# In comparison, informal speech is characterised by smaller clauses, and thus more verbs.

#       A: Did you feel like dropping by?
#       B: I thought I did, but now I don't think I want to

# Here, we have only a few, simple nouns (*you*, *I*), with more expressive verbs (*feel*, *dropping by*, *think*, *want*)

# > **Note**: SFL argues that through *grammatical metaphor*, one linguistic feature can stand in for another. *Would you please shut the door?* is an interrogative, but it functions as a command. *invitation* is a nominalisation of a process, *invite*. We don't have time to deal with these kinds of realisations, unfortunately.

# <headingcell level=3>
# Fraser's speeches and linguistic theory

# <markdowncell>
# So, from an SFL perspective, when Malcolm Fraser gives a speech, he is simultaneously making meaning about events in the real world (through transitivity choices) and about his role and identity (through mood and modality choices).

# With this basic theory of language, we can create two research questions:

# 1. **How does Malcolm Fraser's tone change over time?**
# 2. **What are the major things being spoken about in Fraser's speeches, and how do they change?**

# As our corpus is well-structured and parsed, we can create queries to answer these questions, and then visualise the results.

# <headingcell level=4>
# Interpersonal features

# <markdowncell>
# We'll start with interpersonal features of language in the corpus. First, we can devise a couple of simple metrics that can teach us about the interpersonal tone of Fraser's speeches over time. We don't have time to run all of these queries right now, but there should be some time later to explore the parts of this material that interest

# <codecell>
# number of content words per clause
openwords = r'/\b(JJ|NN|VB|RB)+.?\b/'
clauses = r'S < __'
opencount = interrogator(path, '-C', openwords)
clausecount = interrogator(path, '-C', clauses)

# <codecell>
plotter('Lexical density', opencount.totals, 
        fract_of = clausecount.totals, y_label = 'Lexical Density Score', multiplier = 1)

# <markdowncell>
# We can also look at the use of modals auxiliaries (*would could, may, etc.*) over time. This can be interesting, as modality is responsible for communicating certainty, probability, obligation, etc.

# Modals are very easily and accurately located, as there are only a few possible words, and they occur in predicable places within clauses.

# Most grammars tag them with 'MD'.

# If modality interests you, later, it could be a good set of results to manipulate and plot.

# <codecell>
query = r'MD < __'
modals = interrogator(path, '-t', query)
plotter('Modals', modals.results, fract_of = modals.totals)

# <codecell>
# percentage of tokens that are I/me
query = r'/PRP.?/ < /(?i)^(i|me|my)$/'
firstperson = interrogator(path, '-C', query)

# <codecell>
plotter('First person', firstperson.totals, fract_of = allwords.totals)

# <codecell>
# percentage of questions
query = r'ROOT <<- /.?\?.?/'
questions = interrogator(path, '-C', query)

# <codecell>
plotter('Questions/all clauses', questions.totals, fract_of = clausecount.totals)

# <codecell>
# ratio of open/closed class words
closedwords = r'/\b(DT|IN|CC|EX|W|MD|TO|PRP)+.?\b/'
closedcount = interrogator(path, '-C', closedwords)

# <codecell>
plotter('Open/closed word classes', opencount.totals, 
        fract_of = closedcount.totals, y_label = 'Open/closed ratio', multiplier = 1)

# <codecell>
# ratio of nouns/verbs
nouns = r'/NN.?/ < __'
verbs = r'/VB.?/ < __'
nouncount = interrogator(path, '-C', nouns)
verbcount = interrogator(path, '-C', verbs)

# <codecell>
plotter('Noun/verb ratio', nouncount.totals, fract_of = verbcount.totals, multiplier = 1)

# <headingcell level=4>
# Experiential features of Fraser's speech

# <markdowncell>
# We now turn our attention to what is being spoken about in the corpus. First, we can get the heads of grammatical participants:

# <codecell>
# heads of participants (heads of NPS not in prepositional phrases)
query = r'/NN.?/ >># (NP !> PP)'
participants = interrogator(path, '-t', query, lemmatise = True)

# <codecell>
plotter('Participants', participants.results, fract_of = allwords.totals)

# <markdowncell>
# Next, we can get the most common processes. That is, the rightmost verb in a verbal group (take a look at the visualised tree!)

# > *Be careful not to confuse grammatical labels (predicator, verb), with semantic labels (participant, process) ... *

# <codecell>
# most common processes
query = r'/VB.?/ >># VP >+(VP) VP'
processes = interrogator(path, '-t', query, lemmatise = True)

# <codecell>
plotter('Processes', processes.results[2:], fract_of = processes.totals)

# <markdowncell>
# It seems that the verb *believe* is a common process in 1973. Try to run *conc()* in the cell below to look at the way the word behaves.

# <codecell>
# write a call to conc() that gets concordances for r'/VB.?/ < /believe/ in 1973
# conc('fraser-corpus-annotated/1973', r'/VB.?/ < /believe/)
#

# <markdowncell>
# For discussion: what events are being discussed when *believe* is the process? Why use *believe* here?
# <br>

# Next, let's chart noun phrases headed by a proper noun (*the Prime Minister*, *Sydney*, *John Howard*, etc.). We can define them like this:

# <codecell>
# any noun phrase headed by a proper noun
pn_query = r'NP <# NNP'

# <markdowncell>
# To make for more accurate results the *interrogator()* function has an option, *titlefilter*, which uses a regular expression to strip determiners (*a*, *an*, *the*, etc.), titles (*Mr*, *Mrs*, *Dr*, etc.) and first names from the results. This will ensure that the results for *Prime Minister* also include *the Prime Minister*, and *Fraser* results will include the *Malcolm* variety. The option is turned on in the cell below:

# <codecell>
# Proper noun groups
propernouns = interrogator(path, '-t', pn_query, titlefilter = True)

# <codecell>
plotter('Proper noun groups', propernouns.results, fract_of = propernouns.totals, num_to_plot = 15)

# <markdowncell>
# Proper nouns are a really good category to investigate further, as it is through proper nouns that we can track discussion of particular people, places or things. So, let's look at the top 100 results:

# <codecell>
quickview(propernouns.results, n = 100)

# <markdowncell>
#  You can now use the *merger()* and *surgeon()* options to make new lists to plot. Here's one example: we'll use *merger()* to merge places in Victoria, and then *surgeon()* to create a list of places in Australia.

# <codecell>
merged = merger(propernouns.results, [9, 13, 27, 36, 78, 93], newname = 'places in victoria')
quickview(merged, n = 100)

ausparts = surgeon(merged, [7, 9, 23, 25, 33, 41, 49], remove = False)
plotter('Places in Australia', ausparts, fract_of = propernouns.totals)

# <markdowncell>
# Neat, eh? Well, that concludes the structured part of the lesson. You now have a bit of time to explore the corpus, using the tools provided. Below, for your convenience, is a table of the functions and their arguments.

# Particularly rewarding can be playing more with the proper nouns section, as in the cells above. Shout out if you find something interesting!

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/options.png" />
# <br>

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <codecell>
#

# <markdowncell>
# By the way, here's the code behind some of the functions we've been using. With all your training, you can probably understand quite a bit of it!

# <codecell>
%load corpling_tools/additional_tools.ipy

# <markdowncell>
# That's it for this lesson, and for our interrogation of the Fraser Corpus. Remember that this is the first time anybody has conducted a sustained corpus linguistic investigation of this corpus. Everything we found here is a new discovery about the way language changes over time! (feel free to write it up and publish it!)

# The final session will look to the future: we hope to have a conversation about what you can do with the kind of skills you've learned here.

# *See you soon!*


# <headingcell level=1>
# Session 6: Getting the most out of what we've learned

# <markdowncell>
# So, now you know Python and NLTK! The main things we still have to do are:

# 1. Manage resources and results
# 2. Brainstorm some other uses for NLTK
# 3. Integrate IPython into your existing workflow
# 4. Have an open discussion about what we've done
# 5. Summarise and say goodbye!

# This lesson is pretty light on content and structure. Please do jump in at any point, and tell us about your research, and whether or not what you've learned here will be of much use.

# Or, ask us if Python can do a certain thing. Maybe we have some tips!

# <headingcell level=2>
# Managing resources and results

# <markdowncell>
# You generate huge amounts of code, data and findings. Often, it's hard to know what to do with it all. In this section, we'll provide some suggestions designed to keep your work:

# 1. Reproducible
# 2. Reusable
# 3. Comprehensible

# <headingcell level=3>
# Your code

# <markdowncell>

# 1. Most importantly, **write comments on your code**. You **will** forget what bits of code are supposed to do. Using others' code is much easier if it's commented up. 
# 2. A related point is to name your variables meaningfully: *variablexxy* does not tell us much about what it will contain. *For image in images:*  is a very comprehensible line.
# 3. Also, write docstrings for your functions. Help messages come in very handy for not only others, but yourself. Simply stating what
# 2. **Version control**. When editing your code, you may sometimes break it. [Here](https://drclimate.wordpress.com/2012/11/16/version-control/)'s a write-up about version control from Damien Irving.
# 3. **Share your code**. You are often doing novel things when you code, and sharing what you've done can save somebody else a lot of work. *GitHub* is free for open-source projects. GitHub provides version control, which is especially useful when you are working with a team.

# <headingcell level=4>
# Developing as a programmer

# <markdowncell>
# We've only scratched the surface of Python, to be honest. In fact, we've only been treating Python as a programming language. Many of its users, however, see it as more than just a programming language: it is an ideology and culture, as well. 

# You'll notice on Stack Overflow, people will remark that some solutions are more 'pythonic' than others. By this, they typically mean that the code is easy to read and broken into discrete functions. More broadly, *pythonic* refers to code that adheres to the *Zen of Python*:

# <codecell>
import this

# <markdowncell>
# So, as you explore Python more and more, you learn not only new ways to get tasks done, but also what ways are better to others. While at first you'll be content with making code that works, you'll later want to make sure your code is elegant as well. Fixing up your old code becomes a form of procrastination from thesis writing. Luckily, of all the kinds of procrastination, it's one of the better kinds.

# Another change you might notice is a switch toward *defensive programming*, where you write code to handle potential errors, and to provide useful messages when people do something wrong. This is a really awesome thing to do.

# Some code authors also try to use *test-driven development*. From [the wikipedia article](http://en.wikipedia.org/wiki/Test-driven_development):

# > First the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards.

# This helps stop feature-creep, builds your confidence, and encourages the division of long code into well-defined functions.

# Oh, and you'll probably start dreaming in code. *Not* a joke.

# <headingcell level=3>
# Your data

# <markdowncell>
# It should now be clear to you that you have data!
# Think about how you structure it. Without necessarily becoming an archivist, do think about your metadata. It will help you to manage your data later.
# *Cloud computing* offers you access to more storage and compute-power than you might want to own. Plus you're unlikely to spill coffee on it.

# <headingcell level=3>
# Your findings

# <markdowncell>
# [*Figshare*](http://www.figshare.com) is a site for storing tables and figures. It's particularly useful for working with large datasets, as we often generate far more raw tables and statistics than we can possibly publish.

# It's becoming more and more common to link journal publications to additional online resources such as GitHub code or Figshares. It's also more and more common to cite GitHub and Figshare---always nice to bump up your citation count!

# <headingcell level=2>
# Other uses of NLTK

# <markdowncell>
# What other things might we use NLTK for? A few examples, and possible workflows.

# <headingcell level=3>
# Scenario 1: You have some old books.

# <markdowncell>
# * Are they machine readable?
# * OCR options---institutional or DIY?
# * Structure them in a meaningful way---by author, by year, by language ... 
# * Start querying!

# <headingcell level=3>
# Scenario 2: You're interested in an online community.

# <markdowncell>
# * Explore the site. Sign up for it, maybe.
# * Download it: *Wget*, *curl*, *crawlers, spiders* ...
# * Extract relevant data and metadata: Python's *Beautiful Soup* library.
# * **Structure your data!**
# * Annotate your data, save these annotations
# * Start querying!

# <headingcell level=3>
# Scenario 3: Something of interest breaks in the news

# <markdowncell>
# * It will start being discussed all over the web.
# * You can use the Twitter API to harvest tweets containing a term or hashtag of interest.
# * You can get a list of RSS feeds and mine news articles
# * You can use something like *WebBootCat* to harvest search engine results and make a plain text corpus
# * Process these into a manageable form
# * Structure them
# * *Start querying!

# <headingcell level=2>
# Integrating IPython into your workflow

# <markdowncell>
# What you've learned here isn't much good unless you can pull things out of it and put them into your own research workflow.

# It's important to remember that IPython code may be a little different from vanilla Python, as it can contain Magics, shell commands, and the like.

# Perhaps the coolest thing about programming is you are simultaneously researching and developing. The functions that you write can be uploaded to the web and used by others who encounter the problem that necessitated your writing the function in the first place.

# In reality, NLTK is nothing more than a lot of Python functions, coupled with some datasets (corpora, stopword lists, etc.). You can even visit NLTK on GitHub, fork their repository, and start playing around with the code! If you find bugs in the code, or if you think documentation is lacking, you can either write directly to the people who maintain the code, or fix the problem yourself and request that they review your fix and integrate it into NLTK.

# <headingcell level=3>
# Using IPython locally

# <markdowncell>
# We've done everything on the cloud so far, and it's been pretty good to us. You may also want to use IPython locally. To do this, you need to install it. There are many ways to install it, and these vary depending on your OS and what you already have installed. See the [IPython website](http://ipython.org/ipython-doc/2/install/install.html#installnotebook) for detailed instructions.

# > *[Anaconda](http://continuum.io/downloads)* is a large package of Python-based tools (including IPython and Matplotlib) that is easy to install. 

# Once you have IPython installed, it's very easy to start using it. All you need to do is open up Terminal, navigate to the notebook directory and type:

#      ipython notebook filename.ipynb

# This will open up a blank notebook, exactly the same as the kind of notebook we've been using on the cloud. The only difference will be that if you enter:

#      os.listdir('.')

# you'll get a list of files in the directory of your notebook file, rather than a directory of your part of the cloud.

# <headingcell level=2>
# Next steps - keep going!

# <codecell>
Image(url='http://starecat.com/content/wp-content/uploads/two-states-of-every-programmer-i-am-god-i-have-no-idea-what-im-doing.jpg')

# <markdowncell>
# We hope you've learned enough in these two days to be excited about what NLTK can add to your work and you're feeling confident to start working on your own.
# Code breaks. Often. Be patient and try not to get discouraged.
# The good thing about code breaking so often is that you can find help. Try:
# * Coming back to these notebooks and refreshing your memory
# * Checking the NLTK book
# * Googling your error messages. This will often lead you to Stack Overflow, the major online community for sharing coding questions.
# * NLTK also has a Google group where people share their experiences and ask for help
# * Keep in touch! Your community is a wonderful resource.


# <headingcell level=2>
# Summaries and goodbye

# <markdowncell>
# Before we go, we should summarise what we've learned. Add all this to your CV!

# * Navigating the IPython notebook
# * Python commands - defining a variable; building a function
# * Using Python to perform basic quantitative analysis of text
# * Tagging and parsing to perform more sophisticated analysis of language
# * A crash course in corpus linguistics!
# * An appreciation of clean vs messy data and data structure
# * Data management practices

# <headingcell level=2>
# Bragging rights 

# <markdowncell>
# The work you have been doing today on the Fraser corpus is actually pretty cutting edge. Very little analysis like this has been undertaken on an Australian political corpus.

# You have produced publishable work today. Really. Be proud. And if you feel like writing up your findings, do it!

# <headingcell level=2>
# Thanks!

# <markdowncell>
# That's the end of of course. Thank you to everybody for your participation.

# Please let us know how you found the course.

# Also, [submit a pull request](https://github.com/resbaz/lessons) and improve our teaching materials! 

# <headingcell level=2>
# Bibliography

# <markdowncell>
# <a id="ref:chomsky"></a>
# Chomsky, N. (1965). Aspects of the Theory of Syntax (Vol. 11). The MIT press.
#
# Eggins, S. (2004). Introduction to systemic functional linguistics. Continuum International Publishing Group.
#
# Halliday, M., & Matthiessen, C. (2004). An Introduction to Functional Grammar. Routledge.
#
# <a id="ref:sinclair"></a>
# Sinclair, J. (2004). Trust the text: Language, corpus and discourse. Routledge. Available at
# [http://books.google.com.au/books/about/Trust_the_Text.html?id=n6xU2lyVoeQC&redir_esc=y](http://books.google.com.au/books/about/Trust_the_Text.html?id=n6xU2lyVoeQC&redir_esc=y).

# <headingcell level=3>
# Workspace

# <markdowncell>
# Here are a few blank cells, in case you need them for anything:

# <codecell>
# 
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
# 