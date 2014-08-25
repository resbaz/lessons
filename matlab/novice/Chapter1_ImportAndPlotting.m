%% Chapter 1 - Importing, Arrays, and Plotting
% This is the first Chapter

%%
% We are studying inflammation in patients who have been given a new treatment for arthritis, and need to analyze the first dozen data sets. The data sets 
% is stored in comma-separated values (CSV) format: each row holds information for a single patient, and the columns represent successive days. The first few rows of our first file look like this:
%
%  0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
% 0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
% 0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
% 0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
% 0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,1
% 
%
% We want to:
% 
% * load that data into memory,
% * calculate the average inflammation per day across all patients, and
% * plot the result.
%
% To do all that, we'll have to learn a little bit about programming.
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
dlmread('inflammation-01.csv',',',0, 0)

%%
% Our call to |dlmread('gasprices.csv',',',5, 1)| read our file, and asigns 
% it to a variable called |ans|. |ans| always just contains the last value
% that we didn't explicitly assign to a variable. To prevent that and to be
% able to recall the array we just loaded later, we assign it to a
% variable, simply using |=|:
inflammationData = dlmread('inflammation-01.csv',',',0, 0);

%%
% A |;| at the end of the line supresses the output in the Command Window.
% We can now find our data in the Workspace. Double-clicking on the
% variablt name in the Workspace brings up our data for us to inspect. 
%
% We can also recall it typing:
% 
%  inflammationData


%% Manipulating Data
% Now that our data is in memory, we can start doing things with it. First, let's ask what class of thing inflammationData refers to:

class(inflammationData)
size(inflammationData)

%%
% The output tells us that data currently refers to an array of doubles
% containing 60 rows and 40 columns.
%
% If we want to get a single value from the matrix, we must provide an index in round parentheses, just as we do in math:
disp('First value in data:'); disp(inflammationData(1,1));

disp('Middle value in data:'); disp(inflammationData(31,21));

inflammationData(5,3) = 2;

%%
% Programming languages like Fortran and MATLAB start counting at 1, because 
% that's what human beings have done for thousands of years. Languages 
% in the C family (including C++, Java, Perl, and Python) count from 0 
% because that's simpler for computers to do.
%
% An index like (31, 21) selects a single element of an array, but we can
% select whole sections as well. For example, we can select the first ten 
% days (columns) of values for the first four (rows) patients like this:
disp(inflammationData(1:4, 1:10));

%% 
% The slice 1:4 means, "Start at index 1 and go up to, including, 
% index 4.".
%
% We don't have to start slices at 1:
disp(inflammationData(5:10, 1:10));

%%
% and we don't have to take all the values in the slice. If we provide a 
% stride, Matlab takes values spaced that far apart:
disp(inflammationData(1:3:10, 1:2:10));

%% 
% Here, we have taken rows 1, 4, 7, and 10, and columns 1, 3, 5, 7, and 9.
%
% We can also look at only one row and all colums.
% If we just use ':' on its own, the slice includes everything in that dimension:
disp(inflammationData(5, :));

%%
% Or use the handy key word |end|, displaying 
disp(inflammationData(50:end, 30:end));

%% 
% With arrays, we can also perform common mathematical operations. 
% If we want to find the average inflammation for all patients (each row is one patient)
% we can just ask the array for its mean value in that dimension (row = dimension 1):
mean(inflammationData,1)

%% 
% If we want to find the average inflammation for all days we use dimension 2:
mean(inflammationData,2)

%%
% The overall mean for all patients and all days can be computed using the 
% mean twice:
mean(mean(inflammationData))

%% 
% |mean| is a function. If variables are nouns, functions are verbs: 
% they are what the thing in question knows how to do. 
%
% Matlab arrays have lots of useful methods:

disp('Maximum inflammation:'); disp(max(max(inflammationData)));
disp('Minimum inflammation:'); disp(min(min(inflammationData)));

%% FIRST CHALLENGE  
%
% A subsection of an array is called a slice. We can take slices of character strings as well:
element = 'oxygen';
disp('First three characters:'); disp(element(1:3));
disp('Last three characters:'); disp(element(4:6));

%%
% 
% # What is the value of element(1:4)? What about element(4:end)? Or element(:)? 
% # What is element(0)? 

%% Plotting 
% The mathematician Richard Hamming once said, "The purpose of computing is
% insight, not numbers," and the best way to develop insight is often to
% visualize data. Visualization deserves an entire lecture (or course) of
% its own, but we can explore a few plotting features of Matlab here. 
% First, let's create a plot will all the data. To do this, we create a new figure and then  
% display a three-dimensional surface plot using the |surf| command:

figure;
surf(inflammationData);

%%
% Let's say we want to look at the plot from a specific angle. 3D figures come with the option of
% setting a certain view direction:

view(2);

%%
% Anoher thing we might want to do is lable out axes and give our plot a title.
% We can do this using the commands |xlabel|, |ylabel|, and |title|.

xlabel('Time');
ylabel('Patient');
title('Inflammation data');

%%
% Blue regions in this plot are low values, while red shows high values. 
% As we can see, inflammation rises and falls over a 40-day period. 
% Let's take a look at the average inflammation over time:

ave_inflammation = mean(inflammationData,2);
figure;
plot(ave_inflammation);
title('Average inflammation');
xlabel('Days');

%%
% Here, we have put the average per day across all patients in the
% variable ave_inflammation, then asked pyplot to create and display
% a line graph of those values using the |plot| function.
% The result is roughly a linear rise and fall, which is suspicious:
% based on other studies, we expect a sharper rise and slower fall.
% Let's have a look at two other statistics, the maximum and minumum 
% inflammation per day. Instead of plotting these into two separate 
% figures, we now want to overlay both graphs in one figure.
% We can do this, by holding the plot until all graphs are plotted and
% releasing it again once we're done.

figure;
title('Inflammation per day');
hold on;
plot(max(inflammationData,2));
plot(min(inflammationData,2));
xlabel('Days');
legend('Maximum','Minimum');
hold off;

%%
% The maximum value rises and falls perfectly smoothly, while the minimum
% seems to be a step function. Neither result seems particularly likely,
% so either there's a mistake in our calculations or something is wrong with our data.

%% SECOND CHALLENGE  

%%
% # Why do all of our plots stop just short of the upper end of our graph? Why are the vertical lines in our plot of the minimum inflammation per day not vertical?
% # Create a plot showing the standard deviation of the inflammation data for each day across all patients using the |std| command.


%% Creating subplots

figure;
subplot(2, 1, 1);
plot(max(inflammationData,2));
title('Maximum inflammation');

subplot(2, 1, 2);
plot(min(inflammationData,2));
title('Minimum inflammation');

%% Challenge
% 
% # Modify the program to display the three plots on top of one another instead of side by side.

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


%% Key Points
% 
% * Import data into Matlab using |dlmread|
% * Use variable = value to assign a value to a variable in order to record it in memory.
% * Variables are created on demand whenever a value is assigned to them.
% * Use |disp| to display the value of something.
% * The expression size() gives the size of an array in a certain dimension.
% * Use array(row, column) to select a single element from an array.
% * Array indices start at 1.
% * All the indexing and slicing that works on arrays also works on strings.
% * Use |%| to add comments to programs.
% * Use |mean|, |max|, and |min| to calculate simple statistics.
% * Use |plot| and |surf| to create simple plots.
% * Annotate your plots using |xlabel|, |ylabel|, and |title|.
% * Use |hold on| (and |hold off|) to overlay different plots in one figure.
% * Use |subplot| to create different plots next to each other in one figure.
% * Use scripts to save your work for later.
% * Use the publishing option to create a report from your script.

%% Next Steps
%
% Our work so far has convinced us that something's wrong with our first data file. 
% We would like to check the other 11 the same way, but typing in the same commands 
% repeatedly is tedious and error-prone. Since computers don't get bored (that we know of),
% we should create a way to do a complete analysis with a single command, and then
% figure out how to repeat that step once for each file.
% These operations are the subjects of the next two lessons.
