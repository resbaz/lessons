# Extension for Lesson 2

## For OS X (Apple)

### Connecting to your VM from a Mac

Ensure that your downloaded private key (the .pem file) is in a known folder.

Open up the terminal from your Applications -> Utilities menu

In the terminal change to the directory in which your private key is saved.

Protect it by running this command:

    chmod 600 KEYPAIR_NAME.pem

Find the name of the login/username USER from the nectar image catalog: [https://wiki.rc.nectar.org.au/wiki/Image_Catalog](https://wiki.rc.nectar.org.au/wiki/Image_Catalog)

You can now connect to it by running the command:

    ssh -i KEYPAIR_NAME.pem USER@IP

If you get asked "are you sure you want to continue connecting..." simply type yes.

### Transfer files between your Mac and your VM

#### To the VM:

    scp -i KEYPAIR_NAME.pem SOMEFILE USER@IP:~/DESTINATION_FOLDER

#### From the VM to your current directory on your desktop machine:

    scp -i KEYPAIR_NAME.pem USER@IP:~/SOURCE_FOLDER/SOMEFILE .

## For Windows

Download[ https://qriscloud.zendesk.com/hc/en-us/article_attachments/200235864/QRIScloud_Beginners_Guide__ZenDesk_version_.pdf](https://qriscloud.zendesk.com/hc/en-us/article_attachments/200235864/QRIScloud_Beginners_Guide__ZenDesk_version_.pdf)

And follow the instructions on page 14 and 15.

**But** in the text field "auto-login" username, use the name of the login/username USER from the nectar image catalog:

[https://wiki.rc.nectar.org.au/wiki/Image_Catalog](https://wiki.rc.nectar.org.au/wiki/Image_Catalog) 

# Useful links

[http://espaces.edu.au/vwrangler/nectar-topics](http://espaces.edu.au/vwrangler/nectar-topics)

