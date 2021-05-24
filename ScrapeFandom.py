import requests
from bs4 import BeautifulSoup

fandom_site = "finalfantasy"
#Get All Pages
nextpage_url = "/wiki/Special:AllPages"
AllPage = "https://"+fandom_site+".fandom.com"+nextpage_url
listofpages = ""
while nextpage_url != "":
    print(AllPage)
    req = requests.get(AllPage)
    soup = BeautifulSoup(req.content,"lxml")
    content = soup.find("div",{"class":"mw-allpages-body"})
    nextpage = soup.find("div",{"class":"mw-allpages-nav"})
    listofentries = content.find_all("li")
    for i in listofentries:
        listofpages += i.text.replace("(redirect","") + "\n"    
    # Gets next page from AllPages
    if nextpage is not None:
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
    
# Exports XML file of all the pages scraped
payload = {'catname':'','pages':listofpages,'curonly':'1','wpDownload':1,'wpEditToken':'+\\','title':'Special:Export'}    
response = requests.post("https://"+fandom_site+".fandom.com/wiki/Special:Export", data=payload)
data = response.content
with open(fandom_site+'.xml', 'wb') as s:
    s.write(data)
