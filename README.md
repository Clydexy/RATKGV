# RATKGV
Used throughout the coronavirus era to quickly submit a negative RAT test result to the KGV School website

## How to Use
Open the python file and enter a parent username and password
Install Selenium using the command
`pip3 install selenium` on POSIX (Mac & Linux)
`pip install selenium` on Windows

To execute, run:
`python3 RATTest.py -C`
To check whether test has been checked already, run:
`python3 RATTest.py -I`
For help, run:
`python3 RATTest.py -H`

Replace `python3` with `python` to run on Windows

## How it Works
Uses the selenium library to access the internet
Logs into the web page, and then first checks to see whether the checkbox has already been checked, if not then selenium will register a click, then checks if the click has been registered by the site. 
