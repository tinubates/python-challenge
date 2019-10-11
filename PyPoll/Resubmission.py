import csv
import numpy as np
csvpath = "election_data.csv" #since this file is in the same folder as the code
data = []

#read CSV into data list so we can manipulate elements
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader,None)#skip header
    for row in csvreader:
        data.append(row)

#since each row represent 1 vote, we just need to count the rows
votecount=len(data)

#find unique candidates
candidates=[]
for row in data:
    candidates.append(row[2])
candidatelist=set(candidates)

#establish candidate vote count array
tally=[]
for item in candidatelist:
    info=[item,0,0]
    tally.append(info)
    
#properly populate vote count in position [1] of the tally array
for item in tally:
    for row in data:
        if row[2]==item[0]:
            item[1]=item[1]+1

#properly populate vote percentage in position [2] of the tally array as well as winner
maxvotes= 0
winner = ''
for item in tally:
    item[2]="("+str(round(item[1]/votecount*100,1))+"%)"#multiply 100 for % and round to 1 decimal
    if item[1] > maxvotes:
        maxvotes = item[1]
        winner = item[0]

        
#summarize, print to terminal, export to text
summary = """Total Votes: {}""".format(votecount)
for row in tally:
    summary = summary+"\n"
    for item in row:
        summary = summary+" "+str(item)
summary = summary+"\n"+("Winner: {}".format(winner))
print(summary)
textfile=open("summary.txt","w+")
textfile.write(summary)
textfile.close()