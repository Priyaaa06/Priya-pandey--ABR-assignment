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
      "[12, 24, 35, 88, 120, 155]\n"
     ]
    }
   ],
   "source": [
    "def Remove(duplicate): \n",
    "    final_list = [] \n",
    "    for num in duplicate: \n",
    "        if num not in final_list: \n",
    "            final_list.append(num) \n",
    "    return final_list \n",
    "      \n",
    "# Driver Code \n",
    "duplicate = [12,24,35,24,88,120,155,88,120,155] \n",
    "print(Remove(duplicate))"
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
