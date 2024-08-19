# ffmpeg Utils

> package name: *ffmpeg_utils*

Some useful line commands for ffmpeg queries and other utils.

# Requirements
Requires `ffmpeg` to be installed and to be ready to use in every terminal by typing "ffmpeg".

# Download
Recommended install is by executing install files respectively .bat for windows and ??? for linux. 

This will install this package and dependencies in a virtual environment. Then all commands will be put in Commands folder that will automaticly added to path variable. In this way commands will always loaded on terminal. All this is done in the scrypt `post_install.py`. 

If you only want to install the package, just use this command inside the package folder: 
``` 
pip install -e .
```

## Windows
Just double click on `setup.bat` file. If you want to uninstall just double click on `uninstall.bat` file. Easy peasy.

## Linux
work in progress


# Commands:
|command|description|
|-|-|
|`ffmpeg_utils`|shows all commands of this package|
|`ffmp4`|allows to use an ffmpeg query for all files mp4 in a folder and also changes modification date of new files (useful if for example we are compressing some old files to save space, and we would like to keep the date from the old file)|
|`date_transfer`|transfer modification date from a file to another|
|`date_set`|allows to change modification date of a file|