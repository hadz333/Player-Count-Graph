# PlayerCount Graph

This app will get the number of players online on Old School RuneScape and output an updated graph every x seconds: ideally 1, 60, or 3600. 

For example, if you set the graph to update every 60 seconds and let the program run for 1 hour, you will have a graph that displays the amount of players online over the course of that hour by the minute.

The graph utilizes the matplotlib plugin.
(https://matplotlib.org/users/pyplot_tutorial.html). 

The update frequency of the graph is by default 1 second. This can be changed via the update_frequency variable in the PlayerCountGraph.py file (line 12).
