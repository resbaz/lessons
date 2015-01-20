
# <headingcell level=1>
# Session 4: Advanced NLTK usage

# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <markdowncell>
# <br> **Welcome back!**

# So, what did we learn yesterday? A brief recap:

# * **IPython**: 
# * **Python**: syntax, variables, functions, 
# * **NLTK**:
# * **Corpus linguistic tasks**: tokenisation, keywords, collocation
# * **Fraser Speeches Corpus**: managing and exploring it

# Today's focus will be on **developing more advanced NLTK skills** and using these skills to **investigate the Fraser Speeches Corpus**. In the final session, we will discuss **how to use what you have learned here in your own research**.

# > Any questions or anything before we dive in?

# <headingcell level=2>
# Reloading the corpus

# <markdowncell>
# Yesterday, we loaded up the corpus. We need to do it again today.

# <codecell>
# LOAD CORPUS

# <headingcell level=2>
# Adding information to the corpus

# <markdowncell>
# So far, the kinds of tasks we've done have involved meaningfully reducing data into numbers, or words into stems, etc.

# At this point in the course, we begin to add additional data to the corpora. This allows us to 'go deeper' into the texts.

# Before we start annotating our own corpora, let's just quickly play with a pre-annotated corpus.

# > **Note:** John Sinclair, an early propoent of corpus linguistics generally, was famously resistent to the use of annotation and parsing. He felt that the corpus alone should be used to build theory, rather than using existing theories (grammars) to annotate data (e.g. [2004](#ref:sinclair)). Though this is an uncommon viewpoint today, it is still useful to remember that the process of value-adding is never free of theory or interpretation.

# <codecell>
# Load corpus...

# <headingcell level=2>
# Part-of-speech tagging

# <markdowncell>
# Part-of-speech (POS) tagging is the process of assigning each token a label. One of the well-known tagsets is the Brown Tagset, used to annotate the Brown Corpus in the 1960s.

# > **Note:** It is generally considered good practice to train your tagger by exposing it to well-annotated language of a similar variety. For reasons of scope, however, training taggers and parsers is not covered in these sessions.

# <headingcell level=2>
# Parsing

# <markdowncell>
# Parsing involves determining the underlying grammatical structure of a sentence. 

# There are many grammars available, and thus, many kinds of parsing.

# <headingcell level=3>
# Phrase structure grammar

# <markdowncell>

# Phrase structure grammar is the tree-style representation popularised by generative grammarians (i.e. [Chomsky 1965](#ref:chomsky)):

# <br>
# <img style="float:left" src="http://specgram.com/CLIII.d/syntax_tree.gif" />
# <br>

# <headingcell level=3>
# Dependency parsing

# <markdowncell>
# Dependency parsing is the process of assigning each word in a clause a governer and a dependent. The output looks like:

# <br>
# <img style="float:left" src="http://nlp.stanford.edu/software/stanford-dependencies/brownback_ccprocessed.png" />
# <br>

# > **Note:** Dependency grammars are often used to represent free-word-order languages, such as Russian, Latin or Farsi.

# <markdowncell>
# Now that we have dependency parsed data, we can calculate things that could not be calculated before (e.g. imperative, passive...)


# <headingcell level=2>
# Shell commands/IPython Magic

# <markdowncell>
# IPython has a very simple system for using shell commands. These may not work from your command line in the same way, but can be useful shortcuts at times.










# <headingcell level=2>
# Summary

# <markdowncell>
# So now we're able to do some pretty complex stuff!

# The ability to tag and parse our data, however, has many advantages. When we're generating lists of words, dividing them by word class makes a lot of sense. We can also understand the 'tone' of texts by counting the distributions of different word classes. 


# <headingcell level=1>
# Session 5: Charting change in Fraser's speeches

# <markdowncell>
# <br>

# <headingcell level=2>
# Data structure

# <markdowncell>
# Data structuring is key to distance reading/corpus linguistic/NLP research.

# Too often, people mix a bunch of words together and run queries over them. These 'bag of words' approaches help us learn about what a corpus contains, but do not exploit metadata...

# Programming allows us to automate tasks, so performing the same query on each subcorpus and tallying the results is not much more work than querying the dataset as a whole.

# Increasingly, data comes to us pre-structured in some way. Reasons for this include large digitisation efforts and 'born digital' data.

# We could divide Fraser's speeches in a number of ways, with each way making different kinds of insights possible:

# * **Structure by topic**: learn how key participants and processes are discursively constructed
# * **Structure by occupation**: learn how language changes when a person becomes/stops being PM
# * **Structure by speech date**: learn how language changes over the course of a career



# <headingcell level=2>
# Charting longitudinal change in Fraser's speeches

# <markdowncell>
# Now that we've broken Fraser's speeches into parts, we can interrogate each part in turn to look for longitudinal change.

# First, we'll interrogate each subcorpus to build a profile the way Fraser positions himself in relation to the reader, and the things he is talking about. To do this, we need a little bit of linguistics, however.

# <headingcell level=3>
# Some linguistics...

# <markdowncell>
# *Functional linguistics* is a research area concerned with how *realised language* (lexis and grammar) work to achieve meaningful social functions.

# One functional linguistic theory is *Systemic Functional Linguistics*, pioneered by Michael Halliday (Prof. Emeritus at University of Sydney).

# Central to the theory is a division between **intpersonal meanings** and **experiential meanings**.

# * Interpersonal meanings negotiate identities and role relationships between speakers 
# * Experiential meanings communicate what happened to whom, under what circumstances.

# Halliday argues that these two kinds of meaning are realised **simultaneously** through different parts of English grammar.

# * Interpersonal meanings are made through **mood choices**
# * Experiential meanings are made through **transitivity choices**.

# Mood features of a language include:

# * Mood type (*declarative, interrogative, imperative*)
# * Modality (*would, can, might*)
# * Lexical density---the number of words per clause, the number of content to non-content words, etc.

# Transitivity choices include fitting together configurations of:

# * Participants (*a man, green bikes*)
# * Processes (*sleep, has always been, is considering*)
# * Circumstances (*on the weekend*, *)

# > **Note**: SFL argues that through *grammatical metaphor*, one linguistic feature can stand in for another. *Would you please shut the door?* is an interrogative, but it functions as a command. *invitation* is a nominalisation of a process, *invite'. We don't have time to deal with these kinds of realisations, unfortunately.

# <headingcell level=3>
# Fraser's speeches and linguistic theory

# <markdowncell>
# So, from an SFL perspective, when Malcolm Fraser gives a speech, he is simultaneously making meaning about his role and identity (through mood choices) and about events in the real world (through transitivity choices).

# We can create two research questions.

# 1. **How does Malcom Fraser's tone change over time?**
# 2. **What are the major things being spoken about in Fraser's speeches, and how do they change?**

# As our corpus is well-structured and parsed, we can create functions to answer these questions. We will define each function before we run anything.

# <headingcell level=4>
# Interpersonal features

# <codecell>
# number of content words per clause
def lexical_density: 

# <codecell>
# percentage of tokens that are I/me
def firstperson_perc:

# <codecell>
# ratio of open/closed class words
def open_closed:

# <codecell>
# ratio of nouns/verbs
def noun_verb:


# <headingcell level=4>
# Experiential features

# <codecell>
# heads of noun phrases not in PPs
def top_participants:

# <codecell>
# most common predicators
def top_processes:


# <headingcell level=2>
# Running our functions over each subcorpus

# <codecell>
# for each subcorpus, 
# do function on subcopus
# store result in array.
# print array

# <headingcell level=2>
# Getting pretty results

# <markdowncell>
# So, we have our answers. Now we want to produce two kinds of output:

# 1. A table of numbers
# 2. A visualised representation of these

# <codecell>
# table generation

# <codecell>
# plotting our findings

# <headingcell level=2>
# Querying our subcorpora

# <markdowncell>
# A danger when working with very large linguistic datasets is that the researcher may never really read actual sentences as they appeared.

# We can combine quantitative and qualitative findings by modifying a function to also list example clauses from the text.

# <codecell>
def process_examples:
	# etc
	# etc

# <headingcell level=3>
# Groupwork!

# <markdowncell>
# With each group working on a subcorpus, we'll try to paint a more qualitative picture of how language changes. To do this, we want to find salient examples of real language use by Fraser.

# This will involve querying lexis and grammar at the same time, using regex where needed. You should be able to cannibalise some of the previous examples if need be.

# <headingcell level=4>
# Challenge 1: list Interrogative clauses

# <codecell>
# code here

# <headingcell level=4>
# Challenge 2: find what processes 'I' and 'we' most commonly do

# <codecell>
# code here

# <headingcell level=4>
# Challenge 3: find which participants 'should/must' do something

# <codecell>
# code here

# <headingcell level=1>
# Session 6: Getting the most out of what we've learned

# <markdowncell>
# <br>

# <markdowncell>
# So, now you know Python and NLTK! The main things we still have to do are:

# 1. Manage resources and results
# 2. Brainstorm some other uses for NLTK
# 3. Integrate IPython into your existing workflow
# 4. Summarise and say goodbye!

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

# 1. Most importantly, **write comments on your code**. You **will** forget what bits of code are supposed to do. Using others' code is much easier if it's commented up. A related point is to name your variables meaningfully: *variablexxy* does not tell us much about what it will contain.
# 2. **Version control**. When editing your code, you may sometimes break it. LINK TO DAMIEN'S STUFF
# 3. **Share your code**. You are often doing novel things when you code, and sharing what you've done can save somebody else a lot of work. *Github* is free for open-source projects. Github provides version control, which is especially useful when you are working with a team.

# <headingcell level=3>
# Your data

# <markdowncell>
# *Cloud computing*

# <headingcell level=3>
# Your findings

# <markdowncell>
# [*Figshare*](http://www.figshare.com) is a site for storing tables and figures. It's particularly useful for working with large datasets, as we often generate far more raw tables and statistics than we can possibly publish.

# It's becoming more and more common to link journal publications to additional online resources such as Github code or Figshares.

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
# * Download it: Wget, curl, crawlers ...
# * Extract relevant data and metadata: *Beautiful Soup*
# * **Structure your data**
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

# <headingcell level=3>
# Using IPython locally

# <markdowncell>
# You may also want to use IPython locally. To do this, you need to install it. There are many ways to install it, and these vary depending on your OS and what you already have installed. See the [IPython website](http://ipython.org/ipython-doc/2/install/install.html#installnotebook) for detailed instructions.

# Open up Terminal, navigate to the notebook directory and type:

# > **ipython notebook filename.ipynb**

# This will open up a blank notebook.

# <headingcell level=2>
# Summaries and goodbye

# <markdowncell>
# Before we go, we should summarise what we've learned. Add all this to your CV!

# * thing
# * thing
# * thing
# * thing
# * thing
# * thing
# * thing
# * thing
# * thing

# <headingcell level=2>
# Thanks!

# <markdowncell>
# That's the end of of course. Thank you to everybody for your participation.

# Please let us know how you found the course.

# <markdowncell>
# 

# <headingcell level=2>
# Solutions

# <headingcell level=2>
# Additional resources

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
# <markdowncell>
# 