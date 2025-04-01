import random
import time

def getRandomDate(startDate, endDate):
    print("Printing a random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("The Random Date is: ", getRandomDate("1/1/2016", "12/12/2018"))