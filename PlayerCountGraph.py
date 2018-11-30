import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

# to download the page
import requests

# use for time delay on scraping
import time

# allows us to email
import smtplib


old_txt = ""

player_counts = []

plt.plot([1,2,3,6])
plt.ylabel('some numbers')
plt.show()
    
# The following two methods were obtained from:
# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


    

while True:
    current_num = ""
    html = urllib.request.urlopen('https://oldschool.runescape.com/').read()
    txt = text_from_html(html)
    index = txt.find('currently')
    displacement = len('currently') + 1
    num_location = index + displacement
    print(txt[num_location])
    
    while (txt[num_location] != ','):
        current_num += txt[num_location]
        num_location += 1
    
    num_location += 1
    
    while (txt[num_location] != ' '):
        current_num += txt[num_location]
        num_location += 1
        
    print(current_num)
    player_counts.append(int(current_num))
    
    print(player_counts)
    
    # check the player count every 60 seconds
    time.sleep(2)



    

