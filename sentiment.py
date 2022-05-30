### EXTRACT TWEETS FROM JSON DATA AND AGGREGATE EACH SCHOOL TO ITS OWN TEXT FILE
### HAROLD THAN '23, DARTMOUTH COLLEGE

import json

schoolNames= ['brown', 'columbia', 'cornell','dartmouth','harvard','penn','princeton','yale']
for schoolName in schoolNames:
    #Read Current School
    with open(f'IviesRetweetData/{schoolName}.json') as json_file:
        datas = json.load(json_file)

    sumOfTweets = []
    for item in datas:
        sumOfTweets.append(item['tweets'])

    # Write Tweets To Text File
    with open(f'IviesRetweetData/TweetsOnly/{schoolName}Tweets.txt', 'w') as f:
        for tweet in sumOfTweets:
            f.writelines(tweet)