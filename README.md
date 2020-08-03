# codeforces-automation--with-python
This script will help you to download your codeforces accepted codes to your local directory. It scrapes your submission page and copies all the accepted codes and writes them as a .cpp file.
Featues: 
1. It doesn't require you to sign up so it's safe
2. Saves the file with proper name
HOW TO USE?
Step 1: Copy the full code and save it as a .py file
Step 2: Open it with any text editor
Step 3: run these command one by one in a command propmt 
pip3 install selenium
pip3 install beautifulsoup4
pip3 install pyperclip
Step 4: Change the username to your Codeforces handle/ username
username = 'your user name here'
Step 5: download Chrome driver from google and copy the path of chrome driver in your pc and replace this path here
driver = webdriver.Chrome('your path here')
eg: driver = webdriver.Chrome('C:/usr/chrome/chromedriver_win32 83.0/chromedriver')
Step 6: run the script and set back
Step 7: ENJOY!

It saves the file as .cpp file if you code in java just find this line and change the file type from .cpp to .java
eg: file = open(fileName+" .cpp", "w+") to file = open(fileName+" .cpp", "w+")
You're good to go! 
