# 1-min-olhc-to-multiple-timeframe-converter
Data for several stocks, Indexes and futures are scarce , So here is a simple python script to convert your 1 min data into multiple timeframe olhc data.

# How to use
![image](https://user-images.githubusercontent.com/84351843/186872211-e6cbe54b-e176-4814-9a82-b03e8c974915.png)
This is the format for the source csv file.
To select the timeframe in which you want to convert, just adjust the freq
t = df.groupby(pd.Grouper(freq='15min')).agg({"Open": "first", 
                                             "Close": "last", 
                                             "Low": "min", 
                                             "High": "max"})
for example freq = '5min' for 5 minute date
            freq = '1d' for 1 day data
                                             
