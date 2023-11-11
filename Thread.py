from threading import Thread

counter=0

def thread_1():
    global counter
    for i in range(100000):
        counter+=1

def thread_2():
    global counter
    for i in range(100000):
        counter-=1

thread1=Thread(target= thread_1)
thread2=Thread(target= thread_2)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(counter)