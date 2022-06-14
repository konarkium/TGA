import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

# %% detecting file
filename = 'tga.csv'
for f in os.listdir(r'C:/Users/konar/.spyder-py3'):
    if f == filename:
        print('the file exists')
        break
    else:
        print('file not found')
        
# %%
df = pd.read_csv(filename) #grab data

damp = 1000 #affects the smoothness of graph, useful for derivatives

x1 = df['Time']
damp_x1 = x1[::damp] #damped

x2 = df['Temp']
damp_x2 = x2[::damp] #damped

y1 = df['m']

#calculating residue content
wi = y1[0] #initial sample weight
wr = y1[len(y1)-1] #final residue weight
y2 = 100-(((wi-y1)/(wi-wr))*100) # #residue = 100 - %conversion
damp_y2 = y2[::damp] #damped

damp_y2_diff = np.diff(damp_y2) # using NumPy function to find difference 
damp_x1_diff = np.diff(damp_x1) # between damped elements 

damp_y3 = damp_y2_diff/damp_x1_diff # 1st derivative of mass w.r.t. time
damp_y3 = np.append(damp_y3,0) # number of elements on both axes should be equal
damp_y3 = -damp_y3 # just following the convention

#%%

#Prepare multipanel plot 
fig = plt.figure(1, figsize=(5, 11))
#prepare grid
gs = gridspec.GridSpec(10,5)
#determine gap dimentions
gs.update(hspace=0.0005)

#%% TGA
xtr_subplot = fig.add_subplot(gs[0:5,0:5])
plt.plot(x2,y2, label='resin',c='black')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=False, top=False, left=True, right=False)

plt.tick_params(which='major', direction='in', length=10, 
                bottom=False, top=False, left=True, right=False)

plt.tick_params(labelbottom=True, labeltop=False,
                labelleft=True, labelright=False)
plt.ylabel(r'1-$\alpha$ (%)')

#%% DTG
xtr_subplot = fig.add_subplot(gs[5:10,0:5])
plt.plot(damp_x2,damp_y3, label='resin',c='black')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(labelbottom=True, labeltop=False,
                labelleft=True, labelright=False)

plt.xlabel('Temperature ($^o$C)')
plt.ylabel(r'd(1-$\alpha$)/dt (%/s)')

plt.legend()

plt.savefig('tga.png', dpi=300,bbox_inches="tight")
