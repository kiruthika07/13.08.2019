from twitter import *
import csv

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(1140643453262389248-o9uUtmo2FOxEyJvZOuZb4UGDhs4qoJ ,
                  yHZMdlWB3xxaV60GJ0IB0UsxtQwtniC4ttu4rL4nPHpfC,
                  kILI0ypHXgbHVbV9SshWbv0v9,
                  PNnGdPMy96F0HdKvXvBRi2tZn9J4SExxTPtMJB20edb9zy7RKV ))


results = twitter.trends.place(_id = 23424848)

print("Indian Trends")
trends=[]
for location in results:
    #print(location)
    for trend in location["trends"]:
        #print(" - %s" % trend["name"])
        trends.append([trend["name"]])
#print (trends)
with open('twitter_trends.csv', 'w',encoding="utf-8",newline='') as csvFile:
   csvwriter = csv.writer(csvFile)
   csvwriter.writerows(trends)
      
