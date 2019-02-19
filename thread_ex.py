import threading
#threading.Thread(grops=None, target=None,agrs=(), kwarg={}, deamon=None
def square(seq):
    for i in seq:
        print("Suare: ", i**2)
def cube(seq):
    for i in seq:
        print("Cube: ", i**3)
L=[2,3, 5, 6]
t=threading.Thread(target=square, args=(L,))
t.start()
t.join()
t1=threading.Thread(target=cube, args=(L,))
t1.start()
