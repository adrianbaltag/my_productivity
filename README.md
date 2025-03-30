
# My_productivity

This script contains 3 small scripts for enhancing the productivity: deleting certain files from your Desktop, based on choosen file extension, deletes the content of specified folder(s), and open specific urls in your browser, choosed by you.
Run each script, and modify it, based on your necessity.
    
   




## Features

- delete_desktop_files.py  # This script deletes ALL specified files extensions from Desktop
- folders_cleaning.py  # This script cleans the contents of specified folders on your Desktop.
- open_apps_google.py # Open a list of URLs in the default web browser with a delay between each one


## Dependencies

In order to be able to use this script, you will need to have installed Python 3.13 version

Here is the link for download(secured):
🐍 [Python.org](https://www.python.org/downloads/)

Also, please make sure when installing python, to "add it to PATH" while following the steps provided by the python installer

To check installation was succesful, in CMD Prompt run:

```bash
python --version
```

The above cmd should display the python version you just installed, meaning that ython was succesfully installed on your system


## Installation



```bash
  # from cmd -- choose Desktop path:
    cd Desktop
  # should be able to see
   C:\Users\your_username\Desktop>
  # clone the repo
  git clone https://github.com/adrianbaltag/my_productivity.git
```
    

## Usage

- double click "my_productivity" folder on your Desktop, and open it
- once inside, double click 'src" folder
- you should be able to see:

      1) delete_desktop_files.py
  
      2) folders_cleaning.py

      3) open_apps_google.py

      4) __init__ file !!! DO NOT TOUCH !!!

- right click on "delete_desktop_files.py" and choose "Open with Notepad"
- you will see the entire script, and at the bottom of it, should see "file_extensions"
- feel free to add / remove extensions there

#### NOTE:

Please make sure to keep the indentation seen, and not to modify anything else


- once you have added / removed file extensions customized to you, save the file, with "ctrl + s"

- BACK in the  Terminal, make sure you're still in "my_productivity" folder, also inside "src" folder

```bash
      # navigate to src folder
      cd src   
```

```bash  
      # once there, add the following cmd and "Enter"
      python delete_desktop_files.py
```

- this will run the specific script using the Terminal, and should be able to see the deleted files

- same procedure for "folders_cleaning", only exception, is that on the top of the script, you should see a "# todo - comment": under it, modify the"target_folder_list" with the name of your desktop folder(s) that you want to be cleaned

- for open_apps_google file: same procedure, and on the top of the script you should see "my_urls": there add / remove your urls respecting the format, and the indentation


#### Follow up command for Terminal:

```bash
# navigate to Desktop / folder my_productictivity path
cd desktop/my_productivity/src

# assuming you already modified each script according to your needs, run the choosed script
python delete_desktop_files.py
# or
python folders_cleaning.py
# or
python open_apps_google.py`
    
## FAQ

#### Do I need to have "uv - python packaging tool globally installed on my system?

No. This is a simple script, with just built-in libraries

#### Do I need a virtual environment to run this script ?

No. Since the script ONLY use built-in libraries, there is no need to.


#### Final note:

Enjoy!😉
    