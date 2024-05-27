"""Module which writes a URL to Instapaper."""

import os
import requests

from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USERNAME')
USERPASS = os.getenv('USERPASS')

#This creates parameter for the POST request
URL = "https://wilderreport.substack.com/p/the-prairies-frozen-angel"
TITLE = "The Prairie's Frozen Angel: Hazel Miner's Sacrifice Echoes through Eternity"
SELECTION = "This article was originally told by my friend The Way I Heard It: . " \
     "Not many outside of North Dakota know this incredible true story. Hazel's " \
     "story needs telling, and go follow. The Way I Heard It: The prairie wind howls " \
     "like a famished beast, ripping across the plains with teeth of ice. In this land " \
     "of stark beauty and brutal winters, survival is a knife's edge, a dance with death " \
     "where the weak wither and the strong endure. But even the harshest landscapes " \
     "can't extinguish the flames of courage that flicker in the human heart. Enter Hazel " \
     "Miner, a fifteen-year-old girl whose story is etched in ice and blood, a testament " \
     "to the raw, untamed power of love."

params = ({"url": URL, "title": TITLE,"selection": SELECTION})

#This posts the request using HTTPS basic authentication
resp = requests.post("https://www.instapaper.com/api/add", data=params, \
    auth=(USERNAME, USERPASS), timeout=10)

#This prints the response code
print(resp)
