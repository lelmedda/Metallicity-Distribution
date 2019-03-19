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

#from pdf2image import convert_from_path
#newpic = convert_from_path('data_plot_588017979448754350.pdf', 500)
#from PIL import Image
#im = Image.open(newpic)

#croppedim = im.crop((335,435,565,560))

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

    #slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
    #print('slice_xy',slice_xy)
            	#sort the spaxel ids (this sorts by x/y position)
    #sort=slice_xy.argsort()
    #sorted_spax=slice_xy[sort]
    sorted_metal=slice_z#slice_z[sort]
    #print("should be same galaxy:YES!",slice_xy)
    #print('z of same galaxy:yes!',slice_z)
    #print(sort)
    #print(len(sorted_metal))
        	#split out the spaxels into their own lists (I think I did this for you? - break spaxels is a function I wrote, but I think your x y coordinates should work if you replace them)
        	#x, y = break_spaxels(all_spaxels[numpy.where(objid_oh == '587724240159834264')])

    # def break_spaxels(xy):
    # #    print(xy)
    #     x=np.asarray([])
    #     y=np.asarray([])
    #
    #     for entry in xy:#NOT LOOOPING
    #         coord=entry.split('_')
    #         x=np.append(x, float(coord[1]))
    #         y=np.append(y, float(coord[2]))
    # #        print("entry",entry)
    # #        print(x)
    # #        print(y)
    #     return x, y
    #
    # x, y = break_spaxels(sorted_spax)

    new_sorted_metal = sorted_metal[np.where(np.isfinite(sorted_metal) == True)]
    #for entryy in sorted_metal:
    #    if np.isfinite(entryy) == True:
        #    new_sorted_metal = np.append(new_sorted_metal, entryy)
        #else:
        #    new_sorted_metal = np.append(new_sorted_metal, 0)

    #center = ((min(x)+ max(x))//2, (min(y)+max(y))//2)
    #print(center)
    #if x<min(x) and y<min(y): #use .where()      #ware function
    # I expect to see RuntimeWarnings in this block
    #with warnings.catch_warnings():
        #warnings.simplefilter("ignore", category=RuntimeWarning)
        #warnings.warn("Mean of empty slice.", RuntimeWarning)
    #print(new_sorted_metal)
    if len(new_sorted_metal) != 0:
        avg = np.average(new_sorted_metal, axis=None, weights=None, returned=False)
        med = np.median(new_sorted_metal,axis=None, out=None, overwrite_input=False, keepdims=False)
    #if len(new_sorted_metal) == 0:
    #    avg = 0
    #    med = 0
    avg_list.append(avg)
    med_list.append(med)
    g[ID[i]]= avg,med
galaxiesID = g.keys()
print(galaxiesID)
print(datetime.datetime.now().time())

#avg_listt = np.nda ray.tolist(avg_list)
#med_listt = np.ndarray.tolist(med_list)
#x = np.arange(10)
#bins_ = np.histogram_bin_edges(a, bins=10, range=None, weights=None)

#hist,bins=numpy.histogram(avd)
#plt.hist(x+0.8,med_list, histtype='step')
#plt.bar(bins[:-1], hist, width=(bins[-1]-bins[-2]), align="edge")

plt.hist(avg_list, bins = 'rice', alpha = 0.3, linestyle='--' , histtype='step',color='black', linewidth= 4, label='average metallicity')
plt.hist(med_list, bins = 'rice', histtype='step', color='blue', label='median metallicity')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')
plt.ylabel('Number of Galaxies')
plt.xlabel('Metallicity')
plt.title('Distribution of metallicity')
savefig('metallicity_avg_med'+[i]+'.pdf', bbox_inches='tight')
#ax.set_xticklabels(galaxiesID, rotation = 45, ha="right")
#ax.set_xticks(avg_list)
show()
#objectid = np.ndarray.tolist(ID)

#data_dist = []
#for id in range(0,len(objectid)):
#    objectid[id] = str(objectid[id])
#    for value in range(0,len(avg_list)):
#        for value2 in range(0,len(med_list)):
#                data_dist.append((objectid[id],avg_list[value],med_list[value2]))
#print("here")
#print(datetime.datetime.now().time())
#connection = sql.connect(host="localhost",user="loubna", password="10ubn4", database="sdss")
#cursor = connection.cursor()
#data = data_dist
#sql_insert_query = ( "INSERT INTO met_dist (title,average,median) "
#                 "VALUES (%s, %s, %s)"
#)
#data = data_dist

#cursor.executemany(sql_insert_query,data)
#connection.commit()
#print ("Record inserted successfully into python_users table")

#cursor.close()
#connection.close()
#print(datetime.datetime.now().time())
#import webbrowser
#pdf = webbrowser.open_new(r'file://C:\Documents\Research\Loubna\data_plot_588017979448754350.pdf.pdf')
#print(pdf)
