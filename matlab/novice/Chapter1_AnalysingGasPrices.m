%% Chapter 01 - Analysing Gas Prices
% This is the first Chapter

%%
% We are studying gas prices acr, and need to analyze a data set. The data set 
% is stored in comma-separated values (CSV) format: each row holds information 
% for a single year, and the columns represent different countries. 
% The first few rows of our first file look like this:
%
% 
%  1 Average Annual Gasoline (Petrol) Retail Prices in Selected Countries [$US per gallon]										
% 2 Source: US Dept. of Energy										
% 3 http://www.eia.doe.gov/emeu/aer/txt/ptb1108.html										
% 4										
% 5 Year	Australia	Canada      France      Germany     Italy       Japan       Mexico      South Korea     UK      USA
% 6 1990                1.87        3.63        2.65        4.59        3.16        1.00        2.05            2.82	1.16
% 7 1991    1.96        1.92        3.45        2.90        4.50        3.46        1.30        2.49            3.01	1.14
% 8 1992    1.89        1.73        3.56        3.27        4.53        3.58        1.50        2.65            3.06	1.13
% 9 1993    1.73        1.57        3.41        3.07        3.68        4.16        1.56        2.88            2.84	1.11
% 
%
% We want to:
% 
% * load that data into memory,
% * calculate the average price in each country
% * plot the result.
% * To do all that, we'll have to learn a little bit about programming.
%

%% Objectives
%
% * Understand the Matlab GUI.
% * Load data from a csv-file into the program.
% * Assign values to variables.
% * Select individual values and subsections from data.
% * Perform operations on arrays of data.
% * Display simple graphs.

%% Matlab's graphical user interface
%  
% Using the default setup, the matlab desktop contains several important
% sections:
%
% * The Current Folder: The current folder is the directory that we are in
% at the moment. Since we normally don't want to save all our functions and
% files in one folder, we need to tell Matlab where to find our files. We
% point Matlab in the right direction by setting thep path to contain all
% folders that we want to work in. This is done in > Home > Set Path: 
% Include all folders and subfolders you want to be in the path. In
% "Current Folder", these folders should stop being transparent now. 
% * The Command Window: In the command window, we can run and debug our
% code. Everything that's typed into the command window is executed
% immediately. 
% * Workspace: The workspace contains all variable names and assigned
% values that we currently work with. As long as they pop up in the
% workspace, they are universally available, which is why it's good to keep
% it clean to not accidentally overwriting a variable of function that you 
% later use (can be cleaned up typing |clear all|).
% * Command History: The command history saves all commands you recently
% used. Double-clicking on one or a few will execute them again. They can
% also be exported directly into a script (right-click "Create script")
% * Search Documentation: On the top right of your screen, you can search
% for functions. Suggestions for functions that would do what you want to
% do will pop up. Clicking on them will open the documentation. 

%% Loading Data
% Words are useful, but what's more useful are the sentences and stories we use them to build. 
%
% In order to load our gas price data, we need to import it in a
% meaningful format that lets us work with it. 
% To do this, we need a function that reads in a file and converts it into
% a matrix. (Type "read file into matrix" in "Search Documentation". dlmread should pop up as a suggestion - click on that).
% We're using a function called dlmread. In the Matlab documentation centre, we can look
% at the syntax this function uses:
%
%%
% 
%  M = dlmread(filename)
% M = dlmread(filename, delimiter)
% M = dlmread(filename, delimiter, R, C)
% M = dlmread(filename, delimiter, range)
%
%  M = dlmread(filename) reads the ASCII-delimited numeric data file filename, and returns the data in output matrix M. The filename input is a string enclosed in single quotes. dlmread infers the delimiter from the formatting of the file.
% M = dlmread(filename, delimiter) reads data from the file, using the specified delimiter. Use '\t' to specify a tab delimiter.
% M = dlmread(filename, delimiter, R, C) reads data whose upper left corner is at row R and column C in the file. Values R and C are zero-based, so that R=0, C=0 specifies the first value in the file.
% M = dlmread(filename, delimiter, range) reads the range specified by range = [R1 C1 R2 C2] where (R1,C1) is the upper left corner of the data to read and (R2,C2) is the lower right corner. You can also specify the range using spreadsheet notation, such as range = 'A1..B7'.
%
%%
% When reading in our data, we want to be able to set a delimiter, and the
% number of rows that don't belong to the data, so we will be using
% |dlmread(filename, delimiter, R, C)|. Our function asks us for four
% different parameters: the filename, a delimiter - the character that
% separates our values, and the row and column of our first data value.
% Since we're dealing with a .csv(coma-seperated value) file, our delimiter
% is the comma. Our data starts in the 5th row and the 1st column:
dlmread('gasprices.csv',',',5, 0)
% Our call to |dlmread('gasprices.csv',',',5, 1)| read our file, and asigns 
% it to a variable called |ans|. |ans| always just contains the last value
% that we didn't explicitly assign to a variable. To prevent that and to be
% able to recall the array we just loaded later, we assign it to a
% variable, simply using |=|:
gasprices = dlmread('gasprices.csv',',',5, 0);
% A |;| at the end of the line supresses the output in the Command Window.
% We can now find our data in the Workspace. Double-clicking on the
% variablt name in the Workspace brings up our data for us to inspect. 
%
% We can also recall it typing:
gasprices
%
% The data we loaded is stored in an array. If we want to look at the
% value of row 5 and column 3, we can do this by typing:
gasprices(5,3)


%% Manipulating Data
% We can also change single or multiple values in an array:
gasprices(5,3) = 3.1;

%%
% _introduction of indexing in arrays, :, end, only work on or display a subsection of the array_
% _maybe convert all data into AUD_
% _compute the mean for each year, for each contry, and overall_ 


%% FIRST CHALLENGE  
% _load a file, do things to it_

%% Plotting 
% _introduce different plot types (one 2D, one 3D), subplots, hold on, figure properties and the 
% possibility to change things and then peek in the code what's happened._

%% SECOND CHALLENGE  
% _load a file, do things to it, plot it?_


%% Scripts, Comments
% We normally don't want to run our code just once, but might want to run
% it again some time in the future. This is what we can use scripts for. In
% our case, we can simply export the code we just wrote (highlight section 
% "Command History", right-click, "Create script"). 
% We save the script as an .m file, which is the Matlab specific file
% format and give it a meaningful name. 
% Our script does exactly the same thing as the Command Window, just not 
% instantly. Which means, from here, we can re-run the code, change it; but
% we can now also debug and publish it. We'll look at debugging in the next
% lesson. For now, let's look at how to create a nice report from the
% script we just wrote. 
% 
% If you look at your code in 2 months, you've most likely forgotton why
% you made certain decisions. 
% This is why naming conventions and comments are extremely important.
% (open myfirstscript.m or write some useful comments into the script you
% just created.)
%
% You can comment in different ways:
%
% * Use |%%| + space to split your code into meaningful cells. They don't have a
% functional use, but they keep code clear.
% * Use |%| to have comments in line with your code.
% * A comment right at the start of your script will pop up.
% * Clever usage of variable names. 
%
% Another neat feature that Matlab has to offer, is, that it let's you
% automatically create a report. 
% To do this, Matlab runs your script once, creates all images and combines
% everything into a nice document in your favourite format.
% Different comments will look differently in your report. 
% |%%|, for example, will create a new headline.
% The toolbar ("Publish") is great help if you want your report to look
% nice. (Now hit the publish button and watch the magic.)

%% Wrapping up
% _save variables, save plots (as .fig and .jpg), clc, close all, clear all_


%% THIRD CHALLENGE
% _create a script from the command history, comment, and hit the publish button_

%% Key Points

%% Next Steps
