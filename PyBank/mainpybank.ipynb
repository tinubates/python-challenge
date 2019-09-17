{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months: 86\n",
      "Total: 38382578\n",
      "Average Change: -2315.1176470588234\n",
      "Greatest Increase in Profits: ['Feb-2012', 1926159]\n",
      "Greatest Decrease in Profits: ['Sep-2013', -2196167]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "csvpath = \"budget_data.csv\" #since this file is in the same folder as the code\n",
    "data = []\n",
    "\n",
    "#read CSV into data list so we can manipulate elements\n",
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader=csv.reader(csvfile,delimiter=',')\n",
    "    next(csvreader,None)#skip header\n",
    "    for row in csvreader:\n",
    "        data.append(row)\n",
    "\n",
    "#since each row represent 1 month, we just need to count the rows\n",
    "count = len(data)\n",
    "\n",
    "#assign 0 to variable \"total\", then runs through the data to add and subtract\n",
    "total = 0\n",
    "for row in data:\n",
    "    total = total + int(row[1])\n",
    "\n",
    "#initiate a list for month-over-month PL changes, then take average of that list\n",
    "change = []\n",
    "for i in range(count-1): #loops through data 85 times\n",
    "    change.append(int(data[i+1][1]) - int(data[i][1]))\n",
    "averagechange=sum(change)/len(change)\n",
    "\n",
    "#assign initial month Feb and corresponding change value\n",
    "increase = [data[1][0],change[0]]\n",
    "decrease = [data[1][0],change[0]]\n",
    "\n",
    "#then cycle through change list and determine whether each change was greater/lesser than previous one\n",
    "for row in change:\n",
    "    if row > increase[1]:\n",
    "        increase[1] = row\n",
    "        increase[0]=data[change.index(row)+1][0]\n",
    "    elif row < decrease[1]:\n",
    "        decrease[1] = row\n",
    "        decrease[0] = data[change.index(row)+1][0]\n",
    "\n",
    "#summarize, print to terminal, export to text\n",
    "summary = \"\"\"Total Months: {}\\nTotal: {}\\nAverage Change: {}\\nGreatest Increase in Profits: {}\\nGreatest Decrease in Profits: {}\"\"\".format(count,total,averagechange,increase,decrease)\n",
    "print(summary)\n",
    "textfile=open(\"summary.txt\",\"w+\")\n",
    "textfile.write(summary)\n",
    "textfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
