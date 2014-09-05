## What is remote computing?

We're all familiar with doing data analysis on our own laptop or desktop computer, usally after hours of messing around in order to get the relevant software installed (e.g. Python, Matlab, R). These days, however, more and more researchers are doing their data analysis on remote computers. In other words, they simply use their own computer to access (via a network, such as the internet) a computer that is located somewhere else. This remote computing is typically labelled as either *supercomputing* or *cloud computing*.

### Supercomputing

In the case of supercomputing, the remote machine in question is a very large, very powerful computer such as [Raijin](http://nci.org.au/nci-systems/national-facility/peak-system/raijin/) at the National Computational Infrastructure in Canberra. Hundreds of researchers around Australia conduct their research and data analysis on Raijin every day. 

### Cloud computing

In the case of cloud computing, the remote machine isn't a single, large, powerful computer, but instead a collection of many regular machines. In fact, the remote computers in cloud computing are typically no better or more advanced than your personal laptop. Here the advantage is not the power of any single computer, but the fact that there are so many of them. By way of analogy, think of supercomputing as a single Formula 1 car and cloud computing as an entire fleet of Holden Commadores. 


## Why are we using the cloud at this bootcamp?

The cloud is a useful tool for Software Carpentry bootcamps because (a) at regular bootcamps a lot of time is wasted dealing with software installation issues, and (b) tools like the UNIX Shell look and behave slightly differently depending on which operating system you're using (i.e. Windows, Mac OS X or Linux), which can be confusing for beginners. By using the cloud we can setup a bunch of computers with exactly the same operating system and with the software already installed.    


### "DIT4C" on the NeCTAR Reasearch Cloud 

The [Research Bazaar](http://resbaz.tumblr.com/about) project is funding an initiative called Data Intensive Tools for the Cloud (DIT4C), which aims to get researchers using the [NeCTAR Research Cloud](http://www.nectar.org.au/research-cloud). Any researcher at an Australian university can apply for access to the NeCTAR Research Cloud, however for the purposes of this bootcamp we'll be using an DIT4C interface designed specifically for Software Carpentry activies. To access the enviroment, head the this URL:

https://dit4c.metadata.net/


#### Teaching notes:

* The DIT4C environment comes with Vim and Nano for text editing at the command line, but no text editor like Notepad++, Kate or TextWrangler.
* On a Mac, `command``+` doesn't work for zooming in the shell environment. Instead, hold down `control` and scroll with the mouse


## Should I be using the cloud in my actual research?  

but for their future work it's all about being aware that the cloud is the way to 'get' a new/different computer without actually purchasing hardware (which is expensive, inconvenient, etc)...

If you need a linux machine to run some software but your personal 
machine is Windows, no problem - get a linux machine on the cloud. 

If you need a machine with more RAM, no problem, try one out on the cloud
If you want to run a simulation across multiple machines, no problem, get a whole bunch of machines on the cloud


