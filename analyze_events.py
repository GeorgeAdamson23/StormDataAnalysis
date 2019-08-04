# Created by George Adamson on 08/02/2019
# This script will analyze the storm event data that has been loaded into a SQL database using the load_events.py script
# By design, this script focuses on the Southeast Michigan region (DTX) and Washtenaw County, Michigan

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Open up the SQL database with storm event data
conn = sqlite3.connect('StormEvents.sqlite')
cur = conn.cursor()



# Define a function to create the bar graphs for standard numStorms vs month
def createBarGraph(sqlstr,plotTitle):
    monthCount = {'January' : 0, 'February' : 0, 'March' : 0, 'April' : 0, 'May' : 0, 'June' : 0, 'July' : 0, 'August' : 0, 'September' : 0, 'October' : 0, 'November' : 0, 'December' : 0}

    for row in cur.execute(sqlstr):
        monthCount[row[1]] = monthCount[row[1]] + 1

    # Print to console to show num of occurrences
    print(plotTitle)
    print(monthCount)

    # Create a bar graph of the num of storm occurrences vs month
    plt.bar(range(len(monthCount)), list(monthCount.values()), align='center')
    plt.xticks(range(len(monthCount)), list(monthCount.keys()))
    plt.suptitle(plotTitle)
    fig = plt.gcf()
    fig.set_size_inches(13, 6)
    plt.show()

# Research Question 1: What is the probability of a heavy snow or winter storm event in each month in Southeast Michigan (DTX)?
# To ensure a single storm does not cause multiple storm events in multiple counties in DTX, I ensure that a unique episode_id is present. This way a single storm affecting
# multiple counties will register as a single event for that month.
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Heavy Snow' OR event_type = 'Winter Storm') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Heavy Snow or Winter Storm Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 2: What is the probability of a heavy snow or winter storm event in each month in Washtenaw County, Michigan?
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Heavy Snow' OR event_type = 'Winter Storm') AND cz_name = 'WASHTENAW') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Heavy Snow or Winter Storm Events in Washtenaw County, Michigan by Month From 2000-2018")



# Research Question 3: Probability of Ice Storms in Southeast Michigan (DTX) by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Ice Storm') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Ice Storm Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 4: Probability of Ice Storms in Washtenaw County, Michigan by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Ice Storm') AND cz_name = 'WASHTENAW') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Ice Storm Events in Washtenaw County, Michigan by Month From 2000-2018")



# Research Question 5: Probability of Blizzards in Southeast Michigan (DTX) by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Blizzard') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Blizzard Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 6: Probability of Thunderstorm Winds in Southeast Michigan (DTX) by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Thunderstorm Wind') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Thunderstorm Wind Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 7: Probability of Thunderstorm Winds in Washtenaw County, Michigan by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Thunderstorm Wind') AND cz_name = 'WASHTENAW') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Thunderstorm Wind Events in Washtenaw County, Michigan by Month From 2000-2018")



# Research Question 8: Probability of Hail in Southeast Michigan (DTX) by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Hail') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Hail Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 9: Probability of Hail in Washtenaw County, Michigan by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Hail') AND cz_name = 'WASHTENAW') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Hail Events in Washtenaw County, Michigan by Month From 2000-2018")



# Research Question 10: Probability of Tornados in Southeast Michigan (DTX) by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Tornado') AND wfo = 'DTX') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Tornado Events in Southeast Michigan (DTX) by Month From 2000-2018")



# Research Question 11: Probability of Tornados in Washtenaw County, Michigan by Month
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Tornado') AND cz_name = 'WASHTENAW') ORDER BY month_name'''
createBarGraph(sqlstr,"Number of Tornado Events in Washtenaw County, Michigan by Month From 2000-2018")



# Research Question 12: Combined Seasonal Storm Climatology for Southeast Michigan (DTX)
# This bar graph is a bit more involved, so I opted not to use the predefined function
sqlstr = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Heavy Snow' OR event_type = 'Winter Storm') AND wfo = 'DTX') ORDER BY month_name'''
monthCountWinter = {'January' : 0, 'February' : 0, 'March' : 0, 'April' : 0, 'May' : 0, 'June' : 0, 'July' : 0, 'August' : 0, 'September' : 0, 'October' : 0, 'November' : 0, 'December' : 0}

for row in cur.execute(sqlstr):
    monthCountWinter[row[1]] = monthCountWinter[row[1]] + 1

sqlstr2 = '''SELECT DISTINCT episode_id,month_name FROM Storm_Events WHERE (state = 'MICHIGAN' AND (event_type = 'Thunderstorm Wind') AND wfo = 'DTX') ORDER BY month_name'''
monthCountSummer = {'January' : 0, 'February' : 0, 'March' : 0, 'April' : 0, 'May' : 0, 'June' : 0, 'July' : 0, 'August' : 0, 'September' : 0, 'October' : 0, 'November' : 0, 'December' : 0}

for row in cur.execute(sqlstr2):
    monthCountSummer[row[1]] = monthCountSummer[row[1]] + 1

# Create a bar graph to show both summer and winter storm data
X = np.arange(len(monthCountWinter))
ax = plt.subplot(111)
ax.bar(X, monthCountWinter.values(), width=0.2, color='b', align='center')
ax.bar(X-0.2, monthCountSummer.values(), width=0.2, color='r', align='center')
ax.legend(('Heavy Snow/Winter Storms','Thunderstorm Wind Events'))
plt.xticks(X, monthCountWinter.keys())
plt.title("Combined Seasonal Storm Climatology for Southeast Michigan (DTX) by Month 2000-2018", fontsize=17)
fig = plt.gcf()
fig.set_size_inches(13, 6)
plt.show()
