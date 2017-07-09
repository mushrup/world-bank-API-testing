#this module output the overall cpi multiple from 1976 to 2013
#!/local/bin/python
import wbdata
import datetime
import pandas
import matplotlib.pyplot as plt

#set up the countries I want
countries = "US"

#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'GFDD.OE.01':'CPI(2010=100)'}

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, data_date=(datetime.datetime(1976, 1, 1), datetime.datetime(2013, 1, 1)))
totalcpi = df['CPI(2010=100)'].values[0]/df['CPI(2010=100)'].values[-1]
print "The overall CPI multiple from 1976 to 2013:",totalcpi

