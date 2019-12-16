import matplotlib.pyplot as plt
from random_walk import RandomWalk

c = 'y'
while c=='y': 
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    pts = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=pts,
        cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0, 0 , c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
        edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    c = input("Another(y/n): ")