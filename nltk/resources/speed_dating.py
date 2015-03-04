# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Speed dating with Python and NLTK

# <markdowncell>
# <br>
# > Welcome to Python and the *IPython Notebook*! Today, we're demonstrating NLTK, a library for working with natural language.

# <headingcell level=1>
# Tell me a little about yourself

# <markdowncell>
# > Whatever your area of study, Python can speed up repetitive tasks and ensure that whatever you do can quickly be redone, by anyone.

# <headingcell level=1>
# What line of work are you in?

# <markdowncell>
# > The NLTK library of Python provides a powerful way of working with **language as data**.

# <codecell>
import nltk
from nltk.book import text4 as speeches
print speeches[:100]

# <headingcell level=1>
# What's so great about that?

# <markdowncell>
# > We can quickly harvest and visualise information from large bodies of text.

# <codecell>
from nltk.draw import dispersion_plot
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# <headingcell level=1>
# You probably say that to everyone!

# <markdowncell>
# > You can work with your own texts, too:

# <codecell>
sentence = "That's a lovely dress you're wearing."

# <codecell>
parsetree(sentence)

# <headingcell level=1>
# Let's talk politics ...

# <markdowncell>
# > We have been investigating a corpus of speeches made by Malcolm Fraser between 1951 and 1981. 

# > Every word has been annotated with its word class, and every clause has been annotated with grammatical structure information

# <codecell>
corpus = 'fraser-corpus-annotated'
modal_words = 'MD'

# <codecell>
modals = interrogator(corpus, '-t', modal_words)

# <codecell>
plotter('Modals in Fraser Speeches', modals.results, fract_of = modals.totals)

# <headingcell level=1>
# Call me, eh?

# <markdowncell>
# Sign up for free Python, IPython and NLTK lessons!

# <markdowncell>
# 














# <codecell>
% run corpling_tools/interrogator.ipy
% run corpling_tools/plotter.ipy
% run corpling_tools/additional_tools.ipy