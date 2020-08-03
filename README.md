# codeforces-automation--with-python
This script will help you to download your codeforces accepted codes to your local directory. It scrapes your submission page and copies all the accepted codes and writes them as a .cpp file. <br/>
Featues: <br/>
1. It doesn't require you to sign up so it's safe <br/>
2. Saves the file with proper name <br/>
HOW TO USE? <br/>
Step 1: Copy the full code and save it as a .py file <br/>
Step 2: Open it with any text editor <br/> 
Step 3: run these command one by one in a command propmt <br/>
pip3 install selenium <br/>
pip3 install beautifulsoup4 <br/>
pip3 install pyperclip <br/> 
Step 4: Change the username to your Codeforces handle/ username <br/>
username = 'your user name here' <br/>
Step 5: download Chrome driver from google and copy the path of chrome driver in your pc and replace this path here <br/>
driver = webdriver.Chrome('your path here') <br/>
eg: driver = webdriver.Chrome('C:/usr/chrome/chromedriver_win32 83.0/chromedriver') <br/>
Step 6: run the script and set back <br/>
Step 7: ENJOY! <br/>
<br/>
It saves the file as .cpp file if you code in java just find this line and change the file type from .cpp to .java <br/>
eg: file = open(fileName+" .cpp", "w+") to file = open(fileName+" .cpp", "w+") <br/>
You're good to go! 
