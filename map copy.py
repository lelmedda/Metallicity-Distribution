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
print(len(rows))

#This should select the spaxel ID, the objid, and the metallicity quantity from the database.

ID = []
xy = []
yy = []
z = []
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

for i in range(0,2):
	slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
	slice_z=z[np.where(ID==(np.unique(ID)[i]))]

	#sort the spaxel ids (this sorts by x/y position)
	sort=slice_xy.argsort()
	sorted_spax=slice_xy[sort]
	sorted_metal=slice_z[sort]
	print(len(sorted_spax))
	#split out the spaxels into their own lists (I think I did this for you? - break spaxels is a function I wrote, but I think your x y coordinates should work if you replace them)
	#x, y = break_spaxels(all_spaxels[numpy.where(objid_oh == '587724240159834264')])
	def break_spaxels(xy):
		x=np.asarray([])
		y=np.asarray([])
		for entry in xy:
			coord=entry.split('_')
			x=np.append(x, float(coord[0]))
			y=np.append(y, float(coord[1]))
		return x, y
	x, y = break_spaxels(sorted_spax)
	print(min(x), max(x), min(y), max(y))
	print(len(x), len(y), len(sorted_metal))
	print(type(x))
	#Set up a zeroed array with dimensions one larger than the maximum in x & y
	fullmask = np.zeros((int(max(x)+1.0), int(max(y)+1.0)))
	print(np.shape(fullmask))
	#For every object in that galaxy, assign the metallicity to its location in the zeroed array (this is fast)
	for index, entry in enumerate(sorted_metal):
		#print x[index], (y[index])
		fullmask[int(x[index])][int(y[index])]=entry
	#extent = [x[0],x[1],y[0],y[1]]
	#print out for checking
	print(fullmask[np.where(fullmask>0.0)])
	print(np.shape(fullmask))
	extent = [min(x), max(x), min(y), max(y)]
	#Imshow works!
	imshow(fullmask, extent = extent, vmin=min(sorted_metal), vmax=max(sorted_metal))
	colorbar()
	show()
	savefig('data_plot_'+str(np.unique(ID)[i]+'_'))
