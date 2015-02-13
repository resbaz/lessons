
# <headingcell level=1>
# Session 1: Orientation

# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <markdowncell>
# <br>
# Welcome to the *IPython Notebook*. Through this interface, you'll be learning a lot of things:

# * A Programming language: **Python**
# * A Python library: **NLTK**
# * Overlapping research areas: **Corpus linguistics**, **Natural language processing**, **Distant reading**
# * Additional skills: **Regular Expressions**, some **Shell commands**, and **tips on managing your data**

# You can head [here](https://github.com/resbaz/lessons/blob/master/nltk/README.md) for the fully articulated overview of the course, but we'll almost always stay within IPython. 
# Remember, everything we cover here will remain available to you after ResBaz is over, including these Notebooks. It's all accessible at the [ResBaz Github](https://github.com/resbaz/lessons/tree/master/nltk).

# **Any questions before we begin?**

# Alright, we're off!

# <headingcell level=2>
# Text as data

# <markdowncell>
# Programming languages like Python are great for processing data. In order to apply it to *text*, we need to think about our text as data.
# This means being aware of how text is structured, what extra information might be encoded in it, and how to manage to give the best results. 

# <headingcell level=2>
# What is the Natural Language Toolkit?

# <markdowncell>
# <br>
# We'll be covering some of the theory behind corpus linguistics later on, but let's start by looking at some of the tasks NLTK can help you with. 

# <markdowncell>
# NLTK is a Python Library for working with written language data. It is free and extensively documented. Many areas we'll be covering are treated in more detail in the NLTK Book, available free online from [here](http://www.nltk.org/book/).

# > Note: NLTK provides tools for tasks ranging from very simple (counting words in a text) to very complex (writing and training parsers, etc.). Many advanced tasks are beyond the scope of this course, but by the time we're done, you should understand Python and NLTK well enough to perform these tasks on your own!

# We will start by importing NLTK, setting a path to NLTK resources, and downloading some additional stuff.

# <codecell>
import nltk # imports all the nltk basics
user_nltk_dir = "/home/researcher/nltk_data" # specify our data directory
if user_nltk_dir not in nltk.data.path: # make sure nltk can access this dir
    nltk.data.path.insert(0, user_nltk_dir)
nltk.download("book", download_dir=user_nltk_dir) # download book materials to data directory

# <markdowncell>
# Oh, we've got to import some corpora used in the book as well...

# <codecell>
from nltk.book import *  # asterisk means 'everything'

# Importing the book has assigned variable names to ten corpora. We can call these names easily: 

# <codecell>
#text1
text2
#text3

# <headingcell level=3>
# Exploring vocabulary

# <markdowncell>
# NLTK makes it really easy to get basic information about the size of a text and the complexity of its vocabulary.

# *len* gives the number of symbols or 'tokens' in your text. This is the total number of words and items of punctuation.

# *set* gives you a list of all the tokens in the text, without the duplicates.

# Hence, **len(set(text3))** will give you the total number unique tokens. Remember this still includes punctuation. 

#*sorted* places items in the list into alphabetical order, with punctuation symbols and capitalised words first.

# <codecell>
len(text3)

# <codecell>
len(set(text3))

# <codecell>
sorted(set(text3)) 

# <markdowncell>
# We can investigate the *lexical richness* of a text. For example, by dividing the total number of words by the number of unique words, we can see the average number of times each word is used. 
# We can also count the number of times a word is used and calculate what percentage of the text it represents.

# <codecell>

len(text3)/len(set(text3))

# <codecell>
text4.count("American")

# <markdowncell>
# **Challenge!** 

# How would you calculate the percentage of Text 4 that is taken up by the word "America"?

# <codecell>
100.0*text4.count("America")/len(text4) 

# <headingcell level=3>
# Exploring text - concordances, similar contexts, dispersion

# <markdowncell>
# 'Concordance' shows you a word in context and is useful if you want to be able to discuss the ways in which a word is used in a text. 
# 'Similar' will find words used in similar contexts; remember it is not looking for synonyms, 
# although the results may include synonyms

# <codecell>
text1.concordance("monstrous")

# <codecell>

text1.similar("monstrous")

# <codecell>
text2.similar("monstrous")

# <codecell>

text2.common_contexts(["monstrous", "very"])  # this function takes two arguments

# <markdowncell>
# Python also lets you create graphs to display data.
# To represent information about a text graphically, import the Python library *numpy*. We can then generate a dispersion plot that shows where given words occur in a text.

# <codecell>
import numpy
% matplotlib inline # allow visuals to show up in this interface---see note below
text1.dispersion_plot(["whale"])

# <markdowncell>
# **Challenge!**
# <br>
# Create a dispersion plot for the terms "citizens", "democracy", "freedom", "duties" and "America" in the innaugural address corpus.
# What do you think it tells you? 

# <codecell>
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) # plot five words longitudinally

# <headingcell level=2>
# How Python works

# <markdowncell>
# We've seen a bit now of how NLTK can help you to interrogate a text. Let's back up and talk about Python itself and the environment we're using.

# <codecell>
# A simple welcome message printer.
# Anything after a hash is ignored
# Run a cell with shift+enter

condition = True
if condition is True:
    print 'Welcome to Python and the IPython Notebook.'

# <markdowncell>
# Success! *And so it begins ... *

# <headingcell level=2>
# The IPython Notebook

# <markdowncell>
# Before we start coding, we should familiarise ourselves with the IPython Notebook interface. Click *Help* --\> *User interface tour* to begin.
# <br>
# Keyboard shortcuts come in very handy. Click *Help* --\> *Keyboard shortcuts* to get an overview. *The more you code, the less you'll want to use your mouse!*

# <headingcell level=2>
# Python: core concepts

# <markdowncell>
# If you're new to Python, there are a few core concepts that will help you understand how everything works. Here, we'll cover:

# * Significant whitespace
# * Input/output types
# * Commands and arguments
# * Defining functions
# * Importing libraries, functions, etc.

# <headingcell level=3>
# Significant Whitespace

# <markdowncell>
# One thing that makes Python unique is that whitespace at the start of the line (use a tab for consistency!) is meaningful. 
# In many other languages, whitespace at the start of lines is simply a readability convention.

# <codecell>
# Fix this whitespace problem!

string = 'user'
if string == 'user':
print 'Phew, fixed.'

# <markdowncell>
# So, whitespace tells both Python and human readers where things start and stop.

# <codecell>
# You should be able to get different kinds of output depending on how you indent this code.

print 'Python\nis\n'
for i in ['very', 'really', 'truly']:  # repeat three times, quite arbitrarily
    print i + '\n'
    if i is 'truly':  # nested conditional
        print 'interesting!'
    else:
        print 'complicated!'
 print 'day.'  # at present, this occurs after the three repetitions.

# <headingcell level=3>
# Input/Output Types

# <markdowncell>
# * Python understands different *types* of input, including *string*, *integer*, *array*, *item* ... 
# * You need to always make sure your input types are correct, or Python won't know what to do with them.
# * For example, if you're trying to do maths, everything has to be an integer:

# <codecell>
1 + 2  # integer plus integer

# <codecell>
1 + '2'  # integer plus string

# <markdowncell>
# Note the error message. These will help you to understand what went wrong. 
# The first part looks like gobbledygook, but the rest is helpful. Line 3 of error tells us what command
# was executing when the error happened, which can assist in isolating a problem. The leading digit is the line number.
# Line 4 actually tells us what the error was - that's what we would have googled if we were looking for a solution.

# <markdowncell>
# You can determine the type of data stored in a variable with type():

# <codecell>
var = 'A string'
print type(var)
var = 42
print type(var)
var = ['item']
print type(var)

# <markdowncell>
# Sometimes you can sometimes easily convert between types.

# <codecell>
secondnumber = '2'
1 + int(secondnumber)

# <headingcell level=3>
# Basic syntax

# <markdowncell>
# Python has *variables* and *commands*. Commands may have *arguments* and *options*.

# > IPython highlights your code automatically, which can help you read it faster and spot problems.

# <codecell>
from math import sqrt  # importing math library and square root function
avariable = 50  # make a variable that is 50 as integer
answer = sqrt(avariable)  # figure out the answer by issuing a command with avariable as an argument
print answer  # tell us

# <codecell>
# This example has two arguments
from math import pow  # importing pow function (pow is short for 'power')
avariable = 50
answer = pow(avariable, 3)  # 50 to the power of 3
print answer

# <headingcell level=2>
# Advantages of IPython

# <markdowncell>
# So, we've been writing Python code in an IPython notebook. Why?

# 1. The main strength of IPython is that you can run bits of code individually, so you don't have to keep repeating things. In the previous cell, IPython remembered two ingredients in the fruit salad.
# 2. IPython also allows you to display images alongside code, and to save the input and output together.
# 3. IPython also makes learning a bit easier, as mistakes are easier to find and do not break an entire workflow.

# You can get more information on IPython, including how to install it on your own machine, at the [IPython Homepage](http://ipython.org).

# > **Note**: not everybody uses *IPython*, so later in the course we'll explain how to convert your work here into 'regular python' scripts.

# <headingcell level=3>
# Defining a function

# <markdowncell>
# You may wish to repeat an operation multiple times looking at different texts or different terms within a text. Instead of re-entering the formula every time, you can assign a name and set of actions to a particular task.

# We've just created a simple function that welcomed you and told you the time.

# Previously, we calculated the lexical diversity of a text. In NLTK, we can create a function called **lexical diversity** that runs a single line of code. We can then call this function to quickly determine the lexical density of a corpus or subcorpus.
# Advantages of functions:
# 1. Save you typing
# 2. You can be sure you're doing exactly the same operation every time
# <br>
# > **Note** Learn to love tab-completion! Typing the first one or two letters of a command you've used previously then hitting tab 
# will auto-complete that command, saving you typing (i.e. time and mistakes!). 
 
# <markdown cell>
# *Challenge!*

# Using a function, determine which of the nine texts in the NLTK Book has the highest lexical diversity score.

# <codecell>
def lexical_diversity(text):
    return len(text)/len(set(text))

# <codecell>
#After the function has been defined, we can run it:
lexical_diversity(text2)

# <markdowncell>
# The parentheses are important here as they sepatate the the task, that is the work of the function, from the data that the function is to be performed on. 
# The data in parentheses is called the argument of the function. When we use a function, we say that we 'call' it. 

# Other functions that we've used already include len() and sorted() - these were predefined. *lexical_diversity()* is one we set up ourselves; note that it's conventional to put a set of parentheses after a function, to make it clear what we're talking about.

# <headingcell level=3>
# Lists

# <markdowncell>
# Python treats a text as a long list of words. First, we'll make some lists of our own, to give you an idea of how a list behaves.

# <codecell>

sent1 = ['Call', 'me', 'Ishmael', '.']

# <codecell>
sent1

# <codecell>
len(sent1)

# <markdowncell>
# The opening sentences of each of our texts have been pre-defined for you. You can inspect them by typing in 'sent2' etc.

# You can add lists together, creating a new list containing all the items from both lists. You can do this by typing out the two lists or you can add two or more pre-defined lists. This is called concatenation.

# <codecell>
sent4 + sent1

# <markdowncell>
# We can also add an item to the end of a list by appending. When we append(), the list itself is updated. 

# <codecell>
sent1.append('Please')
sent1

# <markdowncell>
# There are some things we can do to make it easier to read the contents of a string. Note that we get some brackets and so on when we try to print the items in a list as a string.

# <codecell>
fruitsalad = []  # declare an empty list
fruitsalad.append('watermelon')  # add watermelon
fruitsalad.append('orange')  # add orange
print 'Our fruit salad contains: ' + str(fruitsalad)

# <markdowncell>
# If we want to print our ingredients in a nicer looking form, we might use a function like **join**

# <codecell>
fruitsalad = []
fruitsalad.append('watermelon')
fruitsalad.append('orange')
listasastring = ''.join(fruitsalad)  # create a string with all the list items joined together
print 'Our fruit salad contains: ' + listasastring

# <markdowncell>
# ... whoops! Still ugly. We didn't put anything in between the '' to use as a delimiter

# <codecell>
fruitsalad.append('canteloupe')
listasastring = ', '.join(fruitsalad)  # note the comma and space in quotation marks
print 'Our fruit salad contains: ' + listasastring


# <headingcell level=3>
#  Indexing Lists

# <markdowncell>
# We can navigate this list with the help of indexes. Just as we can find out the number of times a word occurs in a text, we can also find where a word first occurs. We can also navigate to different points in a text.

# <codecell>
text4.index('awaken')

# <markdowncell>
# This works in reverse as well. We can ask Python to locate the 158th item in our list (note that we use square brackets here, not parentheses)

# <codecell>
text4[158]

# <markdowncell>
# As well as pulling out individual items from a list, indexes can be used to pull out selections of text from a large corpus to inspect. We call this slicing

# <codecell>
text5[16715:16735]

# <markdowncell>
# If we're asking for the beginning or end of a text, we can leave out the first or second number. For instance, [:5] will give us the first five items in a list while [8:] will give us all the elements from the eighth to the end. 

# <codecell>
text2[:10]
text4[145700:]

# <markdowncell>
# To help you understand how indexes work, let's create one.

# We start by defining the name of our index and then add the items. You probably won't do this in your own work, but you may want to manipulate an index in other ways. Pay attention to the quote marks and commas when you create your test sentence.

# <codecell>
sent = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
sent[0]
sent[8]

# Note that the first element in the list is zero. This is because we are telling Python to go zero steps forward in the list. If we use an idnex that is too large (that is, we ask for something that doesn't exist), we'll get an error.

# We can modify elements in a list by assigning to one of its index values. We can also replace a slice with new material.

# <codecell>

sent[2] = 'furry'
sent[7] = 'spotty'
sent

# <headingcell level=3>
#  Defining variables

# <markdowncell>
# In Python, we give the items we're working with names, a process called assignment. For instance, in the NLTK corpus, 'Sense and Sensibility' has been assigned the name 'text2', which is much easier to work with. 
# We also assigend the name 'sent' to the sentence that we created in the previous exercise, so that we could then instruct Python to do various things with it. Assigning a variable in python looks like this:
# variable = expression
# You can call your variables (almost) anything you like, but it's a good idea to pick names that will be meaningful and easy to type. You can't use words that already have a meaning in Python, such as import, def, or not. If you try to use a word that is reserved, you'll get a syntax error.

# <markdowncell>
# *Challenge*
# 1. Create a list called 'Opening' that consists of the phrase "It was a dark and stormy night; the rain fell in torrents"
# 2. Create a variable called 'clause' that contains the contents of 'Opening', up to the semi-colon
# 3. Create a variable called 'alphabetised' that sorts 'clause' alphabetically
# 4. Print 'alphabetised' 

# <codecell>

opening = ['It', 'was', 'a', 'dark', 'and', 'stormy', 'night', ';' 'the', 'rain', 'fell', 'in', 'torrents']
clause = opening[0:7]
alphabetised = sorted(clause)

# Note that assigning a variable just causes Python to remember that information without generating any output. 
# If you want Python to show you the result, you have to ask for it (this is a good thing when you assign a variable to a very long list!).

# <codecell>

clause


# <codecell>

alphabetised


# <headingcell level=3>
# Exploring vocabulary 2

# <markdowncell>
# We can use Python's ability to perform statistical analysis of data to do further exploration of vocabulary. For instance, we might want to be able to find the most common or least common words in a text. We'll start by looking at frequency distribution.


# <codecell>
fdist1 = FreqDist(text1)

# <codecell>
fdist1.most_common(50)

# <codecell>
fdist1['whale']

# <codecell>
fdist1.plot(50, cumulative = True)

# <markdowncell>
# *Challenge!*

# Create a function called "Common_Words" and use it to compare the 15 most common words of four of the texts in the NLTK book. 
# Discuss what you found with your neighbour

# <codecell>
# As well as counting individual words, we can count other features of vocabulary, such as how often words of different lengths occur. We do this by putting together a number of the commands we've already learned.
# We could start like this: [len(w) for w in text1], but this would print the length of every word in the whole book, so let's skip that bit!

# <codecell>

fdist2= FreqDist(len(w) for w in text1)

# <codecell>

fdist2.max()


# <codecell>

fdist2.freq(3)


# <markdowncell>
# These last two commands tell us that the most common word length is 3, and that these 3 letter words account for about 20% of the book. 
# We can see this just by visually inspecting the list produced by fdist2.most_common(), but if this list were too long to inspect readily, or we didn't want to print it, there are other ways to explore it.  


# <markdowncell> 
# It is possible to select the longest words in a text, which may tell you something about its vocabulary and style

# <codecell>
v = set(text4)
long_words = [word for word in v if len(word) > 15]
sorted(long_words)


# <markdowncell>
# We can fine-tune our selection even further by adding further conditions. For instance, we might want to find long words that occur frequently (or rarely)
# *Challenge!*

# Can you find all the words in a text that are more than seven letters long and occur more than seven times?

# <codecell>
fdist3 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

# <markdowncell>
# There are a number of functions defined for NLTK's frequency distributions:

# * fdist = FreqDist(samples)   create a frequency distribution containing the given samples
# * fdist[sample] += 1  increment the count for this sample
# * fdist['monstrous']  count of the number of times a given sample occurred
# * fdist.freq('monstrous')     frequency of a given sample
# * fdist.N()   total number of samples
# * fdist.most_common(n)    the n most common samples and their frequencies
# * for sample in fdist:    iterate over the samples
# * fdist.max()     sample with the greatest count
# * fdist.tabulate()    tabulate the frequency distribution
# * fdist.plot()    graphical plot of the frequency distribution
# * fdist.plot(cumulative=True)     cumulative plot of the frequency distribution
# * fdist1 |= fdist2    update fdist1 with counts from fdist2
# * fdist1 < fdist2     test if samples in fdist1 occur less frequently than in fdist2


# <markdowncell>
# We can also find words that typically occur together, which tend to be very specific to a text or genre of texts. We'll talk more about these features and how to use them later.

# <codecell>
text4.collocations()

# <markdowncell>
# We can also use numerical operators to refine the types of searches we ask Python to run. We can use the following relational operators:

# * <       less than
# * <=      less than or equal to
# * ==      equal to (note this is two "=" signs, not one)
# * !=      not equal to
# * \>      greater than
# * \>=     greater than or equal to

# <markdowncell>
# *Challenge!*
# Using one of the pre-defined sentences in the NLTK corpus, use the relational operators above to find:

# <markdowncell>
# 1. Words longer than four characters
# 2. Words of four or more characters
# 3. Words of exactly four characters

# <codecell>
#
# <markdowncell>
# We can also look for features such as letter combinations, upper and lowercase letters, and digits. Some operators you might like to use are:

# * s.startswith(t) test if s starts with t
# * s.endswith(t)   test if s ends with t
# * t in s          test if t is a substring of s
# * s.islower()     test if s contains cased characters and all are lowercase
# * s.isupper()     test if s contains cased characters and all are uppercase
# * s.isalpha()     test if s is non-empty and all characters in s are alphabetic
# * s.isalnum()     test if s is non-empty and all characters in s are alphanumeric
# * s.isdigit()     test if s is non-empty and all characters in s are digits
# * s.istitle()     test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)

# <codecell>
sorted(w for w in set(text1) if w.endswith('ableness'))

# <codecell>
sorted(n for n in sent7 if n.isdigit())

# <markdowncell>
# **Bonus!**

# You'll remember right at the beginning we started looking at the size of the vocabulary of a text, but there were two problems with the results we got from using **len(set(text1)**. 

# This count includes items of punctuation and treats capitalised and non-capitalised words as different things (*This* vs *this*). We can now fix this. We can start by getting rid of capitalised words, then we can get rid of the punctuation and numbers

# <codecell>
len(set(word.lower() for word in text1))


# <codecell>
len(set(word.lower() for word in text1 if word.isalpha()))

# <markdowncell>
# <img style="float:left" src="http://images.catsolonline.com/cache/custom/CEN/CE651-250x250.jpg" />
# <br>

# <markdowncell>
# You've completed the introduction to Python Natural Language Toolkit! To summarise, here's what you've learned so far:

# * How to navigate the iPython notebook
# * How Python uses whitespace 
# * Why functions are useful and how to define one
# * How to use basic Python commands to start exploring features of a text
#
# We'll practice all these commands in the following lessons ... so don't panic!

# It's a lot to take in and it will probably take a while before you feel really comfortable.

# <headingcell level=1>
# Session 2: Common NLTK tasks

# <markdowncell>
# <br>
# In this session we provide an quick introduction to the field of *corpus linguistics*. We then engage with common uses of NLTK within these areas, such as sentence segmentation, tokenisation and stemming. Often, NLTK has inbuilt methods for performing these tasks. As a learning exercise, however, we will sometimes build basic tools from scratch.

# <headingcell level=2>
# Corpus linguistics

# <markdowncell>
# Though corpus linguistics has been around since the 1950s, it is only in the last 20 years that its methods have been made available to individual researchers. GUIs including [Wordsmith Tools](http://www.lexically.net/wordsmith/) and [AntConc](http://www.laurenceanthony.net/software.html). 

# Alongside the development of GUIs, there has also been a shift from *general, balanced corpora* (corpora seeking to represent a language generally) toward *specialised corpora* (corpora containing texts of one specific type, from one speaker, etc.). More and more commonly, texts are taken from the Web.

# > **Note:** We'll discuss building corpora from online texts in Session 6.

# After a long period of resistance, corpus linguistics has gained acceptence within a number of research areas. A few popular applications are within:

# * **Lexicography** (creating usage-based definitions of words and locating real examples)
# * **Language pedagogy** (advanced language learners can use a concordancing GUI or collocation tests to understand how certain words are used in the target language)
# * **Discourse analysis** (researching how meaning is made beyond the level of the clause/sentence)

# Notably, corpus linguistic methods have been embraced within the emerging paradigm of Digital Humanities, where it's sometimes called *distant reading*.

# <headingcell level=3>
# Corpora and discourse

# <markdowncell>
# As hardware, software and data become more and more available, people have started using corpus linguistic methods for discourse-analytic work. Paul Baker refers the combination of corpus linguistics and (critical) discourse analysis as a *useful methodological synergy*. Corpora bring objectivity and empiricism to a qualitative, interpretative tradition, while discourse-analytic methods provide corpus linguistics with a means of contextualising abstracted results.

# Within this area, researchers rely on corpora to varying extents. In *corpus-driven* discourse analysis, researchers interpret the corpus based on the findings of the corpus interrogation. In *corpus-assisted* discourse analysis, researchers may use corpora to provide evidence about the way a given person/idea/discourse is commonly represented by certain people/in certain publications etc.

# Our work here falls under the *corpus-driven* heading, as we are exploring the dataset without any major hypotheses in mind.

# > **Note:** Some linguists remain skeptical of corpus linguistics generally. In a well-known critique, Henry Widdowson ([2000, p. 6-7](#ref:widdowson)) said:
# >
# > Corpus linguistics \[...\] (there) is no doubt that this is an immensely important development in descriptive linguistics. That is not the issue here. The quantitative analysis of text by computer reveals facts about actual language behaviour which are not, or at least not immediately, accessible to intuition. There are frequencies of occurrence of words, and regular patterns of collocational co-occurrence, which users are unaware of, though they must be part of their competence in a procedural sense since they would not otherwise be attested. They are third person observed data ('When do they use the word X?') which are different from the first person data of introspection ('When do I use the word X?'), and the second person data of elicitation ('When do you use the word X?'). Corpus analysis reveals textual facts, fascinating profiles of produced language, and its concordances are always springing surprises. They do indeed reveal a reality about language usage which was hitherto not evident to its users.
# >
# > But this achievement of corpus analysis at the same time necessarily defines its limitations. For one thing, since what is revealed is contrary to intuition, then it cannot represent the reality of first person awareness. We get third person facts of what people do, but not the facts of what people know, nor what they think they do: they come from the perspective of the observer looking on, not the introspective of the insider. In ethnomethodogical terms, we do not get member categories of description. Furthermore, it can only be one aspect of what they do that is captured by such quantitative analysis. For, obviously enough, the computer can only cope with the material products ofwhat people do when they use language. It can only analyse the textual traces of the processes whereby meaning is achieved: it cannot account for the complex interplay of linguistic and contextual factors whereby discourse is enacted. It cannot produce ethnographic descriptions of language use. In reference to Hymes's components of communicative competence (Hymes 1972), we can say that corpus analysis deals with the textually attested, but not with the encoded possible, nor the contextually appropriate.
# > 
# > To point out these rather obvious limitations is not to undervalue corpus analysis but to define more clearly where its value lies. What it can do is reveal the properties of text, and that is impressive enough. But it is necessarily only a partial account of real language. For there are certain aspects of linguistic reality that it cannot reveal at all. In this respect, the linguistics of the attested is just as partial as the linguistics of the possible.

# <headingcell level=2>
# Loading a corpus

# <markdowncell>
# First, we have to load a corpus. We'll use a text file containing posts to an Australian forum. This file is available online, at the [ResBaz Github](https://github.com/resbaz). We can ask Python to get it for us. 

# > Later in the course, we'll discuss how to extract data from the Web and turn this data into a corpus.

# <codecell>
from urllib import urlopen # a library for working with urls
url = "https://raw.githubusercontent.com/resbaz/lessons/master/nltk/corpora/oz_politics/ozpol.txt" # define the url
raw = urlopen(url).read() # download and read the corpus into raw variable
raw = unicode(raw.lower(), 'utf-8') # make it lowercase and unicode
print len(raw) # how many characters does it contain?
print raw[:2000] # first 2000 characters

# <markdowncell>
# We actually already downloaded this file when we first cloned the ResBaz GitHub repository. It's in our *corpora* folder. We can access it like this:

# <codecell>
f = open('corpora/oz_politics/ozpol.txt')
raw = f.read()
raw = unicode(raw.lower(), 'utf-8') # make it lowercase and unicode
len(raw)
print raw[:2000] 

# <headingcell level=2>
# Regular Expressions

# <markdowncell>
# Before we go any further, we need to talk about Regular Expressions. Regular Expressions (regexes) are ways of searching for complex patterns in strings. Regexes are standardised across many programming platforms, and can also be used in GUI text editors and word processers.

# <codecell>
import nltk # just in case (you should only need to import a library once per session, but nothing bad will happen if you do it again)
import re # import this before using regexes!

# <markdowncell>
# If only using alphanumeric characters and spaces, regexes work like any normal search.

# <codecell>
# print only match
regex = re.compile(r"government")
re.findall(regex, raw)

# <markdowncell>
# Hmm ... not very useful.

# <codecell>
# print whole line
regex = re.compile(r'government')
for line in raw.splitlines():
    if regex.search(line) is not None:
        print line

# <markdowncell>
# ... but regex can be much more powerful than that. Certain characters have special meanings:

# * . (period): any character
# * * (asterisk): any number of times
# * \b: word boundary
# * ^ (carat): start of a line
# * $ (dollar sign): end of a line
# * + (plus): one or more times
# * [xy]: either x or y
# * o{5}: five os in a row
# * o{5,}: at least five os in a row
# * o{,5}: max five os in a row
# * (any|of|these|words)

# <codecell>
# [a-z] means any letter
# the plus means ''one or more of the thing before''
regex = re.compile(r"[a-z]+ment")
# find all instances of regex in raw
results = re.findall(regex, raw)
sorted(set(results)) # sort and print only unique results

# <codecell>
# word at start of line that ends in ion:
regex = re.compile(r"^[a-z]+ion\b")
# find all instances of regex in raw
results = re.findall(regex, raw)
sorted(set(results)) # sort and print only unique results

# <markdowncell>
# Sometimes, we want match the special characters:

# <codecell>
string = 'What!? :) U fink im flirtin wit *u*!? LOL'
# define a regex:
regex = re.compile(r':)')
re.findall(regex, string)

# <markdowncell>
# What happened? Well, if you want to search for any special character, it must be 'escaped' by a backslash:

# <codecell>
string = 'What!? :) U fink im flirtin wit *u*!? LOL'
# define a regex:
regex = re.compile(r':\)')
re.findall(regex, string)

# <markdowncell>
# Regular expressions take a while to master, but have great benefits for searching large texts for very specific things. Here are some additional regex resources:

# * [Regex Info](http://www.regular-expressions.info/): tutorials etc.
# * [Regexr](http://www.regexr.com/): a place to build and test out your regex
# * [Regex crosswords](http://regexcrossword.com/): exactly what you think it is!

# <markdowncell>
# The code below will get any word over *minlength* alphabetic characters by passing an integer into a regex.

# <codecell>
minlength = 5  # minimum number of letters as integer 
# gets passed into the building of the regex
sentence = 'We, the democratically-elected leaders of our people, hereby declare Kosovo to be an independent and sovereign state'

# any letter, minlength times:
pattern = re.compile(r'[A-Za-z]{' + str(minlength) + ',}') 
# What happens if you add a hyphen after 'a-z' inside the square brackets above?
re.findall(pattern, sentence)

# <headingcell level=2>
# Sentence segmentation

# <markdowncell>
# So, with a basic understanding of regex, we can now start to turn our corpus into a structured resource. At present, we have 'raw', a very, very long string of text.

#  We should break the string into segments. First, we'll split the corpus into sentences. This task is a pretty boring one, and it's tough for us to improve on existing resources. We'll try, though.

# Let's define a sentence as any string ending with (one or more) newline, full stop, question mark, or exclamation mark. A regex can be written to find these, and the split() function can  be used to break the string into a list of strings.

# <codecell>
import re
sentences = re.split("(\n|\.|\?|!)+", raw)
print 'Sentence: ' + '\nSentence: '.join(sentences[:10]) # print the first ten sentences

# <markdowncell>
# Well, it worked, sort of. What problems do we have?

# 1. sh.thole was split
# 2. Empty matches/punctuation only matches

# So, to fix our first problem, we have to make an intpretative decision. Is *sh.thole* a word? We could:

# 1. Clean the corpus and remove this false positive
# 2. Define sentence differently

# We'll go with the second option, for better or worse. The regex in the code below makes sure that any sentence final character must not be followed by a letter.

# <codecell>
sentences = re.split("(?:\n|\.|\?|!)+([^a-zA-Z]|$)", raw)
print 'Sentence: ' + '\nSentence: '.join(sentences[:10])

# <markdowncell>
# Problem 1 is solved: *sh.thole* is now a single token. To fix Problem 2, we will remove list items not containing a letter, as any sentence must contain at least one by definition.

# <codecell>
regex = re.compile('[a-zA-Z]')
no_blanklines = [sentence for sentence in sentences if regex.match(sentence)]
# or, an alternative approach using filter function:
# no_blanklines = filter(regex.match, sentences)
print 'Sentence: ' + '\nSentence: '.join(no_blanklines[:20]) # this should be better!

# <markdowncell>
# The code below turns out sentence segmenter into a function.

# <codecell>
def sent_seg(string):
    allmatches = re.split("(?:\n|\.|\?|!)+([^a-zA-Z]|$)", string)
    regex = re.compile('[a-zA-Z]')
    sentences = [sentence for sentence in allmatches if regex.match(sentence)]
    length = len(sentences)
    return sentences

# <codecell>
# Call the segmenter on our raw text here. Store it in a variable called 'sents'

# <markdowncell>
# It's all academic, anyway: NLTK actually has a sentence segmenter built in that works better than ours (we didn't deal with quotation marks, or brackets, for example).

# <codecell>
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(raw)
sents[101:111]

# <markdowncell>
# Alright, we have sentences. Now what?

# <headingcell level=2>
# Tokenisation

# <markdowncell>
# Tokenisation is simply the process of breaking texts down into words. We already did a little bit of this in Session 1. We won't build our own tokenizer, because it's not much fun. NLTK has one we can rely on.

# Keep in mind that definitions of tokens are not standardised, especially for languages other than English. Serious problems arise when comparing two corpora that have been tokenised differently.

# > **Note:** It is also possible to use NLTK to break tokens into morphemes, syllables, or phonemes. We're not going to go down those roads, though.

# <codecell>
tokenized_sents = [nltk.word_tokenize(i) for i in sents]
print tokenized_sents[:10]
# another view:
# tokenized_sents[:10]

# <headingcell level=2>
# Stemming

# <markdowncell>
# Stemming is the task of finding the stem of a word. So, *cats --> cat*, or *taking --> take*. It is an important task when counting words, as often the counting each inflection seperately is not particuarly helpful: forms of the verb 'to be' might seem under-represented if we could *is, are, were, was, am, be, being, been* separately. 

# NLTK has pre-programmed stemmers, but we can build our own using some of the skills we've already learned.

# A stemmer is the kind of thing that would make a good function, so let's do that.

# <codecell>
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']: # list of suffixes
        if word.endswith(suffix):
            return word[:-len(suffix)] # delete the suffix
    return word

# <markdowncell>
# Let's run it over some text and see how it performs.

# <codecell>
# empty list for our output
stemmed_sents = []
for sent in tokenized_sents:
    # empty list for stemmed sentence:
    stemmed = []
    for word in sent:
        # append the stem of every word
        stemmed.append(stem(word))
    # append the stemmed sentence to the list of sentences
    stemmed_sents.append(stemmed)
# pretty print the output
stemmed_sents[:10]

# <markdowncell>
# Looking at the output, we can see that the stemmer works: *wingers* becomes *winger*, and *tearing* becomes *tear*. But, sometimes it does things we don't want: *Nothing* becomes *noth*, and *mate* becomes *mat*. Even so, for the learns, let's rewrite our function with a regex:

# <codecell>
def stem(word):
    import re
    # define a regex to get word, and common suffixes
    regex = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regex, word)[0]
    return stem

# <markdowncell>
# Because we just redefined the *stem()* function, we can run the previous code and get different results.


# <markdowncell>
# Here's a very quick implementation of our stemmer on our raw tokens:

# <codecell>
tokens = nltk.word_tokenize(raw)
stemmed = [stem(t) for t in tokens]
print stemmed[:50]

# <markdowncell>
# We can see that this approach has obvious limitations. So, let's rely on a purpose-built stemmer. These rely in part on dictionaries. Note the subtle differences between the two possible stemmers:

# <codecell>
# define stemmers
lancaster = nltk.LancasterStemmer()
porter = nltk.PorterStemmer()
# stem each word in tokens
stems = [lancaster.stem(t) for t in tokens]  # replace lancaster with porter here
print stems[:100]

# <markdowncell>
# Notice that both stemmers handle some things rather poorly. The main reason for this is that they are not aware of the *word class* of any particular word: *nothing* is a noun, and nouns ending in *ing* should not have *ing* removed by the stemmer (swing, bling, ring...). Later in the course, we'll start annotating corpora with grammatical information. This improves the accuracy of stemmers a lot.

# > Note: stemming is not *always* the best thing to do: though *thing* is the stem of *things*, things has a unique meaning, as in *things will improve*. If we are interested in vague language, we may not want to collapse things --> thing.

# <headingcell level=2>
# Keywording: 'the aboutness of a text'

# <markdowncell>
# Keywording is the process of generating a list of words that are unusually frequent in the corpus of interest. To do it, you need a *reference corpus*, or at least a *reference wordlist* to which your *target corpus* can be compared. Often, *reference corpora* take the form of very large collections of language drawn from a variety of spoken and written sources.

# Keywording is what generates word-clouds beside online news stories, blog posts, and the like. In combination with speech-to-text, it's used in Oxford University's [Spindle Project](http://openspires.oucs.ox.ac.uk/spindle/) to automatically archive recorded lectures with useful tags.

# In fact, the keywording part of the Spindle Project is written in Python, and in open source.

# Spindle has sensible defaults for keyword calculation. Let's download their code and use it to generate keywords from our corpus.

# <codecell>
import sys
 # download spindle from github
!wget https://github.com/sgrau/spindle-code/archive/master.zip
!unzip master.zip # unzip it
!rm master.zip # remove the zip file
# put the keyworder directory in python's path, so we can call it easily
sys.path.insert(0, 'spindle-code-master/keywords')
# import the function
from keywords import keywords_and_ngrams # import keywords function

# <codecell>
# this tool works with raw text, not tokens!
keywords_and_ngrams(raw.encode("UTF-8"), nBigrams = 0)

# <markdowncell>
# Success! We have keywords.

# > Keep in mind, the BNC reference corpus was created before ISIS and ISIL existed. *Moslem/moslems* is a dispreferred spelling of Muslim, used more frequently in anti-Islamic discourse. Also, it's unlikely that a transcriber of the spoken BNC would choose the Moslem spelling. *Having an inappropriate reference corpus is a common methodological problem in discourse analytic work*.

# Our keywords would perhaps be better if they were stemmed. That shouldn't be too hard for us:

# <codecell>
keywords_and_ngrams(stems, nBigrams = 0) # this will use our corpus of stems, as defined earlier.

# <markdowncell>
# Rats! Keywording with stems actually revealed a list of incorrect stems.

# What re really need to do is improve our stemmer, and then come back and try again.

# <headingcell level=2>
# A return to stemming

# <markdowncell>
# Keywords and ngram searches actually work by comparing a corpus to a reference corpus. In our case, we have been using a dictionary of words in the 100 million word *British National Corpus*. We could use this same dictionary to make sure our stemmer does not create non-words when it stems.

# First, let's get a list of common words in the BNC from the *pickle* provided by SPINDLE (*pickle* is a kind of list compression).

# <codecell>
import pickle
import os
# unpack the pickled list
bncwordlist = pickle.load(open('spindle-code-master/keywords/bnc.p', 'rb')) 
bnc_commonwords = [] # empty list
for word in bncwordlist:
    getval = bncwordlist[word] # find out number of occurrences of word
    if getval > 20: # if more than 20
        bnc_commonwords.append(word) # add to common word list
print bnc_commonwords[:200] # what are our results?

# <markdowncell>
# So, this gives us a list of any word appearing more than twenty times in the BNC. We could build this function into our stemmer:

# <codecell>
# Now, let's use this as the dict for our stemmer
# The third variable sets a default threshold, but also allows us to enter one.
def newstemmer(words, stemmer, threshold = 20):
    """A stemmer that uses Lancaster/porter stemmer plus a dictionary."""
    import pickle
    import os
    import nltk
    bncwordlist = pickle.load(open('spindle-code-master/keywords/bnc.p', 'rb'))
    bnc_commonwords = {k for (k,v) in bncwordlist.iteritems() if v > threshold}
    # if words is a raw string, tokenise it
    if type(words) == unicode or type(words) == string:
        tokens = nltk.word_tokenize(words)
    # or, if list of tokens, duplicate the list
    else:
        tokens = words
        # define stemmer based on the argument we passed in
    if stemmer == 'Lancaster':
        stemmertouse = nltk.LancasterStemmer()
    if stemmer == 'Porter':
        stemmertouse = nltk.PorterStemmer()
    # empty list of stems
    stems = []
    for w in tokens:
        # stem each word
        stem = stemmertouse.stem(w)
        # if the stem is in the bnc list
        if stem in bnc_commonwords:
            # add the stem
            stems.append(stem)
        else:
            # or else, just add the word as it was
            stems.append(w)
    return stems

# <markdowncell>
# Now, we can fiddle with the stemmer and BNC frequency to get different keyword lists.

# <codecell>
# try raising the threshold if there are still bad spellings!
stemmed = newstemmer(raw, 'Lancaster', 10)

# <codecell>
keys = keywords_and_ngrams(stemmed)
keys[0] # only keywords
keys[1] # only n-grams

# <headingcell level=2>
# Collocation

# <markdowncell>
# > *You shall know a word by the company it keeps.* - J.R. Firth, 1957

# Collocation is a very common area of interest in corpus linguistics. Words pattern together in both expected and unexpected ways. In some contexts, *drug* and *medication* are synonymous, but it would be very rare to hear about *illicit* or *street medication*. Similarly, doctors are unlikely to perscribe the *correct* or *appropriate drug*.

# This kind of information may be useful to lexicographers, discourse analysts, or advanced language learners.

# In NLTK, collocation works from ordered lists of tokens. Let's put out tokenised sents into a single, huge list of tokens:

# <codecell>
allwords = []
# for each sentence,
for sent in tokenized_sents:
    # for each word,
    for word in sent:
        # make a list of all words
        allwords.append(word)
print allwords[:20]
# small challenge: can you think of any other ways to do this?

# <markdowncell>
# Now, let's feed these to an NLTK function for measuring collocations:

# <codecell>
# get all the functions needed for collocation work
from nltk.collocations import *
# define statistical tests for bigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
# go and find bigrams
finder = BigramCollocationFinder.from_words(allwords)
# measure which bigrams are important and print the top 30
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# So, that tells us a little: we can see that terrorists, Muslims and the Middle East are commonly collocating in the text. At present, we are only looking for immediately adjacent words. So, let's expand out search to a window of *five words either side*

# ''window size'' specifies the distance at which 
# two tokens can still be considered collocates
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# Now we have the appearance of very common words! Let's use NLTK's stopwords list to remove entries containing these:

# <codecell>
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
# get a list of stopwords from nltk
ignored_words = nltk.corpus.stopwords.words('english')
# make sure no part of the bigram is in stopwords
finder.apply_word_filter(lambda w: len(w) < 2 or w.lower() in ignored_words)
finder.apply_freq_filter(2)
#print the sorted collocations
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# There! Now we have some interesting collocates. Finally, let's remove punctuation-only entries, or entries that are *n't*, as this is caused by different tokenisers:

# <codecell>
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
ignored_words = nltk.corpus.stopwords.words('english')
# anything containing letter or number
regex = r'[A-Za-z0-9]'
# the n't token
nonot = r'n\'t'
# lots of conditions!
finder.apply_word_filter(lambda w: len(w) < 2 or w.lower() in ignored_words or not re.match(regex, w) or re.match(nonot, w))
finder.apply_freq_filter(2)
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# You can get a lot more info on collocation at the [NLTK homepage](http://www.nltk.org/howto/collocations.html).

# <headingcell level=2>
# Clustering/n-grams

# <markdowncell>
# Clustering is the task of finding words that are commonly **immediately** adjacent (as opposed to collocates, which may just be nearby). This is also often called n-grams: bigrams are two tokens that appear together, trigrams are three, etc.

# Clusters/n-grams have a spooky ability to tell us what a text is about.

# We can use *Spindle* for bigram searching as well:

# <codecell>
# an argument here to stop keywords from being produced.
keywords_and_ngrams(raw.encode("UTF-8"), nKeywords=0)

# <markdowncell>
# There's also a method for n-gram production in NLTK. We can use this to understand how n-gramming works.

# Below, we get lists of any ten adjacent tokens:

# <codecell>
from nltk.util import ngrams
# define a sentence
sentence = 'give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime'
# length of ngram
n = 10
# use builtin tokeniser (but we could use a different one)
tengrams = ngrams(sentence.split(), n)
for gram in tengrams:
  print gram

# <markdowncell>
# So, there are plenty of tengrams in there! What we're interested in, however, is duplicated n-grams:

# <codecell>
# arguments: a text, ngram size, and minimum occurrences
def ngrammer(text, gramsize, threshold = 4):
    """Get any repeating ngram containing gramsize tokens"""
    # we need to import this in order to find the duplicates:
    from collections import defaultdict
    from nltk.util import ngrams
    # a subdefinition to get duplicate lists in a list
    def list_duplicates(seq):
        tally = defaultdict(list)
        for i,item in enumerate(seq):
            tally[item].append(i)
            # return to us the index and the ngram itself:
        return ((len(locs),key) for key,locs in tally.items() 
               if len(locs) > threshold)
    # get ngrams of gramsize    
    raw_grams = ngrams(text.split(), gramsize)
    # use our duplication detector to find duplicates
    dupes = list_duplicates(raw_grams)
    # return them, sorted by most frequent
    return sorted(dupes, reverse = True)

# <markdowncell>
# Now that it's defined, let's run it, looking for trigrams

# <codecell>
ngrammer(raw, 3)

# <markdowncell>
# Too many results? Let's set a higher threshold than the default.

# <codecell>
ngrammer(raw, 3, threshold = 10)

# <headingcell level=2>
# Concordancing with regular expressions

# <markdowncell>
# We've already done a bit of concordancing. In discourse-analytic research, concordancing is often used to perform thematic categorisation.

# <codecell>
text = nltk.Text(tokens)  # formats our tokens for concordancing
text.concordance("muslims")

# <markdowncell>
# We could even our stemmed corpus here:
text = nltk.Text(stemmed)
text.concordance("muslims")

# <markdowncell>
# You get no matches in the latter case, because all instances of *muslims* were stemmed to *muslim*.

# A problem with the NLTK concordancer is that it only works with individual tokens.

# What if we want to find words that end with **ment*, or words beginning with *poli**?

# We already searched text with Regular Expressions. It's not much more work to build regex functionality into our own concordancer.

# From running the code below, you can see that bracketting sections of our regex causes results to split into lists:

# <codecell>
# define a regex for different aussie words
aussie = r'(aussie|australia)'
searchpattern = re.compile(r"(.*)" + aussie + r"(.*)")
search = re.findall(searchpattern, raw)
search[:5]

# <markdowncell>
# Well, it's ugly, but it works. We can see five bracketted results, each containing three strings. The first and third strings are the left-context and right-context. The second of the three strings is the search term.

# These three sections are, with a bit of tweaking, the same as the output given by a concordancer.

# Let's go ahead and turn our regex seacher into a concordancer:

# <codecell>
def concordancer(text, regex):
    """Concordance using regular expressions"""
    import re
    # limit context to 30 characters max
    searchpattern = re.compile(r"(.{,30})(\b" + regex + r"\b)(.{,30})")
    # find all instances of our regex
    search = re.findall(searchpattern, raw)
    for result in search:
        #join each result with a tab, and print
        print("\t".join(result).expandtabs(20))
        # expand tabs helps align results

# <codecell>
concordancer(raw, r'aus.*?')

# <markdowncell>
# Great! With six lines of code, we've officially created a function that improves on the one provided by NLTK! And think how easy it would be to add more functionality: an argument dictating the size of the window (currently 30 characters), or printing line numbers beside matches, would be pretty easy to add, as well.

# > Adding too much functionality is known as *feature creep*. It's often best to keep your functions simple and more varied. An old adage in programming is to *make each program do one thing well*.

# <markdowncell>
# In the cells below, try concordancing a few things. Also try creating variables with concordance results, and then manipulate the lists. If you encounter problems with the way the concordancer runs, alter the function and redefine it. If you want, try implementing the window size variable!

# > **Tip:** If you wanted to get really creative, you could try stemming concordance or n-gram results!

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

# <headingcell level=2>
# Summary

# <markdowncell>
# That's the end of session three! Great work.

# So, some of these tasks are a little dry---seeing results as lists of words and scores isn't always a lot of fun. But ultimately, they're pretty important things to know if you want to avoid the 'black box approach', where you simply dump words into a machine and analyse what the machine spits out.

# Remember that almost every task in corpus linguistics/distance reading depends on how we segment our data into sentences, clauses, words, etc.

# Building a stemmer from scratch taught us how to use regular expressions, and their power. But, we also saw that they weren't perfect for the task. In later lessons, we'll use more advanced methods to normalise our data. 

# *See you tomorrow!*

# <headingcell level=1>
# Bibliography

# <markdowncell>
# <a id="firth"></a>
# Firth, J. (1957).  *A Synopsis of Linguistic Theory 1930-1955*. In: Studies in Linguistic Analysis, Philological Society, Oxford; reprinted in Palmer, F. (ed.) 1968 Selected Papers of J. R. Firth, Longman, Harlow.
#
# <a id="ref:hymes"></a>
# Hymes, D. (1972). On communicative competence. In J. Pride & J. Holmes (Eds.), Sociolinguistics (pp. 269-293). Harmondsworth: Penguin Books. Retrieved from [http://humanidades.uprrp.edu/smjeg/reserva/Estudios%20Hispanicos/espa3246/Prof%20Sunny%20Cabrera/ESPA%203246%20-%20On%20Communicative%20Competence%20p%2053-73.pdf](http://humanidades.uprrp.edu/smjeg/reserva/Estudios%20Hispanicos/espa3246/Prof%20Sunny%20Cabrera/ESPA%203246%20-%20On%20Communicative%20Competence%20p%2053-73.pdf)
#
# <a id="ref:widdowson"></a>
# Widdowson, H. G. (2000). On the limitations of linguistics applied. Applied Linguistics, 21(1), 3. Available at [http://applij.oxfordjournals.org/content/21/1/3.short](http://applij.oxfordjournals.org/content/21/1/3.short).

# <markdowncell>
