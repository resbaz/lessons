***Inserting math equations and tables into an Authorea document

Authorea accepts a range of latex formatting including math equations. These can be 
inserted into an Authorea document without the need for libraries.

Further information and a cheat sheet can be found [here](https://authorea.com/users/3/articles/6868/_show_article).

For tables, the standard tabular format in LaTeX is compatible with Authorea. 

Example code ```/begin{tabular}{clll}
			DNA methylation & 1 & 4 & 5\\
		/label{Table}
		/caption{This is a basic table}
            	/end{tabular} ```

**Challenge** Code for one of the most well known mathmatical formulas by Einstein, E =mc^2. Insert another
match equation of your choice.

Tables are bounded by their environment in q LaTeX document. Therefore a number of extra fields of information are required to 
be filled in the data file.

**Challenge** Create a table, give the table a `/label` and a `/caption`. You may need to seek outside information in LaTex
as to what these fields do. Cross reference your table to a reference within your manuscript and us `/ref{}` notation.
