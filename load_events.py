# Created by George Adamson on 07/31/2019.
# This script will load in storm events data from .csv file extension
# These files can be found on https://www.ncdc.noaa.gov/stormevents/ftp.jsp

import sqlite3
import pandas as pd
import numpy as np


# For purposes of this analysis, we will only be analyzing for the time period 2000-2019
stormEventsFileNames = ['StormEvents_details-ftp_v1.0_d2000_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2001_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2002_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2003_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2004_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2005_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2006_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2007_c20170717.csv',
                        'StormEvents_details-ftp_v1.0_d2008_c20180718.csv',
                        'StormEvents_details-ftp_v1.0_d2009_c20180718.csv',
                        'StormEvents_details-ftp_v1.0_d2010_c20170726.csv',
                        'StormEvents_details-ftp_v1.0_d2011_c20180718.csv',
                        'StormEvents_details-ftp_v1.0_d2012_c20190516.csv',
                        'StormEvents_details-ftp_v1.0_d2013_c20170519.csv',
                        'StormEvents_details-ftp_v1.0_d2014_c20180718.csv',
                        'StormEvents_details-ftp_v1.0_d2015_c20180525.csv',
                        'StormEvents_details-ftp_v1.0_d2016_c20180718.csv',
                        'StormEvents_details-ftp_v1.0_d2017_c20190716.csv',
                        'StormEvents_details-ftp_v1.0_d2018_c20190716.csv']


# Create an SQLite database file to store this information
conn = sqlite3.connect('StormEvents.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Storm_Events ''')
cur.execute('''CREATE TABLE Storm_Events (year TEXT, month_name TEXT, episode_id TEXT, state TEXT, event_type TEXT, cz_name TEXT, wfo TEXT)''')


for year in stormEventsFileNames:
    # Only include specific columns from the excel file
    stormEvents = pd.read_csv(year, usecols=['STATE','YEAR','EPISODE_ID','MONTH_NAME','EVENT_TYPE','CZ_NAME','WFO'], dtype={'STATE': str, 'YEAR' : str, 'EPISODE_ID' : str, 'MONTH_NAME' : str, 'EVENT_TYPE' : str, 'CZ_NAME' : str, 'WFO' : str})

    # Send this year's data into the SQL database
    stormEvents.to_sql('Storm_Events', conn, if_exists='append', index=False)


cur.close()
