#   Dev: Amor
#
#   Run in cmd:
#   
#   pip install beautifulsoup4

from urllib2 import urlopen
from bs4 import BeautifulSoup
#import datetime

class data:
    Us = ''
    Eu = ''
    Ch = ''
    Kr = ''
    Tw = ''

def getToken(data):
    url = 'https://wowtokenprices.com/'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
   
    aBox = soup.find_all('p', attrs={'class': 'money-text'})

    data.Us = aBox[0].text.strip() # North America
    data.Eu = aBox[1].text.strip() # Europe
    data.Ch = aBox[2].text.strip() # China
    data.Kr = aBox[3].text.strip() # Korean
    data.Tw = aBox[4].text.strip() # Taiwan
    
def showValues(data):
    print "US:", data.Us
    print "Eu:", data.Eu
    print "Ch:", data.Ch
    print "Kr:", data.Kr
    print "Tw:", data.Tw

def fancyValues(data):
    print '|    Us   |    Eu   |    Ch   |    Kr   |    Tw   |'
    print '|',data.Us,'|', data.Eu,'|', data.Ch,'|', data.Kr,'|', data.Tw,'|'

while (True):
    getToken(data)
    fancyValues(data)
