<table>
  <tr>
    <td>Introduction to the Research Cloud: The session is going to be a high level introduction to the conceptual foundations, advantages, disadvantages, and the parts of the research cloud. If you understand these then you’ll be far less likely to be bitten in your journey to the cloud: and given the scale and low price of the research cloud you will, most likely, be making that journey.</td>
  </tr>
</table>


"Roll up to the NeCTAR mystery tour!" 

I’m your tour guide ...

[First: Do a personal introduction. Who am I, and why am qualified to teach this course?]

# Why do you care about this?

Two researchers at the University of Melbourne, who shall remain nameless, needed to do some fairly complex statistical analysis. So out of their grant money they bought two powerful computers, at a cost of $10 000 per machine to run[ MatLab](http://au.mathworks.com/products/matlab/?nocookie=true) on. 

But on the first run, they found that the machines couldn’t work with their data sets. The machines were underpowered! They were forced to iteratively upgrade those machines, until finally, one was able to perform the required analysis. It had taken them 12 months from the date of purchase to get to this point.

If, instead of purchasing hardware, they had turned to the cloud, they would have been able to have had their initial machine running within minutes. 

If it was underpowered, they would have been able to upgrade it to a larger machine, again within a matter of minutes. They probably wouldn’t even have had to re-install the software.  

The really good news for researchers is that everyone with an AAF login can experience this game changer for themselves, at no cost: through the National eResearch Collaboration Tools And Resources (NeCTAR) project.

If NeCTAR had been around with their current funding model in place when those two researchers were setting up their project that’s $20 000 of grant money that could have been used elsewhere!

**Question 1:**

**Answer: E**

But before you go rushing to the NeCTAR cloud, there are some important gotchas that you have to understand. The cloud environment is a not the same as dedicated computer! 

What I hope to do is to give you enough information to get your own machines up and running on the NeCTAR cloud, and to explain the gotcha’s around this small area.

How I’m going to do this is, is to start with an overview the NeCTAR parts through a very high level drive through of the NeCTAR dashboard. Hence the NeCTAR mystery tour title.

Then we’ll launch and access a machine.

By the end of this session you should be able start up and manage your own machines on cloud. You’ll also know where to go for support when things turn to custard! 

# Log in to the dashboard

**Question:** Has anyone here logged into the NeCTAR dashboard before? 

Please hold up a Red sticky note if you have

[ Hoping for Greens here, as people who have logged on before might have exhausted their trial projects. It would be good to have another project hand that these people can move to]

**Question:** Does everyone here have AAF credentials?

Please hold up a Red sticky not if the answer is "No" 

and a Green one if the answer is "Yes".

[Hoping for Greens, as people without AAF credentials can’t log in to the dashboard

**A:** If you don’t please pair with someone who does…

]

The first time you log on to the NeCTAR dashboard, you get given a **free** trial project, with three-months worth of time if you run it to the maximum. 

But if you keep your machines on the cloud as small as possible, you can get up to six months before your trial project is suspended.

If you only use your small machines for short periods of time, and shut them down religiously after each run, you will find that your trial project should last far longer. 

Regardless of your path,  your trial project should give you the time to learn the NeCTAR cloud ropes!

**Question 2:** Get everyone to log into [https://dashboard.rc.nectar.org.au](https://dashboard.rc.nectar.org.au) using their AAF credentials.

Please hold up a Green sticky note once you are done!

And a Red one if you need help.

# Follow my leader

Now that everyone has logged in, we are going to play a game of "[follow my leader](http://www.thefreedictionary.com/follow-my-leader)".  As I have the big screen, I’m going to be the leader. So there!

What I’d like you all to do is to follow along in your browsers, trying to do what I do. If you have any problems, simply hold up a red sticky note, I’ll stop, and someone will come to help you.

And I’m going to be asking questions as we go long, just to see how well I’m doing!

Having logged in, you should all be at the home page of the dashboard.

**Question:** Does anyone have anything very different from what’s up on the screen in front of them?

Please hold up a Red sticky not if the answer is "Yes" 

and a green one if the answer is "No".

[Hoping for a lot of Greens here, as anything else is a problem!]

# Project drop down

At the top of the dashboard are two drop downs.

The one on the left shows the projects that you belong to.

In OpenStack parlance, a project is: 

"*A logical grouping of users within Compute; defines quotas and access to VM images*."

And every project has a project ID:

A "*User-defined alphanumeric string in Compute; the name of a project.* (NOTE:  http://docs.openstack.org/glossary/content/glossary.html#project-id )"

So a project is really just a way to set group people together and to set constraints on what operations they can do on the NeCTAR cloud.

But here’s the interesting thing: you can belong to one or more projects. That’s why a drop down is used. By using it you can toggle between the different projects that you belong to, and work collaboratively within the constraints of the currently active project.

To the left of the dashboard is a tabbed menu system giving access to the operations and resources bound to the project. Dependent on your project, and your rights within the project, the menu system will expand and contract as you switch between the projects. The project panes to the left control your access to the resources of the cloud.

[**Demonstrate:** Toggle between them to show changes in the menu system to the left of the page.]

As mentioned, everyone who logs into the NeCTAR cloud via the AAF gets a small time limited trial project. This project is prefaced by the words "pt" ([project trial](http://support.rc.nectar.org.au/docs/allocations)) and followed by a number. So mine is, for example, pt-30.

**NB:** If you have multiple projects, get into the habit of always looking at the entry shown in this drop down before you do anything major, simply to confirm that you are in the correct project. You wouldn’t believe the trouble I’ve got into by launching VM’s in the wrong project!

**Q:** Can all those people who have multiple projects make sure they have their personal project selected?

Please hold up a green sticky note if your project is prefaced with the character  "PT", and a red one if it’s not.

[We are hoping for Green to be shown: otherwise there’s a problem]

# Settings drop down

The drop down on the right is the settings drop down. It’s not exactly the most intuitive of drop downs IMHO.

If you select it, you’ll see that there are two options: "Settings" and “Help”.

### The Help Menu

**Activity:** Get everyone to select "help" on the settings drop down.

**Q:** What happens?

**A:** A new tab opens, taking you to the homepage of the NeCTAR support site. This page gives news on the latest updates to the cloud. 

**Activity:** Get everyone to click on the "Getting Started" link of the top bar of the support site.

A menu appears on the left! 


**Demonstrate:** This menu to the left of the support site matches the links in the top bar of the support site.

The support site has loads of useful documentation. It has how to get started guides, tutorials, knowledgebases and more importantly it has information showing you how to get support. It’s well worth exploring. But we are not going to do it now. You know where to go when you want to find some helpful documentation.

**Activity:** Get everyone to click on the "Get Help" link of the top bar of the support site.

**Activity:** Get everyone to click on the "Get Support" link in the resultant page.

This is the important page if you want to reach out and get help. There is documented a process that NeCTAR would like you follow when you reach out to get help.

* Check to see if NeCTAR is OK

* Check to see if anyone else has experienced your problem

* Finally, try to get help.

This process is there to try and save everyone time and effort on the NeCTAR side. We are getting a lot of cloud for free. If we can lessen the amount of work that NeCTAR’s staff do we can get more of the cloud to use. It seems fair to me.

Can everyone click on the cunningly disguised link labelled "submit your support email here".

Please don’t click send! What should happen is that some form of email client opens up with you just having to provide the required details…

**Question: 3**

**Answer: A**

**Activity:** Get everyone to click on the "Status" link of the top bar of the support site.

This link takes you to a new site. It’s a very useful site, as the front page gives the status of all the major NeCTAR parts. If you see anything other than a green tick mark on this page, you know that a service is down. That means some parts of the NeCTAR cloud might not work as you would want them to.

**Activity:** Get people to click around at the top of this site. 

In addition to the status, this site also shows several interesting graphs about the NeCTAR cloud. Click around and have a look at them. Admire the growth!

**Activity:** Get people to close the tab and return to the dashboard.

**Question:** Does anyone have anything very different from what’s up on the big screen in front of them?

Please hold up a red sticky not if the answer is "Yes" 

and a green one if the answer is "they are about the same".

### The Settings Menu

**Activity:** Get everyone to select "settings" on the settings drop down.

**Question:** Notice how the "Project" tabbed pane on the left side of the dashboard has been collapsed and a new “Settings” tabbed pane has been added below it? 

With "User Settings" as the currently selected tab?

The settings on the "User Settings" tab affect your dashboard interface. You can set your preferred language and the timezone you are in. 

These changes affect only you, as a user, but they do cover all projects! 

We can change the language to chinese (to see the effect).

For the purposes of the rest of this lecture, change your language and time settings to match mine. "British English (en-au)" and “Australia/Melbourne (UTC + 11:00) 

**Question:** Does anyone have anything very different from what’s up on the screen in front of them?

Please hold up a red sticky not if the answer is "Yes" 

and a green one if the answer is "they are about the same".

**Activity:** Select the "Reset Password" tab

We logged into the NeCTAR dashboard using the AAF. However, the AAF doesn’t work too well with command line applications. So here you generate a password to use with command line applications.

It’s a little beyond the scope of what we are going to be doing today, but know three things

1. This is where you generate a password to use with command line applications

2. This password will work across all projects 

3. If you want to reset the password, just generate a new one.

So that’s the Settings tab and its children. Site wide changes that work across all projects.

Here’s a usability oddity.

**Demonstrate:**

Click on the Project tab. See how the settings tab collapses, and the project tab opens up?

Click on the Settings tab. See how we’re back to where we started?

Click on the Project tab. Click on the Compute tab. See how it all collapses, but the Settings tab is still there?

Click on the Compute tab, to open it up. Now click on the Overview entry. Where’s the Settings tab?

**Answer:** All gone!

So remember: if you want to change things do with your personal details, such as language and password: the top right drop down with your name on it is the way to go!

**Question 4**

**Answer: D**

# Overview tab

**Question:** Does anyone have anything very different from what’s up on the screen in front of them?

Please hold up a red sticky not if the answer is "Yes" 

and a green one if the answer is "they are about the same".

The overview tab simply gives an overview of your projects usage of its allocated resources. When a pie chart is full, your project has exceeded its quota for that resource type. 

**Demonstrate:** by swapping through projects

They are colour coded, so problems should stand out.

The project overview tab is your default home page when you log in. So these limits are put fairly and squarely in front of your face.

# Project Tab

Going back to the project tab:

You should be able to see that it’s essentially a menu system made out of nested tabs.

The top level tabs within on your personal project should be

* Compute

* Object Store

* Orchestration

* Allocations

Just click around on these tabs and their children seeing how they expand and contract, and how the screens change according which tab is selected. They only change when the leaf tabs are selected.

* The Compute tab is where you manage all of your computer resources.

* **Concept alert:** The Object Store is an ideal replacement for the usb sticks that some people tend to carry around with them: any file that you give it is backed up in at least triplicate, and the copies are monitored for degradation. Any bitrot, and the faulty file is replaced with a good one. You can upload and download files via your browser: and you can share them with the world. Some people have published whole websites from the object store!

* Orchestration is quite advanced: it’s to do with automating your cloud infrastructure. It allows you to repeatedly and reliably build up and tear down your machines. 
Save exploring this tab until you know your way around the NeCTAR cloud!

* Allocations is an important tab: Once you’ve messed around in your personal project, and found that it’s not big enough for serious work, this is where you come. It’s basically an online form that allows you to apply for a proper project with enough resources to support your research. 

Remember, Compute and the Object Store are two separate items: one is where you manage your computers, the other is a data store. They are not linked in any way, and can be run without the other.

## Project -> Object Store -> Containers Tab

**Question:** Is everyone on the same tab as me?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

As you can see, you create containers, and then put "objects" (or as I like to call them, “files”) into the containers.

It is a very simple interface, possibly a bit clunky. 

And the way that you share with the public, is to mark the container as being "public". If you click on the resultant “public” link you get some well formed xml. Just take the name of the object and append it to the url in the title bar to make a public handle that you can share with the world.

Ok: we’re going to abandon the "follow my leader" game for a moment, and do a challenge.

## Activity 1:

Please hold up a red sticky note if you need help

and a green one once you are done.

## Project -> Compute -> Images Tab

Ok. Back to the "Follow my leader game" If you could all join me on the Images subtab of the project tab.

**Question:** Is everyone on the same tab as me?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

**Concept alert:** What we have here are essentially files that are copies of hard drive contents.

How the NeCTAR cloud works is that you select a file that is a copy of the contents of a hard drive when you launch your machine. That file is copied across to wherever your machine is going to be launched and then it becomes the basis of your new machines hard drive.


This architecture has huge advantages: you can create and share these images easily with lots of people, you can quickly spin up identical copies of the same machine.

But it also has drawbacks, which we’ll get to.

Across the top of the list of images are four filters that are reasonably self explanatory.

1. Project - the images that are visible only to your project. 

2. NeCTAR official - the images that NeCTAR share with the world. These are simply images of operating systems. Whilst on this list NeCTAR is keeping them current. 

3. Shared with me - the images that other users have opted to share with you

4. Public - the list of images that others have shared with the world. This mostly already have applications installed on them, ready to run.

BTW, a ‘Snapshot’ is an image. But its one that has been created on the NeCTAR cloud by simply copying the disk of a running machine.

As new users to the NeCTAR cloud it is unlikely that you’ll have either project or shared images. Those come with time. 

So the image you’ll start your adventure on the NeCTAR cloud with is most likely to be a NeCTAR one.

**Question:** So here’s a thought experiment: you fire up a machine that uses a NeCTAR image as it’s base. NeCTAR then release a new copy of the image with a security update applied. Remember, your machine is based on a copy of that older image. Is it likely to have that update applied to it as well?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

[**A:** No. the only way to benefit from that update is to start up a new machine based on that new copy that NeCTAR have provided. So you have to either do a lot of maintenance on your running machine, or start from scratch on a regular basis.]

One common way of working is to start up a machine based on a NeCTAR image, then to install your own software onto it, and then to make a copy of its hard drive as it runs. This process is called "snapshotting". 

This saves you from having to reinstall the software next time you launch a machine. 

**Q:** Again, if you build your own image like this will it benefit from NeCTAR’s updates to the original file you copied?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

[**A:** No, the files are not linked in any way. (NOTE:  Once you make snapshot, you need to update it regularly and re-save it. Otherwise it just won’t get all the security upgrades that are released for the software on it. Also, its a good habit to immediately update all the software on a newly created machine. You can never be too paranoid!) ]

**Q:** And lets be paranoid: if you launch a machine based on a public image, and the software on it asks for your credit card info, do you type it in?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

[**A:** I wouldn’t. At least, without a lot of digging. You can’t trust the software on an image unless you know and trust the people behind the image. ]

## Project -> Access & Security Tab

The next tab we are going to explore is the Access and Security tab. 

This page has three tabs across the top.

### **Project -> Access & Security Tab -> Security Groups**

By default a machine brought up can reach out to the world via the network, but the world can’t reach in. 

Security Groups simply allow you to specify what network traffic is allowed in.

**Project -> Access & Security Tab -> Key Pairs**

Ok way back when, in the olden days, if I borrowed a lot of money from you and then relocated to a remote city, how would I know that the man in front of me claiming to be your emissary, now here to collect your cash for you, was the correct person?

And the answer used by some was ingenious. We’d break a clay seal in half. I’d take half, you’d keep half. Your emissary would hand me the half of the seal that you’d given me and if it matched mine I’d hand the cash over. Obviously there is quite a lot of trust in the system. And you’d want to keep your half of the seal private: under lock and key. Me? Meh, not so much.


Keys are a very similar concept. They have two halves. Anything you encrypt with one half can be decrypted by anyone with the other half.

On this tab you create key pairs. NeCTAR will keep one, the public key, and you will download the private key, the other half, to your local machine.

 When NeCTAR fire up a machine for you, they inject the public key into your machine. Anyone with the private key will be able to communicate and control that machine. Like the clay seals of yesteryear, you want to keep your private key in a secure location. 

**Q:** You fire up your machine. Days later, you realise that you’ve lost your private key. Will you ever be able to communicate and control your machine from that point onward?

Please hold up a red sticky note if the answer is "No" 

and a green one if the answer is "Yes".

[**A:** No, you’ve lost your machine for good.]

**Project -> Access & Security Tab -> API Access**

NeCTAR infrastructure can be communicated with by more than just the browsers we’re using at the moment. You can write or use other programs to manage your cloud resources. There is also a suite of command line tool that you can use instead of the dashboard.

This tab simply gives you all the information you’ll need if you are going to use those tools.

**Question: 5**

**Answer: C**

## Project -> Instances Tab

This is simply the place where you get to see the information about all your running machines.

Lets just walk through what’s going to happen when you launch a machine.

The file that you’ve chosen to be the basis of your hard drive is copied from where it is being stored to the physical machine which is going to host your machine. 

And I say "host" because the machine you are launching is ordinarily going to be a “virtual machine”. 

A virtual machine is one that is simply software and hardware working in concert to emulate a real machine. You can think of it as being a program pretending to be a computer. Much like your desktop computer can run many applications at the same time, such as ms-word, and excel, etc, a NeCTAR server can run many virtual machines at the same time.

The advantages of emulation, or virtualization as its properly called are many. But it does have a downside.

If you think about it, having all those virtual machines sharing one physical machine means that your application running on one of those virtual machines may well be impacted by what's happening in the other virtual machines – especially with regard to input and output. Because you are all sharing the same narrow pipes to the world beyond the CPU.

I love the term used to describe this effect: "Noisy neighbours".

So here’s a question. You have a virtual machine running. It makes all kinds of changes to its hard drives. Which are simply files on the host server. What happens to those changes when you shut your virtual computer down?

**Question 6:**

**Answer D:** The image is simply wiped.

So your virtual machine has what is termed "ephemeral" drives. Anything written to these drives will be lost if it’s associated virtual machine is terminated.

Rebooting or restarting its associated virtual machine does not cause the ephemeral data to vanish. But if you terminate it, then, whatever you wrote to this ephemeral storage will be lost the minute your virtual machine exits. All upgrades, security patches, whatever data you wrote, all will be lost.

This is one of the reasons why people like snapshot images so much. You work with your machine a little, you make a snapshot. The next time you start up from the snapshot, work with it, snapshot it when you are done.

This only works for small machines. It’s not the worlds greatest way of doing things, but it works for small machines.

I've seen ephemeral storage take so many people by surprise when they first start using the NeCTAR cloud. Don’t be one of those!

**Question 7**

**Answer: B**

