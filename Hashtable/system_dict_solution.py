from Hashtable import Hashtable
from threading import Thread

file = open("2sum.txt")
lines = file.readlines()
array = [int(line) for line in lines]
flag = 0


for j in array:
    for i in range(-10000,10000):
        target = i - j
        if target in array:
            flag += 1
            print(flag)
        break

print(flag)
