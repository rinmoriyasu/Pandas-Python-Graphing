import scipy
import matplotlib.pyplot as plt
import numpy as np
import my_data as dc
import pandas as pd



fig, ax = plt.subplots()

#plotter 'label' should be whatever column name is in the original .csv file. Needs to also be changed in my_data.py
plt.plot(dc.x, dc.light_crude, ls = '-.', color = '#9932CC', linewidth = '2', label = 'Light Crude')
plt.plot(dc.x, dc.medium_crude, ls = '-.', color = '#FF8C00', linewidth = '2', label = 'Medium Crude')
plt.plot(dc.x, dc.heavy_crude, ls = '-.', color = '#008080', linewidth = '2', label = 'Heavy Crude')

plt.plot(dc.x, dc.condensate, ls = '-', color = '#20B2AA', linewidth = '2', label = 'Condensate')
plt.plot(dc.x, dc.ifo, ls = '--', color = '#FF0000', linewidth = '2', label = 'IFO')
plt.plot(dc.x, dc.hfo, ls = '-', color = '#EE82EE', linewidth = '2', label = 'HFO')
plt.plot(dc.x, dc.jet_fuel, ls = '--', color = '#F0E68C', linewidth = '2', label = 'Jet Fuel')
plt.plot(dc.x, dc.diesel, ls = '--', color = '#E9967A', linewidth = '2', label = 'Diesel')
plt.plot(dc.x, dc.gasoline, ls = '-.', color = '#DEB887', linewidth = '2', label = 'Gasoline')

#This adds an onclick event to the plot shown by plt.show()
def onclick(event):
    print(f"""

    The point you clicked is:
    >>>
    Distillation Fraction: {event.xdata}
    Temperature: {event.ydata} °C
    
    >>>
    """)

cid = fig.canvas.mpl_connect("button_press_event", onclick)

#labels
plt.xlabel("Distillation Fractions")
plt.ylabel("Temperatures (°C):")
plt.legend(frameon = False)
plt.savefig('distillation_curve.pdf') #rename this to whatever your outfile should be.
#show
plt.show()


