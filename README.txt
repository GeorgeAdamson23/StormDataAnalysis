Location of the Storm Events Database:
https://www.ncdc.noaa.gov/stormevents/ftp.jsp
My script analyzed the StormEvents-details-ftp-v1.0 Files from 2000-2018

load_events.py:
This script was responsible for creating a large SQLite3 database from all of the Storm Event Data.
This database can be viewed with a graphical user interface (GUI) by running the application DB Browser (SQLite).
It read in a comma separated value (.csv) file from each year in the period 2000-2018.
It then dropped any data columns I did not find useful in my data analysis, and loaded the important data columns into a SQLite3 database file named StormEvents.sqlite.
The primary way to adjust this script file would be to add any extra .csv files you may want to load for data analysis.
Additional filenames can be added as strings into the stormEventsFileNames list. Make sure the .csv file is in the same directory as the rest of the files.
Another possible change would be to include or exclude other data columns. This can be done by editing the “CREATE TABLE” statement as well as the “read_csv” statement.
The column data titles can be found at the top of each .csv file.


analyze_events.py:
This is the primary Python script file for data analysis.
The code is structured in that it asks several research questions, and it performs a SQL Query to fetch the data that applies to the current question.
For most of my research questions I was keeping track of the number of storms in each calendar month.
The variables I was manipulating were the DTX Region/Washtenaw County (wfo or cz_name) and the type of storm (event_type).
I also made sure to make the episode_id distinct/unique.
This way if there was a large synoptic storm affecting multiple counties, I would still only count it as a single storm event.
Finally, the code would create several bar graphs to illustrate the storms present in each month. 
When the code is running, it will pause when a figure is created. To continue running the code, you must close the current figure.
This function will also print data to the console if you want to read text instead of figures.
