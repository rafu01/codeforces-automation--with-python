from selenium import webdriver
from bs4 import BeautifulSoup
import pyperclip


# initialize
driver = webdriver.Chrome('C:/usr/chrome/chromedriver_win32 83.0/chromedriver')
username = 'rafu01'

# start
driver.get('https://codeforces.com/submissions/'+username)
pageno = 0
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")
for pages in soup.findAll('span', attrs={'class': 'page-index'}):
    ahr = pages.find('a')
    if(ahr != None):
        pageno = ahr.text

# generate accepted code submission id


def generateListAccepted():
    submission = []
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    for span in soup.find_all('span', attrs={'class': 'submissionVerdictWrapper'}):
        verdict = span.get('submissionverdict')
        if(verdict == 'OK'):
            sid = span.get('submissionid')
            # print(sid)
            submission.append(sid)
    return submission

# generate links of accepted submission


def generateSubmissionId(submission):
    sublinks = []
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    for a in soup.findAll('a', attrs={'class': 'view-source'}):
        sub = a.get('submissionid')
        if(sub in submission):
            link = a.get('href')
            sublinks.append(link)
    return sublinks

# to parse the name of the problem


def nameParser(submission):
    namelinks = []
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    for sub in submission:
        for row in soup.findAll('tr', attrs={'data-submission-id': sub}):
            for td in row.findAll('td'):
                for ah in td.findAll('a'):
                    if(ah != None):
                        mystr = ah.get('href')
                        if(mystr.find('/problem/') != -1):
                            namelinks.append(mystr)
    return namelinks

# get the round name from codeforces


def getRoundName():
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    try:
        continue_link = soup.find('th', attrs={'class': 'left'})
        return continue_link.text
    except:
        continue_link = 'could not generate name'
        return continue_link

# get the problem name from codeforces


def problemName():
    name = driver.find_element_by_class_name('title')
    return name.text


# main
pagenumber = 2
pageno = int(pageno)
while(pageno > 0):
    submission = generateListAccepted()
    sublinks = generateSubmissionId(submission)
    linkget = nameParser(submission)
    index = 0
    for link in sublinks:
        driver.get('https://codeforces.com'+link)
        driver.find_element_by_class_name('source-copier').click()
        code = pyperclip.paste()
        #     linkget = namePar(link)
        #     print(linkget)
        driver.get('https://codeforces.com'+linkget[index])
        fileName = getRoundName() + ' ' + problemName()

        if(fileName.find('?') != -1):
            fileName = fileName.replace('?', ' ')
        try:
            file = open(fileName+" .cpp", "w+")
            file.write(code)
            print('success')
        except:
            print('error parsing one file')
        index = index+1
    driver.get('https://codeforces.com/submissions/' +
               username+'/page/'+str(pagenumber))
    pageno = pageno-1
    pagenumber = pagenumber+1
file.close()
