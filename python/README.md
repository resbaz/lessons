Python teaching content
=======================

It should be noted that the real goal of these lessons isn't to teach Python, but to teach the basic 
concepts that all programming depends on. We simply use Python in our lessons because:

1.  we have to use *something* for examples;
2.  it's free, well-documented, and runs almost everywhere;
3.  it has a large (and growing) user base among scientists; and
4.  experience shows that it's easier for novices to pick up than most other languages.

See [here](http://drclimate.wordpress.com/2013/06/11/picking-the-right-programming-language/) for a discussion
of how Python compares to the many other programming languages out there.

Each lesson is saved as a separate IPython notebook. To view these notebooks, you can 
either navigate to associated nbviewer page, 

[01-numpy.ipynb](http://nbviewer.ipython.org/7572409)  
[02-func.ipynb](http://nbviewer.ipython.org/7572464)  
[03-loop.ipynb](http://nbviewer.ipython.org/7572490)  
[04-cond.ipynb](http://nbviewer.ipython.org/7572504)  
[05-defensive.ipynb](http://nbviewer.ipython.org/7572521)  
[06-cmdline.ipynb](http://nbviewer.ipython.org/7572536)  


or clone my lessons repository,

    git clone https://github.com/resbaz/lessons.git

then navigate to the `python` directory and fire up the IPython notebook:

    cd lessons/python/swc-novice
    ipython notebook &


## Novice lessons

### 1. Introduction to Data Analysis

An introductory example of how to perform typical data analysis tasks in Python. 
(swc-novice/01-numpy.ipynb)

*Topics:* importing libraries/modules, calling functions/attributes (modules) or 
methods/members (classes), reading and storing data, variable assignment, indexing 
(including slice and stride), basic plotting, array operations
  
  
### 2. Creating Functions

Use functions to make code easier to re-use and easier to understand. 
(swc-novice/02-func.ipynb) 

*Topics:* defining functions, the call stack, doc strings, positional and keyword arguments 
  

### 3. Analysing Multiple Datasets

Use lists and arrays to store related values, and loops to repeat operations on them. 
(swc-novice/03-loop.ipynb)

*Topics:* loops, lists
  

### 4. Making Choices 

Have programs make choices based on the values they are manipulating. 
(swc-novice/04-cond.ipynb) 

*Topics:* RGB color schemes, tuples, conditional statements
  

### 5. Defensive programming

Know the how, why and when of testing your code (summarised 
[here](http://drclimate.wordpress.com/2013/10/10/testing-your-code/)) and programming 
defensively. (swc-novice/05-defensive.ipynb)

*Topics:* assertions, unit testing, test driven development
  

### 6. Command Line Programs

Write code that allows the user to specify options at the command line, so you don't have 
to manually edit your code every time you want to make a minor change. 
(swc-novice/06-cmdline.ipynb)

*Topics:* parsing the command line
  
