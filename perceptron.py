import numpy as np
import time
import matplotlib.pyplot as plt


def hardlim(val):
    if val < 0:
        return 0
    return 1


def abrainicializalas(data):
    plt.ion()
    rajz = plt.figure()
    plt.grid(True)
    plt.xlim((-2, 2))
    plt.ylim((-2, 2))
    plt.scatter(data[:, 1], data[:, 2])
    return rajz


def abra(x,z,a,abrazolas):
    vonal, = plt.plot(a, a * z + x[1])
    vonal.set_ydata(a * z + x[1])
    abrazolas.canvas.draw()
    time.sleep(0.3)
    vonal.remove()
    abrazolas.canvas.flush_events()


def perceptronAnd (adat, v):
    N, n = adat.shape
    E = 1
    lr = 0.01
    w = np.random.randn(n, 1)
    a = np.linspace(-5, 5, 50)
    abrazolas = abrainicializalas(adat)
    while E != 0:
        E = 0
        for i in range(N):
            yi = hardlim(np.dot(adat[i], w))
            ei = v[i] - yi
            w = w + lr * ei * adat[i].reshape(n, 1)
            E = E + ei ** 2
        x = [0, -w[0] / w[2]]
        y = [-w[0] / w[1], 0]
        z = (x[1] - x[0]) / (y[1] - y[0])
        abra(x,z,a,abrazolas)

def perceptronHI(adat,v):
    N, n = adat.shape
    E = 1
    lr = 0.01
    wh = np.random.randn(n, 1)
    wi = np.random.randn(n, 1)
    while E != 0:
        E = 0
        for i in range(N):
            yih = hardlim(np.dot(adat[i],wh))
            yii = hardlim(np.dot(adat[i],wi))
            eih = v[i][0] - yih
            eii = v[i][1] - yii
            wh = wh + lr * eih*adat[i].reshape(n,1)
            wi = wi + lr * eii*adat[i].reshape(n,1)
            E = E+ eih**2
            E = E+ eii**2


menu = True
while menu:
    print("""
    1.Perceptron And
    2.Perceptron H/I
    """)
    menu =input("Valasszon:")
    if menu=="1":
        minta = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]])
        fej = [0, 0, 0, 1]
        perceptronAnd(minta, fej)
    elif menu=="2":
        minta = np.array([[1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                           [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
                           ])
        fej=np.array([[1, 0], [0, 1]])
        perceptronHI(minta,fej)
    else:
        print("Nincs ilyen menupont!")

