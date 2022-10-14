import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    z = x*y
    print ('hey')
    return z

def g(x,y):
    A = f(x,y)
    print(A)
    return A+1

def test(x):
    for i in range(0,x):
        print (i)

def t(x):
    for t in range(0,x+3):
        print (t-1)

def somme(x):
    s = 0
    for i in range(0,x+1):
        s = s+i
        print(s)
    return 'la valeur finale est', s
x = [8,10,14]
y = [11,15,20]

#plt.figure('maman')
#plt.plot(x,y)

#plt.figure('papa')
#plt.plot(y,x)
#plt.show()

a = np.array([2,7])
b = np.array([34,1])


c = np.array([[1,2],[5,6]])