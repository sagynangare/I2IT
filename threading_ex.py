import threading
def demo():
    for i in range(1,6):
        print('Square : ', i*i)

t = threading.Thread(target=demo)
t1 = threading.Thread(target=demo)
t2 = threading.Thread(target=demo)
t.start()
t.join()
t1.start()
t1.join()
t2.start()
t2.join()
