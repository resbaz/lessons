## Using the shell on Windows

Everything in these tutorials works on Unix and its descendents, such as Linux and Mac OS X. Things are a bit 
different on Windows. A typical directory path on a Windows 7 machine might be `C:\Users\vlad`. The first 
part, `C:`, is a drive letter that identifies which disk we're talking about. This notation dates back to the 
days of floppy drives; today, different "drives" are usually different filesystems on the network.  

Instead of a forward slash, Windows uses a backslash to separate the names in a path. This causes headaches 
because Unix uses backslash for input of special characters. For example, if we want to put a space in a filename 
on Unix, we would write the filename as `my\ results.txt`. Please don't ever do this, though: if you put spaces, 
question marks, and other special characters in filenames on Unix, you can confuse the shell for reasons explained 
in the lessons.

Finally, Windows filenames and directory names are case insensitive: upper and lower case letters mean the same 
thing. This means that the path name `C:\Users\vlad` could be spelled `c:\users\VLAD`, `C:\Users\Vlad`, and so on. 
Some people argue that this is more natural: after all, "VLAD" in all upper case and "Vlad" spelled normally refer 
to the same person. However, it causes headaches for programmers, and can be difficult for people to understand if 
their first language doesn't use a cased alphabet.

#### For MSysGit (Git Bash) users

MSys is an environment for Windows offering a Unix-type shell. Since Git requires such an environment to run on Windows,
they are [packaged together](http://msysgit.github.io/) and named MSysGit.

MSysGit tries to make Windows paths look more like Unix paths by allowing us to use a forward slash instead of a 
backslash as a separator. It also allows us to refer to the C drive as `/c` instead of as `C:`. Paths are still case 
insensitive, though, which means that if you try to put files called `backup.txt` (in all lower case) and `Backup.txt` 
(with a capital 'B') into the same directory, the second will overwrite the first.

MSysGit also doesn't come with `man` (the command for showing the manual for a given program), although this tends not 
be be a problem since the `--help` flag does much the same thing in most cases.
