{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input your password Abcd@123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid Password\n"
     ]
    }
   ],
   "source": [
    "p= input(\"Input your password\")\n",
    "x = True\n",
    "while x:  \n",
    "    if (len(p)<6 or len(p)>12):\n",
    "        break\n",
    "    elif not re.search(\"[a-z]\",p):\n",
    "        break\n",
    "    elif not re.search(\"[0-9]\",p):\n",
    "        break\n",
    "    elif not re.search(\"[A-Z]\",p):\n",
    "        break\n",
    "    elif not re.search(\"[$#@]\",p):\n",
    "        break\n",
    "    elif re.search(\"\\s\",p):\n",
    "        break\n",
    "    else:\n",
    "        print(\"Valid Password\")\n",
    "        x=False\n",
    "        break\n",
    "\n",
    "if x:\n",
    "    print(\"Not a Valid Password\")"
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
