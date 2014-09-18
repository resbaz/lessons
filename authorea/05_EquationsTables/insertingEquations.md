### Inserting equations and tables.

Authorea accepts a range of LaTeX formatting including math equations. These can be 
inserted into an Authorea document without the need for libraries (further information can
be found in the [cheatsheet](https://authorea.com/users/3/articles/6868/_show_article)).

For tables, the standard tabular format in LaTeX is compatible with Authorea. 

    /begin{tabular}{clll}
    DNA methylation & 1 & 4 & 5\\
    /label{Table}
    /caption{This is a basic table}
    /end{tabular}


##### Challenge 1  
Insert Einstein's famous equation, E =mc^2, into your document, along with another equation of your choice.

##### Challenge 2 

Create a table and give it a `/label` and a `/caption`. You may need to seek outside information about LaTeX to find out how
these fields work. Cross reference your table to a reference within your manuscript using the `/ref{}` notation.

----  
Next we'll learn how to [insert figures](../06_Figures/insertingFigures.md).
