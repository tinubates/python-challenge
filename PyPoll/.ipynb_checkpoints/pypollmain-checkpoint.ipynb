{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Votes: 3521001\n",
      " O'Tooley 105630 (3.0%)\n",
      " Li 492940 (14.0%)\n",
      " Correy 704200 (20.0%)\n",
      " Khan 2218231 (63.0%)\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import numpy as np\n",
    "csvpath = \"election_data.csv\" #since this file is in the same folder as the code\n",
    "data = []\n",
    "\n",
    "#read CSV into data list so we can manipulate elements\n",
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader=csv.reader(csvfile,delimiter=',')\n",
    "    next(csvreader,None)#skip header\n",
    "    for row in csvreader:\n",
    "        data.append(row)\n",
    "\n",
    "#since each row represent 1 vote, we just need to count the rows\n",
    "votecount=len(data)\n",
    "\n",
    "#find unique candidates\n",
    "candidates=[]\n",
    "for row in data:\n",
    "    candidates.append(row[2])\n",
    "candidatelist=set(candidates)\n",
    "\n",
    "#establish candidate vote count array\n",
    "tally=[]\n",
    "for item in candidatelist:\n",
    "    info=[item,0,0]\n",
    "    tally.append(info)\n",
    "    \n",
    "#properly populate vote count in position [1] of the tally array\n",
    "for item in tally:\n",
    "    for row in data:\n",
    "        if row[2]==item[0]:\n",
    "            item[1]=item[1]+1\n",
    "\n",
    "#properly populate vote percentage in position [2] of the tally array as well as winner\n",
    "maxvotes= 0\n",
    "winner = ''\n",
    "for item in tally:\n",
    "    item[2]=\"(\"+str(round(item[1]/votecount*100,1))+\"%)\"#multiply 100 for % and round to 1 decimal\n",
    "    if item[1] > maxvotes:\n",
    "        maxvotes = item[1]\n",
    "        winner = item[0]\n",
    "\n",
    "        \n",
    "#summarize, print to terminal, export to text\n",
    "summary = \"\"\"Total Votes: {}\"\"\".format(votecount)\n",
    "for row in tally:\n",
    "    summary = summary+\"\\n\"\n",
    "    for item in row:\n",
    "        summary = summary+\" \"+str(item)\n",
    "summary = summary+\"\\n\"+(\"Winner: {}\".format(winner))\n",
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
