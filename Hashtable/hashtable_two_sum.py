from Hashtable import Hashtable
from threading import Thread

file = open("2sum.txt")
lines = file.readlines()
hash = Hashtable(703903)
for line in lines:
    hash.insert(int(line))

print("initialization of hashtable has done!")



def two_sum(start, end):
    flag = 0 
    for i in range(start, end):
        target = i
        for j in lines:
            if hash.haskey(i-int(j)) and i!= int(j):
                flag += 1 
                continue
    print(flag)
    return flag

class MyThread(Thread):
    def __init__(self, upper, lower):
        Thread.__init__(self)
        self.upper = upper
        self.lower = lower

    def run(self):
        self.result = two_sum(self.upper, self.lower)

    def get_result(self):
        return self.result


thread1 = MyThread(0,5000)
thread2 = MyThread(5000,10001)
thread3 = MyThread(-5000,0)
thread4 = MyThread(-10000,-5001)


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(sum([thread1.get_result(),thread2.get_result(),thread3.get_result(), thread4.get_result()]))
#print(flag)

    #for i in range(-10000,10001):
