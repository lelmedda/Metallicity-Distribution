import csv
import numpy as np
import matplotlib
from pylab import *

import mysql.connector as sql
import datetime


print(datetime.datetime.now().time())
db = sql.connect(host="localhost",user="loubna", password="10ubn4", database="sdss")
c = db.cursor()
cmd='''SELECT spaxID, objID, KE08 FROM dr14_metallicities'''
try:
    c.execute(cmd)
    rows= c.fetchall()
except:
    pass
db.close()
print(datetime.datetime.now().time())

#This should select the spaxel ID, the objid, and the metallicity quantity from the database.
spaxid=np.asarray([])
ID = np.asarray([])
z = np.asarray([])
rows = np.asarray(rows)
spaxid=rows[:,0]
ID = rows[:,1]
z=rows[:,2].astype(float)
xy = spaxid

for i in range(0,len(np.unique(ID))):
    slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
            	#sort the spaxel ids (this sorts by x/y position)
    sort=slice_xy.argsort()
    sorted_spax=slice_xy[sort]
    sorted_metal=slice_z[sort]
        	#split out the spaxels into their own lists (I think I did this for you? - break spaxels is a function I wrote, but I think your x y coordinates should work if you replace them)
        	#x, y = break_spaxels(all_spaxels[numpy.where(objid_oh == '587724240159834264')])
    def break_spaxels(xy):
        x=np.asarray([])
        y=np.asarray([])

        for entry in xy:
            coord=entry.split('_')
            x=np.append(x, float(coord[1]))
            y=np.append(y, float(coord[2]))
        return x, y

    x, y = break_spaxels(sorted_spax)
        	#Set up a zeroed array with dimensions one larger than the maximum in x & y
    fullmask = np.zeros((int(max(x)+1.0), int(max(y)+1.0)))
        	#For every object in that galaxy, assign the metallicity to its location in the zeroed array (this is fast)
    new_sorted_metal = []
    for index, entry in enumerate(sorted_metal):
        fullmask[int(x[index])][int(y[index])]= entry

    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
    extent = [min(x), max(x), min(y), max(y)]
        imshow(fullmask, extent = extent,vmin=min(new_sorted_metal), vmax=max(new_sorted_metal))
        colorbar()
        savefig('data_plot_'+str(np.unique(ID)[i])+'.pdf')
        close()
print(p12)
    print(1-p12)
    print(sig)
    if 1-p12 < (sig):
        print("q1 and 2 are different")
    else:
        print("q1 and 2 are the same")
    if 1-p13 < (sig):
        print("q1 and 3 are different")
    else:
        print("q1 and 3 are the same")
    if 1-p14 < (sig):
        print("q1 and 4 are different")
    else:
        print("q1 and 4 are the same")
    if 1-p23 < (sig):
        print("q2 and 3 are different")
    else:
        print("q2 and 3 are the same")
    if 1- p24 < (sig):
        print("q2 and 4 are different")
    else:
        print("q2 and 4 are the same")
    if 1-p34 < (sig):
        print("q3 and 4 are different")
    else:
        print("q3 and 4 are the same")
