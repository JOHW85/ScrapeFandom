import requests
from bs4 import BeautifulSoup
import argparse
from tqdm import tqdm
import errno, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise
def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'wb')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--no-sandbox')

parser = argparse.ArgumentParser()
parser.add_argument('input_fandom', help='Fandom\'s name')
args = parser.parse_args()
fandom_site = args.input_fandom
#Get All Pages
nextpage_url = "/wiki/Special:AllPages"
AllPage = "https://"+fandom_site+".fandom.com"+nextpage_url
counter = 0
while nextpage_url != "":
    listofpages = ""
    try:
        req = requests.get(AllPage, allow_redirects=False)
        if req.content != b'':
            soup = BeautifulSoup(req.content,"lxml")
            content = soup.find("div",{"class":"mw-allpages-body"})
            nextpage = soup.find("div",{"class":"mw-allpages-nav"})
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(AllPage)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content = soup.find("div",{"class":"mw-allpages-body"})
            nextpage = soup.find("div",{"class":"mw-allpages-nav"})
            driver.quit()            
        if content:
            listofentries = content.find_all("li")
            for i in tqdm(listofentries, desc="Scraping "+AllPage):
                listofpages += i.text.replace("(redirect","") + "\n"   
            # Exports XML file of all the pages scraped
            payload = {'catname':'','pages':listofpages,'curonly':'1','wpDownload':1,'wpEditToken':'+\\','title':'Special:Export'}    
            response = requests.post("https://"+fandom_site+".fandom.com/wiki/Special:Export", data=payload)
            data = response.content
            # Create directory 'fandom_site' if it doesn't exist
            with safe_open_w(f"{fandom_site}_raw/{counter}.xml") as f:
                f.write(data)
            counter += 1
        else:
            print("No content found")
        # Gets next page from AllPages
        if nextpage:
            nav = nextpage.findAll("a")
            if len(nav) > 0:
                if "Next page" in nav[-1].text:
                    nextpage_url = nav[-1]["href"]
                    AllPage = "https://"+fandom_site+".fandom.com"+nextpage_url
                else:
                    nextpage_url = ""
                    break
        else:
            # Break if there's only one index page on AllPages
            break
    except Exception as e:
        print("Error", e)
        continue
    
# Combine all the MediaWiki XML files into one
# Get all files in the directory
# Files in present working directory
files = os.listdir(f"{fandom_site}_raw")
# Create a new file to write to
with open(f"{fandom_site}.xml", "w") as outfile:
    # Loop through all files in the directory
    for fname in files:
        # Open each file and read it as a MediaWiki XML file
        with open(f"{fandom_site}_raw/{fname}", "r") as infile:
            # Write the contents of each file to the new file
            outfile.write(infile.read())
            outfile.write("\n")
