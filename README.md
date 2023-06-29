# an Emacs org-clock widget for waybar

This repository provides a Python script that checks if, in your current Emacs session, an org-mode task is currently clocked in. If so, it checks its effort estimate (if there is one), duration and task name and displays them.

**Note:** This script requires [jlumpes python-emacs package](https://github.com/jlumpe/python-emacs) to be installed! It will *not* be installed along with this script!

## Installation
Just put the file 'info-emacs-org-clock.py' where you store your waybar scripts (remember to make it executable) and add what's in 'info-emacs-org-clock.json' to your waybar configuration (remember to adjust the '"exec"' option to where the script file is). If you want to customize the look, you find an example in 'info-emacs-org-clock.css'.

## Usage
Easy: Just add the 'custom/emacs-org-clock' widget to your other widgets!

   ***

*Note:* I *might* extend this Readme with screenshots or examples in the future.
