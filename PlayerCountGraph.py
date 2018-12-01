import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

# use for time delay
import time
value_set = False
# This is how frequently (in seconds) the graph will update player count
# Recommended: Set update_frequency to 1 (second), 60 (minute), or 3600 (hour)
while value_set == False:
    try:
        update_frequency = int(input("""At what frequency would  you like to update the graph? \nFor reference:
                                     \nOne second: 1 \nOne minute: 60 \nOne hour: 3600\n"""))
        if (update_frequency > 0):
            value_set = True
    except ValueError:
        print("Please enter a positive number!")
# turns on interactive mode
plt.ion()

# sets the y label to players online
plt.ylabel('Players online')

# sets the x label to reflect update_frequency
if update_frequency == 1:
    plt.xlabel('Seconds')
elif update_frequency == 60:
    plt.xlabel('Minutes')
elif update_frequency == 3600:
    plt.xlabel('Hours')
else:
    plt.xlabel('Seconds (' + str(update_frequency) + 's)')

# list of player counts (grows over time)
player_counts = []
    
# The following two functions were obtained from:
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
    
    while (txt[num_location] != ','):
        current_num += txt[num_location]
        num_location += 1
    
    num_location += 1
    
    while (txt[num_location] != ' '):
        current_num += txt[num_location]
        num_location += 1
        
    #print(current_num)
    player_counts.append(int(current_num))
    
    #print(player_counts)
    plt.plot(player_counts)
    plt.pause(0.0001)

    
    # check the player count every x seconds
    time.sleep(update_frequency)



    

