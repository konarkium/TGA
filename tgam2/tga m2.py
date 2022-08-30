"""TGA M2"""

import matplotlib.pyplot as plt
from matplotlib import rc
font_properties = {'family':'Cambria', 
                   'weight':'bold',            
                   'size':12}                 
rc('font',**font_properties)

fig = plt.figure('TGA and DTG', figsize =(5,5), dpi = 300,)   

import pandas as pd
import numpy as np

poly = np.polynomial.Polynomial

filename = r"C:\Users\konar\Desktop\test.csv"

df = pd.read_csv(filename, 
                 skiprows = 2, #will skip the first two rows
                 )

h_lists = [df[s].dropna() for s in df.columns] #creates individual lists of columns

m = df['m']
Temp = df['Temp']

residue = 100 - ( (max(m) - m) / ( max(m) - min(m)) )*100

plt.plot(Temp,residue, label = 'resin', linestyle = '-', c='k') 
plt.xlabel('Temperature ($^o$C)')
plt.ylabel(r'1-$\alpha$ (%)')
plt.legend(loc=6)

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=3, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(which='major', direction='in', length=7, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(labelbottom=True, labeltop=False,
                labelleft=True, labelright=False)

plt.text(-80, 110, 'TGA') #adds text wrt to provided x,y axis
plt.text( 650, 110, 'DTG') #adds text wrt to provided x,y axis

z = lambda Temp: residue #define a function that will be assigned to polynomial of experimental data
p = poly.fit(Temp, z(residue),20) # polynomial of experimental data
fit_p = p(Temp) # graph of polynomial of experimental data aka the fit
# plt.plot(Temp,fit_p)

Dfit_p = p.deriv(1) #derivative of polynomial of experimental data
Dfit = Dfit_p(Temp) #graph of derivative of polynomial of experimental data

plt.twinx()
plt.plot(Temp, Dfit, linestyle = ':', c='k')
plt.ylabel(r'd(1-$\alpha$)/dt (%/s)')

space = 0.05
plt.ylim(max(Dfit)+space, min(Dfit)-space)

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=3, 
                bottom=True, top=False, left=False, right=True)

plt.tick_params(which='major', direction='in', length=7, 
                bottom=True, top=False, left=False, right=True)

plt.tick_params(labelbottom=True, labeltop=False,
                labelleft=False, labelright=True)


