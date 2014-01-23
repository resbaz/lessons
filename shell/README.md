Shell teaching content
=======================

This directory contains the shell related content that I teach at Software Carpentry bootcamps. 

## Novice lessons

### 1. Files and directories 

(novice/01-filedir.md)  

* The file system is responsible for managing information on disk.
* Information is stored in files, which are stored in directories (folders).
* Directories can also store other directories, which forms a directory tree.
* `/` on its own is the root directory of the whole filesystem.
* A relative path specifies a location starting from the current location.
* An absolute path specifies a location from the root of the filesystem.
* Directory names in a path are separated with `/` on Unix, but `\` on Windows.
* '..' means "the directory above the current one"; '.' on its own means "the current directory".
* Most file names are something.extension; the extension isn't required, and doesn't 
  guarantee anything, but is normally used to indicate the type of data in the file.
* `cd` path changes the current working directory.
* `ls path` prints a listing of a specific file or directory; `ls` on its own lists the 
  current working directory.
* `pwd` prints the user's current working directory
* Most commands take options (flags) which begin with a '-'


### 2. Creating things 

(novice/02-create.md)  

* Unix documentation uses '^A' to mean "control-A".
* The shell does not have a trash bin: once something is deleted, it's really gone.
* `mkdir path` creates a new directory.
* `cp old new` copies a file.
* `mv old new` moves (renames) a file or directory.
* `rm path` removes (deletes) a file.
* `rmdir path` removes (deletes) an empty directory.


### 3. Pipes and filters 

(novice/03-pipefilter.md)  

* Use wildcards to match filenames.
* '*' is a wildcard pattern that matches zero or more characters in a pathname.
* '?' is a wildcard pattern that matches any single character.
* `command > file` redirects a command's output to a file.
* `first | second` is a pipeline: the output of the first command is used as the input to
  the second.
* The best way to use the shell is to use pipes to combine simple single-purpose programs 
  (filters).
* `cat` displays the contents of its inputs.
* `head` displays the first few lines of its input.
* `sort` sorts its inputs.
* `tail` displays the last few lines of its input.
* `wc` counts lines, words, and characters in its inputs.


### 4. Loops 

(novice/04-loop.md)  

* Use a for loop to repeat commands once for every thing in a list.
* Use `$name` to expand a variable (i.e., get its value).
* Do not use spaces, quotes, or wildcard characters such as '*' or '?' in filenames, as 
  it complicates variable expansion.
* Give files consistent names that are easy to match with wildcard patterns to make it 
  easy to select them for looping.
* Use the up-arrow key to scroll up through previous commands to edit and repeat them.
* Use `history` to display recent commands, and `!number` to repeat a command by number.


### 5. Shell scripts  

(novice/05-script.md)

* Save commands in files (usually called shell scripts) for re-use.
* Use `bash filename` to run saved commands.
* `$*` refers to all of a shell script's command-line parameters.
* `$1, $2, etc.,` refer to specified command-line parameters.
* Letting users decide what files to process is more flexible and more consistent with 
  built-in Unix commands.


### 6. Finding things

(novice/06-find.md)  

* Everything is stored as bytes, but the bytes in binary files do not represent characters.
* Use nested loops to run commands for every combination of two lists of things.
* Use `\` to break one logical line into several physical lines.
* Use parentheses `()` to keep things combined.
* Use `$(command)` to insert a command's output in place.
* `find` finds files with specific properties that match patterns.
* `grep` selects lines in files that match patterns.
* `man` command displays the manual page for a given command.
