import csv
newData = []
# open and read the CSV file
with open('data.csv', 'rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        newData.append(row)
        rowLength = len(row)
    
    meanList = [0]*rowLength
    fourPlusCount = [0]*rowLength
    
    # store the number of users who rated that movie, the average rating, % of 4+ ratings, 
    userCount=[0]*rowLength
    for rowIndex, list in enumerate(newData):
        for columnIndex, rating in enumerate(list):
            if rowIndex > 0 and columnIndex > 0 and rating:
                meanList[columnIndex] += int(rating)
                userCount[columnIndex] += 1
            if rowIndex > 0 and columnIndex >0:
                if rating:
                    if int(rating)>=4:
                       fourPlusCount[columnIndex]+=1

    # Calculate the mean rating for each movie & the proportion of 4+ ratings
    for index, count in enumerate(meanList):
        if userCount[index] is not 0:
            meanList[index] = "%.2f" % round(float(meanList[index])/userCount[index], 2)
    for index, count in enumerate(fourPlusCount):
        if userCount[index] is not 0:
            fourPlusCount[index] = "%.2f" % round(float(fourPlusCount[index]) * 100 /userCount[index], 2)
    
    
    # Create dictionary with movie names and the mean rating, and proportion of 4+ ratings
    meanDict = {}
    fourPlusDict={}
    for mean, name in zip(meanList, newData[0]): 
        meanDict[float(mean)] = name
    for count, name in zip(fourPlusCount, newData[0]): 
       fourPlusDict[float(count)] = name
       
    # Sort dictionary based on the mean rating/proportion of 4+ ratings
    sortedMeanDict = sorted(meanDict.items(), key=lambda t: t[0], reverse = True)
    sortedFourPlusDict= sorted(fourPlusDict.items(), key=lambda t: t[0], reverse = True)
    for i in range(0, 5):
        print "Top 5 movies on average rating:", sortedMeanDict[i][1]
    for i in range(0, 5):     
        print "Top 5 movies on % of 4+ ratings:", sortedFourPlusDict[i][1]
