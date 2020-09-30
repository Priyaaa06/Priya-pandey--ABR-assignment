{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'New': 1, 'to': 1, 'Python': 5, 'or': 2, 'choosing': 1, 'between': 1, '2': 2, 'and': 1, '3?': 1, 'Read': 1, '3.': 1}\n"
     ]
    }
   ],
   "source": [
    "def word_count(str):\n",
    "    counts = dict()\n",
    "    words = str.split()\n",
    "\n",
    "    for word in words:\n",
    "        if word in counts:\n",
    "            counts[word] += 1\n",
    "        else:\n",
    "            counts[word] = 1\n",
    "\n",
    "    return counts\n",
    "\n",
    "print( word_count('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'))"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
