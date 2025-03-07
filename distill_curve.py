import scipy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = pd.read_excel("distillation_curves.xlsx")

x = file['Fractions']

#all y-axis
light_crude = file['Light Crude']
medium_crude = file['Medium Crude']
heavy_crude = file['Heavy Crude']
ifo = file['IFO']
hfo = file['HFO']
condensate = file['Condensate']
jet_fuel = file['Jet Fuel']
diesel = file['Diesel']
gasoline = file['Gasoline']






