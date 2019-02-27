#   Dev: Amor
#
#   Requirements:
#   
#   pip install beautifulsoup4

from urllib.request import urlopen 

from bs4 import BeautifulSoup as bs4
#from datetime import datetime

class data:
    t = ''
    Us = ''
    Eu = ''
    Ch = ''
    Kr = ''
    Tw = ''

def getToken(data):
    url = 'https://wowtokenprices.com/'
    page = urlopen(url)
    soup = bs4(page, 'html.parser')
   
    aBox = soup.find_all('p', attrs={'class': 'money-text'})
    #data.t = str(datetime.datetime.now().time())
    data.Us = aBox[0].text.strip() # North America
    data.Eu = aBox[1].text.strip() # Europe
    data.Ch = aBox[2].text.strip() # China
    data.Kr = aBox[3].text.strip() # Korean
    data.Tw = aBox[4].text.strip() # Taiwan
    
def showValues(data):
    #print ('T :',data.t)
    print ("US:", data.Us)
    print ("Eu:", data.Eu)
    print ("Ch:", data.Ch)
    print ("Kr:", data.Kr)
    print ("Tw:", data.Tw)

def fancyValues(data):
    print ('|    T   |    Us   |    Eu   |    Ch   |    Kr   |    Tw   |')
    print ('|',data.t,'|',data.Us,'|', data.Eu,'|', data.Ch,'|', data.Kr,'|', data.Tw,'|')

while (True):
    try:
        print (data.t)
        getToken(data)
        showValues(data)
        #fancyValues(data)
    except:
        print ('Error')
