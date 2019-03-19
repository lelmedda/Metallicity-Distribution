# Dicerne types of galaxies
#2 not/or almost independent parts
#normal round ones
#point like very small we can take the yellow part as the center
#use python shape identification and calculate of center of mass
#For more standard shapes: Divide the hexagone to 4 parts, if most of the galaxy is dominated by yellow pixels, and there's an area of low metallicity(blue) disregard it
#Take a point of reference and find the center of mass
#Center depending on mass or center white area
#There's ones with the white not shaped like hexagone
#include the closest point to the edge

import numpy as np
import matplotlib
from pylab import *
import warnings
import mysql.connector as sql
import datetime
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

print(datetime.datetime.now().time())
db = sql.connect(host="localhost",user="loubna", password="10ubn4", database="sdss")
c = db.cursor()
cmd='''SELECT spaxID, objID, KE08 FROM dr14_metallicities'''
try:
    c.execute(cmd)
    rows= c.fetchall() #Fetch all (remaining) rows of a query result, returning them as a list of tuples.
except:
    pass
db.close()
print(datetime.datetime.now().time())
#print(len(rows))

#This should select the spaxel ID, the objid, and the metallicity quantity from the database.
spaxid=np.asarray([])
ID = np.asarray([])
z = np.asarray([])
rows = np.asarray(rows)

spaxid=rows[:,0]
ID = rows[:,1]
z=rows[:,2].astype(float)
xy = spaxid
avg_list = []
med_list = []
g={}

for i in range(0, len(np.unique(ID))):
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
            	#sort the spaxel ids (this sorts by x/y position)
    sorted_metal=slice_z#slice_z[sort]
    new_sorted_metal = sorted_metal[np.where(np.isfinite(sorted_metal) == True)]
    if len(new_sorted_metal) != 0:
        avg = np.average(new_sorted_metal, axis=None, weights=None, returned=False)
        med = np.median(new_sorted_metal,axis=None, out=None, overwrite_input=False, keepdims=False)
    avg_list.append(avg)
    med_list.append(med)
    g[ID[i]]= avg,med
galaxiesID = g.keys()
print(galaxiesID)
print(datetime.datetime.now().time())

plt.hist(avg_list, bins = 'rice', alpha = 0.3, linestyle='--' , histtype='step',color='black', linewidth= 4, label='average metallicity')
plt.hist(med_list, bins = 'rice', histtype='step', color='blue', label='median metallicity')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')
plt.ylabel('Number of Galaxies')
plt.xlabel('Metallicity')
plt.title('Distribution of metallicity')
savefig('metallicity_avg_med'+[i]+'.pdf', bbox_inches='tight')
show()
