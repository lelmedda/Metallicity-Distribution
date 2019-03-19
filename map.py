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
#print(len(rows))

#This should select the spaxel ID, the objid, and the metallicity quantity from the database.
spaxid=np.asarray([])
ID = np.asarray([])
z = np.asarray([])
rows = np.asarray(rows)

spaxid=rows[:,0]
ID = rows[:,1]
z=rows[:,2].astype(float)

#print(shape(spaxid))

#print(len(ID))
#with open('starter_metallicities.csv','r') as csvfile:
#	plot = csv.reader(csvfile,delimiter=',')
#	for row in plot:
#		ID.append((str(row[0])))
#		xy.append(str(row[1])+'_'+str(row[2]))
		#yy.append(str(row[2]))
#		z.append(float(row[3]))
#ID = np.array(ID)
#xy = np.array(xy)
#yy = np.array(yy)
#z = np.array(z)
#x = np.reshape(xx,(3,789))
#y = np.reshape(yy,(3,789))
#z = np.reshape(z,(3,789))
#loading in the data
#spaxid_oh=x[:,0].astype(str)
#objid_oh=y[:,1].astype(str)
#metallicity=z[:,2].astype(float)
#print(np.where(ID==(np.unique(ID)[0]))[0])
xy = spaxid

for i in range(0,len(np.unique(ID))):
    #print('xy',xy)
    #print(np.shape(xy))
    #print('unique',np.unique(ID, axis=0))
    slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
    #print('slice_xy',slice_xy)
            	#sort the spaxel ids (this sorts by x/y position)
    sort=slice_xy.argsort()
    sorted_spax=slice_xy[sort]
    sorted_metal=slice_z[sort]
    #print("should be same galaxy:YES!",slice_xy)
    #print('z of same galaxy:yes!',slice_z)
    #print(sort)
    #print(len(sorted_metal))
        	#split out the spaxels into their own lists (I think I did this for you? - break spaxels is a function I wrote, but I think your x y coordinates should work if you replace them)
        	#x, y = break_spaxels(all_spaxels[numpy.where(objid_oh == '587724240159834264')])
    def break_spaxels(xy):
    #    print(xy)
        x=np.asarray([])
        y=np.asarray([])

        for entry in xy:#NOT LOOOPING
            coord=entry.split('_')
            x=np.append(x, float(coord[1]))
            y=np.append(y, float(coord[2]))
    #        print("entry",entry)
    #        print(x)
    #        print(y)
        return x, y

    x, y = break_spaxels(sorted_spax)

    #print(min(x), max(x), min(y), max(y))
    #print(len(x), len(y), len(sorted_metal))

    #print(type(x))
        	#Set up a zeroed array with dimensions one larger than the maximum in x & y

    fullmask = np.zeros((int(max(x)+1.0), int(max(y)+1.0)))
    #print(np.shape(fullmask))

        	#For every object in that galaxy, assign the metallicity to its location in the zeroed array (this is fast)

    new_sorted_metal = []
    for index, entry in enumerate(sorted_metal):
        #new_sorted_metal = np.delete(sorted_metal, index)
        #new_sorted_metal= np.where(entry is None,new_sorted_metal,np.append(new_sorted_metal,sorted_metal[index])) #Delete Nonetype
        #

    #    print(index,'***',entry)
        fullmask[int(x[index])][int(y[index])]= entry

    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
    #NoneList = np.isfinite(sorted_metal)
    #print(NoneList)
            #anp.delete(arr, [0,2,4], axis=0)
    #        print('oooo',iindex)
    #print('newwortedmetal',new_sorted_metal)
    #print(type(sorted_metal[0]))
    #print('testing isfinite', len(sorted_metal[np.where(sorted_metal >0.0)]))
        	#extent = [x[0],x[1],y[0],y[1]]
        	#print out for checking
    #print(fullmask[np.where(fullmask > 0.0)])
    #print(np.shape(fullmask))
    extent = [min(x), max(x), min(y), max(y)]
        	#Imshow works!
    #if len(new_sorted_metal):

        imshow(fullmask, extent = extent,vmin=min(new_sorted_metal), vmax=max(new_sorted_metal))
        colorbar()
        savefig('data_plot_'+str(np.unique(ID)[i])+'.pdf')
        close()
        #show()
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
