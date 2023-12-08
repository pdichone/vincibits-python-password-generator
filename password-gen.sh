#!/bin/zsh
# or
##!/bin/bash
cd /Users/pdichone/Code/vincibits/automation/password-generator # make sure to add your own path. Use pwd to get the full path to your project
python3 main.py $1

# when this is run, it will change to the directory where we have our project
# and then run the python file, and $1 will retrieve the input from our user in the terminal
# To run this sh file, we do zsh password-gen.sh, and voila!

