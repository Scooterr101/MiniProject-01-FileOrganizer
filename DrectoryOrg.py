{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3e6c8dcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\hanse'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8b1f11e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\hanse\\\\PPlog'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.chdir(\"C:\\\\Users\\\\hanse\\\\PPlog\")\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e0f29480",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['.ipynb_checkpoints', '2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', 'DirectoryOrganizer_TEST-Copy1.ipynb', 'PlayData', 'TEST 1.txt', 'TEST 2.txt', 'TEST 3.txt', 'TEST 3.zip', 'TEST.py']\n"
     ]
    }
   ],
   "source": [
    "print(os.listdir(\"\\\\Users\\\\hanse\\\\PPlog\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ffa43e9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['.ipynb_checkpoints', '2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', 'PlayData']\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "path = \".\"\n",
    "ext = \"txt\", \"ipynb\", \"py\", \"zip\"\n",
    "\n",
    "for f in os.listdir(path):\n",
    "    fpath = os.path.join(path, f)\n",
    "\n",
    "    if os.path.isfile(fpath) and fpath.endswith(ext):\n",
    "        time = datetime.fromtimestamp(os.path.getctime(fpath)).strftime(\"%Y-%m-%d\")\n",
    "        os.makedirs(os.path.join(path, time), exist_ok=True)\n",
    "        os.replace(fpath, os.path.join(path, time, f))\n",
    "        \n",
    "print(os.listdir(\"\\\\Users\\\\hanse\\\\PPlog\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f20161b",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
