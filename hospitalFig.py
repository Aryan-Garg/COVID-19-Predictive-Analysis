import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data taken from CCDP (A Princeton study which estimates the total number of hospitals and equipment)
hos = pd.read_csv("Hos_ICU_vent_state.csv")
state = hos["States"]
totHos = hos["Total Hospitals"]
ICU_beds = hos["ICU_Beds"]


dic1 = {}

for i in range(len(state)):
    dic1[state[i]] = [totHos[i],ICU_beds[i]]
    
dic1 = sorted(dic1.items(), key = lambda x: x[1][1])

xpts = []
ypts = []
y2pts = []
for i in dic1:
    xpts.append(i[0])
    ypts.append(i[1][0])
    y2pts.append(i[1][1])
    
x = np.arange(len(xpts))
plt.style.use('fivethirtyeight')
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ypts, width, label='Hospitals')
rects2 = ax.bar(x + width/2, y2pts, width, label='ICU Beds')

ax.set_title('Hospitals and ICU Beds in states')
ax.set_xticks(x)
ax.set_xticklabels(xpts)

plt.xticks(rotation=-90)

ax.legend()
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
#autolabel(rects1)
#autolabel(rects2)

plt.show()

'''
Total Hospitals : 69228
Total ICU Beds  : 94963
'''
