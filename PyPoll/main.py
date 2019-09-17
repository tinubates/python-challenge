{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Votes: 3521001\n",
      "[[\"O'Tooley\", 105630, 0.02999999147969569], ['Li', 492940, 0.13999996023857988], ['Correy', 704200, 0.19999994319797126], ['Khan', 2218231, 0.6300001050837531]]\n",
      "Winner: Khan(2218231)\n"
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
    "    item[2]=item[1]/votecount\n",
    "    if item[1] > maxvotes:\n",
    "        maxvotes = item[1]\n",
    "        winner = item[0]\n",
    "\n",
    "        \n",
    "#summarize, print to terminal, export to text\n",
    "summary = \"\"\"Total Votes: {}\\n{}\\nWinner: {}({})\"\"\".format(votecount,tally,winner,maxvotes)\n",
    "print(summary)\n",
    "textfile=open(\"summary.txt\",\"w+\")\n",
    "textfile.write(summary)\n",
    "textfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3521001"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'jon', 'mark'}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidatelist=set(['jon','jon','mark'])\n",
    "candidatelist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "test\n"
     ]
    }
   ],
   "source": [
    "print('test')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "2218231 is not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-890d910e62ae>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtally\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmaxvotes\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m: 2218231 is not in list"
     ]
    }
   ],
   "source": [
    "tally.index(maxvotes)"
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
