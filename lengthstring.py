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
      "The input is  thedogisthewise\n",
      "The length of the longest non-repeating character substring is  15\n"
     ]
    }
   ],
   "source": [
    "def areDistinct(strr, i, j): \n",
    " \n",
    "    visited = [0] * (26) \n",
    "  \n",
    "    for k in range(i, j + 1): \n",
    "        if (visited[ord(strr[k]) - \n",
    "                   ord('a')] == True): \n",
    "            return -1\n",
    "              \n",
    "        visited[ord(strr[k]) -\n",
    "                ord('a')] = True\n",
    "  \n",
    "    return True\n",
    "   \n",
    "def longestUniqueSubsttr(strr): \n",
    "      \n",
    "    n = len(strr) \n",
    " \n",
    "    res = 0 \n",
    "      \n",
    "    for i in range(n): \n",
    "        for j in range(i, n): \n",
    "            if (areDistinct(strr, i, j)): \n",
    "                res = max(res, j - i + 1) \n",
    "                  \n",
    "    return res \n",
    " \n",
    "if __name__ == '__main__': \n",
    "      \n",
    "    strr = \"thedogisthewise\"\n",
    "    print(\"The input is \", strr) \n",
    "      \n",
    "    len = longestUniqueSubsttr(strr) \n",
    "    print(\"The length of the longest \"\n",
    "          \"non-repeating character substring is \", len)"
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
