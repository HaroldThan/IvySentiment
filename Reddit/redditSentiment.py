import csv
import pandas as pd

csv.field_size_limit(100000000)

file = open("Reddit/redditTop50.csv")
data = csv.reader(file)

schoolDictionary = dict()
with open('AllReddit.txt', 'w') as f:
    for item in data:
        comment = item[1] + " || " + item[9]
        schoolName= item[1]
        comment = item[9]
        if schoolName not in schoolDictionary:
            schoolDictionary[schoolName] =[]

        schoolDictionary[schoolName].append([comment])

for key in schoolDictionary:
    with open(f"{key}Reddit.txt","w") as schoolFile:
        for comment in schoolDictionary[key]:
            schoolFile.writelines(comment)