###Drafting manuscript in LaTeX

When drafting a manuscript a mastery or at least basic knowledge of LaTeX would be beneficial. An overview of LaTeX 
can be found [here](http://www.latex-project.org/).

A cheatsheet on what works with regard to LaTeX in Authorea can be found [here](https://authorea.com/users/3/articles/6868/_show_article).

A basic help page can also be found here for [further reference.](https://authorea.com/help) 

Main editor layout and functionality
* Text editor
* Buttons top
* Buttons bottom

The manuscript can be divided up into blockss and each can be individually edited. Between each block, one could
add a figure (more in inserting figures [here](../06_Figures/insertingFigures.md)). One could think of blocks as
a chapter or a section in a manuscript.

Double clicking on a chunk invokes the text editor. 

![TextEditWindow](../images/EditSection.png)

You can give each block a unique name. 

To start editing type `i`, the cursor within the window will change from an orange box to a black line indicating
you can type into the editor.

There are a number of buttons on the top of the editor as well as ones along the bottom, these will be explaned from left to right. 

The buttons found on the top right of the editor are essentially shortcuts to LaTeX code for basic formatting functions. 

The `+` button is the insert citation function. This will be covered more the section on [adding citations](../07_Citations).

**B** button is to insert bold type into the editor. Clicking on this automatically inserts LaTex code for bold type into the
editor, `/textbf{}`.

***i*** button is to insert italic type into the editor, like for bold type above, clicking this button insert `/textit{}` into
the editor.

The next button `{}` is used to insert code snippets into your manuscript. 

The following two are for inserting lists into your block. These can be bullet points of numbered listes accordingly. Clicking
on either of these buttons sets up the LaTex environment for generating lists. 

For bullet points the following is inserted which is standard LaTeX code for inserting lists:
    /begin{itemise}
    /item
    /end{itemise}

The following buttons are used to insert a block quote code **"**, insert link and finally insert heading stye. 

The right hand most drop down menu on the top right of the editor allows you to select encoding, wheather it be
markdown (suffixed with `.md`) or LaTeX (We are convering LaTeX today).


**Challenge** Create a new block, give the block a name, insert bold type text and italic type text into the editor. Click on 
preview to see what happens. How would you make text both bold AND italic? (Hint: requires coding). Check to see you have done
this by previewing or saving and closing the text editor. 

More challenging tasks to follow including:
* [Writing equations and tables](../05_EquationsTables/insertingEquations.md)
* [Inserting figures and cross referencing](../06_Figures/insertingFigures.md)
* [Citations](../07_Citations/insertingCitations))

The tabs on the left hand side of document links to the guts of your Authorea document you just created. These tabs are relatively
self explantory (It is not usually necessary to directly mess with files in the folders tab). :
* Folders
* History
* Chat

![screenShotFolder](../images/EditSection.png))

The History tab, links to a record of the editing of the manuscript by yourself and your collaborators. 

Here, you can easily track changes and by which contributor working on the manusctipt(s). Simply clicking on the compare button
on the right hand side, it is easy to visualise the changes that have happened and made by whome. 

More information can be found [here](../08_collaborativeEditing/collaborating.md). 

The chat tab is self explantory, it's functionality of notifying the owner of the manusrcript or all collabortors can been facilitated 
with minor funding.

**Challenge** Edit a block within your document, preferably one that is shared with your neighbour. Click save and close then go into 
the history tab to ovserve the changes made on the document. 

[Next, we will learn about writing equations and tables](../05_EquationsTables/insertingEquations.md) and other things within this 
directory. 


