from http.client import HTTPSConnection
from base64 import b64encode
import os, urllib
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('USERNAME')
USERPASS = os.getenv('USERPASS')

# Authorization token: we need to base 64 encode it 
# and then decode it to acsii as python 3 stores it as a byte string
def basic_auth(USERNAME, USERPASS):
    token = b64encode(f"{USERNAME}:{USERPASS}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

#This creates the URL to add
URL = ("https://wilderreport.substack.com/p/the-prairies-frozen-angel")
TITLE = ("The Prairie's Frozen Angel: Hazel Miner's Sacrifice Echoes through Eternity")
SELECTION = ("This article was originally told by my friend The Way I Heard It: . Not many outside of North Dakota know this incredible true story. Hazel's story needs telling, and go follow. The Way I Heard It: The prairie wind howls like a famished beast, ripping across the plains with teeth of ice. In this land of stark beauty and brutal winters, survival is a knife's edge, a dance with death where the weak wither and the strong endure. But even the harshest landscapes can't extinguish the flames of courage that flicker in the human heart. Enter Hazel Miner, a fifteen-year-old girl whose story is etched in ice and blood, a testament to the raw, untamed power of love.")

params = urllib.parse.urlencode(({"url": URL, "title": TITLE,"selection": SELECTION}))

#This sets up the https connection
c = HTTPSConnection("www.instapaper.com")
#then connect
headers = { 'Authorization' : basic_auth(USERNAME, USERPASS) }
c.request("POST", "api/add", params, headers)
#get the response back
res = c.getresponse()
# at this point you could check the status etc
# this gets the page text
data = res.read()
print(data)  

# print(urltoadd)

# response = requests.post(api_url, json = urltoadd)
# print(response.json)
# print(response.headers["Content-Type"])