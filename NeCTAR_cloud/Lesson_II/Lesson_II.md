Lesson II A VM: up and running (45min)

<table>
 <tr>
 <td>Introduction to the Research Cloud: The session is going to be a high level introduction to the conceptual foundations, advantages, disadvantages, and the parts of the research cloud. If you understand these then you’ll be far less likely to be bitten in your journey to the cloud: and given the scale and low price of the research cloud you will, most likely, be making that journey.</td>
 </tr>
</table>


Assumption: Know how to get around a dashboard and the basic bits of the machine (lesson 1).

# The power of Checklists

In 2001 a critical-care specialist at Johns Hopkins Hospital designed a checklist to prevent line infections. 

[Show the checklist]

These steps have been known and taught for years. 

They then asked the nurses to observe the doctors for a month as they put lines into patients, and record how often they completed each step. In more than a third of patients, they skipped at least one of the steps.

They then asked the nurses stop the doctors whenever a step was skipped.

The ten-day line-infection rate went from eleven per cent to zero. 

This story inspired a company that I worked at to introduce a checklist for deploying software into production.

We would do it a pairs, one person playing the role of the nurse, the other performing the actual steps.

We had to sign in the date and our names, and each checklist was filed after a deployment.

Our rate of problems encountered during deployment fell to zero.

<table>
 <tr>
 <td>Further reading: http://www.newyorker.com/magazine/2007/12/10/the-checklist</td>
 </tr>
</table>


So I’ve created a checklist for launching a virtual machine.

# Walk through of a launch

First you are going to walk me through the process, and then you going to follow it yourselves.

[ Use the walk through to remind everyone what the key pair and the security group are. Also describe each field as you fill it in.

Once you hit the "Launch" button there might be a delay, as it can take quite some time to get the machine started.

So here you can discuss that image data is possibly being moved across the country. Also that the target data center is shared, and might be very busy: hence taking a long time to respond. Discuss noisy neighbours once again…

Once the machine is launched, point out the IP address.]

Every machine that is launched on the NeCTAR cloud is given an IP address. This is it’s location on the internet.

NeCTAR unfortunately only have a small pool of IP address to use.

So when you terminate your instance, the IP address is returned to the pool and allocated to the next machine that starts up. Much like the transient file system, it is not lost during reboots.

**Question 1**

**Answer: B**

But before you spin up your own instances, you need to create your key pairs and security groups. 

And we have checklists for these as well!

# Key Pairs

Remember the clay tablets that we broke in half so that I could repay your emissary?

Key pairs are modern analogs used to communicate securely.

**NB:** you can only download your keypair once! Don’t lose it!!

[Walk the students through the key pair checklist, describing each entry as you go.**]**

**Activity 1:** Get students to generate key pairs on their own.

Please hold up a red sticky note if you need help

and a green one once you are done.

# Security Groups

Now we’ll move onto security groups.

By default VM brought up can reach out to the world, but the world can’t reach in. The script in the launch box was reaching out...

Security Groups specify what network traffic is allowed..

Lets see if I can explain.

Network messages destined for a computer are broken up into packets. Once a packet reaches a computer how does it know which application the packet is destined for? 

What if each network packet also had an associated number indicating the destination application? Then the computer could sort them into different trays, for the applications to pick up and work with. 

So these numbers associated with a packet are named the port numbers. And well known applications tend to get well known port numbers. So web browsers use port 80, for example.

So a security group allows you to define the ports that packets from the outside world are allowed to reach your VM. Any packets with a different port number don’t even make it to your machine. The security group rules just throw them away.

Ok, lets look at the security group checklist.

[Walk the students through the security group checklist, describing each entry as you go. **CIDR: Classless Internet Domain Routing!]**

**Activity 2:** Now get them to create a security group 

Please hold up a red sticky note if you need help

and a green one once you are done.

**NB:** You can edit a security group at any time.  And the changes will immediately apply to all running virtual machines using that security group.

**NB:** This also means that if you share security groups amongst VM’s, you have to be careful: if you change rules for one server, you might inadvertently break another. 

**Question 2**

**Answer: E. **Yes, it’s true. NeCTAR can experience Network issues from time to time. 

# Launch your own instance

Get students to walk through the creation of an instance.

