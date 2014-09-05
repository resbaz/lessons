## What is remote computing?

We're all familiar with doing data analysis on our own laptop or desktop computer, usally after hours of messing around to get the relevant software installed (e.g. Python, Matlab, R). These days, however, more and more researchers are doing their data analysis on remote computers. In other words, they simply use their own computer to access (via a network, such as the internet) a computer that is located somewhere else. This remote computing is typically labelled as either *supercomputing* or *cloud computing*.

In the case of supercomputing, the remote machine in question is a very large, very powerful computer such as [Raijin](http://nci.org.au/nci-systems/national-facility/peak-system/raijin/) at the National Computational Infrastructure in Canberra. Hundreds of researchers around Australia conduct their research and data analysis on Raijin every day. 

In the case of cloud computing, the remote machine isn't a single, large, powerful computer, but instead a collection of many regular machines. In fact, the remote computers in cloud computing are typically no better or more advanced than your personal laptop. Here the advantage is not the power of any single computer, but the fact that there are so many of them. By way of analogy, think of supercomputing as a single Formula 1 car and cloud computing as an entire fleet of Holden Commadores. 


## Why are we using the cloud at this bootcamp?

The cloud is a useful tool for Software Carpentry bootcamps because (a) at regular bootcamps a lot of time is wasted dealing with software installation issues, and (b) tools like the UNIX Shell look and behave slightly differently depending on which operating system you're using (i.e. Windows, Mac OS X or Linux), which can be confusing for beginners. By using the cloud we can setup a bunch of computers with exactly the same operating system and with the software already installed.    


### "DIT4C" on the NeCTAR Reasearch Cloud 

The [Research Bazaar](http://resbaz.tumblr.com/about) project is funding an initiative called Data Intensive Tools for the Cloud (DIT4C), which aims to get researchers using the [NeCTAR Research Cloud](http://www.nectar.org.au/research-cloud). Any researcher at an Australian university can apply for access to the NeCTAR Research Cloud, however for the purposes of this bootcamp we'll be using an DIT4C interface designed specifically for Software Carpentry activies. To access the enviroment, head to this URL:

https://dit4c.metadata.net/


#### Notes on the DIT4C cloud environment:

* The DIT4C environment comes with Vim and Nano for text editing at the command line, but no text editor like Notepad++, Kate or TextWrangler
* On a Mac, `command``+` doesn't work for zooming in the shell environment. Instead, hold down `control` and scroll with the mouse


## Should I be using the cloud in my actual research?  

If your research involves a computationally expensive data processing task that would take many days/weeks/months to run on your personal computer, then parallel computing in the cloud might be an option. To read more about using the cloud to speed up your code, read [this blog post](http://drclimate.wordpress.com/2014/08/28/speeding-up-your-code/).

Applying for an account on the NeCTAR Research Cloud might also be useful as a way of getting a "new" computer, without actually having to purchase a physical computer (which is expensive, inconvenient, etc). For instance:

* If you need a Linux machine to run a some software a colleague sent you, but your personal computer runs Windows, you can simply apply for access to a Linux machine on the cloud. 
* If Matlab or Python keeps crashing because the data array you're trying to analyse exceeds the 4GB of RAM on your laptop, apply for a computer in the cloud with 16GB of RAM.

In other words, the cloud is a great way to get access to a computer (or 3 or 30) to play around with, without having to go to the effort and expense of actually buying one.

If you're going to be doing a lot of remote computing as part of your research (supercomputing or cloud), Software Carpentry also has a couple of useful lessons:
* [Working remotely](http://www.software-carpentry.org/v5/novice/extras/06-ssh.html)
* [SSH keys](http://www.software-carpentry.org/v5/novice/git/05-sshkeys.html)


