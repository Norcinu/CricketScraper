import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen
from player import Bowler 
from player import Batsman

site_address = "";
site_page = "";

scrape_type = sys.argv[1]

if scrape_type == "bowling":
    site_address = "http://stats.espncricinfo.com";
    site_page = "/ci/content/records/93276.html";
elif scrape_type == "batting":
    site_address = "http://stats.espncricinfo.com";
    site_page = "/ci/content/records/282910.html";
    
def get_categorys(section_url):
    print section_url
    html = urlopen(section_url)
    soup = BeautifulSoup(html, "lxml")
    print(soup.find_all("tr", "data1"))
    
