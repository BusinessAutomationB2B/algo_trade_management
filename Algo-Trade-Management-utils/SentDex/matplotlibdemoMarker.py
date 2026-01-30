import numpy as np
import matplotlib.pyplot as plt

def demo1():
    xs = np.linspace(-np.pi, np.pi, 30)
    ys = np.sin(xs)
    # markers_on = [12, 17, 18, 19]
    # markers_on=[0,1,2,29]
    markers_on=[0,1,2,3,15,29]
    plt.plot(xs, ys, '-gD', markevery=markers_on)
    plt.show()

def demo2():
# display value on chart: https://stackoverflow.com/questions/6282058/writing-numerical-values-on-the-plot-with-matplotlib
    x=[1,2,3]
    y=[9,8,7]
    plt.plot(x,y)
    for a,b in zip(x, y): 
        plt.text(a, b, str(b))
    plt.show()
    
if __name__=='__main__':
    # demo1()
    demo2()
    
    