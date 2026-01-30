# https://youtu.be/Nonkpvfs2fU

import numpy as np
import matplotlib.pyplot as plt

def experiment():
    money = 100000
    for i in range (0,1000):
        earning = np.random.choice([100,-100],1,p=[0.5,0.5])
        money = money + earning
    return money



if __name__ == "__main__":
    data = []
    for i in range(0, 200):
        datapoint = experiment()
        data.append(datapoint)
    plt.plot(np.array(data))
    plt.hlines(np.array(data).mean(), 0, 200, color = 'red')
    plt.show()