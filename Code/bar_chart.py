import matplotlib.pyplot as plt
import numpy as np

def bar_chart(names, std,titlex,titley,option):
    N =len(names)

    ind = np.arange(N)
    width = 0.35 
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, tuple(std), width, color='lawngreen',edgecolor="red",linewidth=0.2)
    ax.set_ylabel(titley)
    ax.set_title(titlex)
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    autolabel(rects1, ax,option)
    
    plt.show()
    return 0

def autolabel(rects, ax,option):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        if option == 'float':
            ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                    '{0}%'.format(float(round(height,1))),
                    ha='center', va='bottom')
        if option == 'int':
            ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                    '{0}%'.format(int(height)),
                    ha='center', va='bottom')