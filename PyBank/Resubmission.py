import csv
csvpath = "budget_data.csv" #since this file is in the same folder as the code
data = []

#read CSV into data list so we can manipulate elements
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader,None)#skip header
    for row in csvreader:
        data.append(row)

#since each row represent 1 month, we just need to count the rows
count = len(data)

#assign 0 to variable "total", then runs through the data to add and subtract
total = 0
for row in data:
    total = total + int(row[1])

#initiate a list for month-over-month PL changes, then take average of that list
change = []
for i in range(count-1): #loops through data 85 times
    change.append(int(data[i+1][1]) - int(data[i][1]))
averagechange=sum(change)/len(change)

#assign initial month Feb and corresponding change value
increase = [data[1][0],change[0]]
decrease = [data[1][0],change[0]]

#then cycle through change list and determine whether each change was greater/lesser than previous one
for row in change:
    if row > increase[1]:
        increase[1] = row
        increase[0]=data[change.index(row)+1][0]
    elif row < decrease[1]:
        decrease[1] = row
        decrease[0] = data[change.index(row)+1][0]

#summarize, print to terminal, export to text
summary = """Total Months: {}\nTotal: {}\nAverage Change: {}\nGreatest Increase in Profits: {}\nGreatest Decrease in Profits: {}""".format(count,total,averagechange,increase,decrease)
print(summary)
textfile=open("summary.txt","w+")
textfile.write(summary)
textfile.close()