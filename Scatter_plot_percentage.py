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
from scipy import stats
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
#This should select the spaxel ID, the objid, and the metallicity quantity from the database.
spaxid=np.asarray([])
ID = np.asarray([])
z = np.asarray([])
rows = np.asarray(rows)
spaxid=rows[:,0]
ID = rows[:,1]
z=rows[:,2].astype(float)
xy = spaxid
symmetric_galaxies = []
d = {}
find_quadrant = {}
count12 = 0
count13 = 0
count14 = 0
count23 = 0
count24 = 0
count34 = 0
diff_q = []

for i in range(0,len(np.unique(ID))):
    slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
    sort=slice_xy.argsort()
    sorted_spax=slice_xy[sort]
    sorted_metal=slice_z[sort]
    def break_spaxels(xy):
        x=np.asarray([])
        y=np.asarray([])
        for entry in xy:
            coord=entry.split('_')
            x=np.append(x, float(coord[1]))
            y=np.append(y, float(coord[2]))
        return x, y
    x, y = break_spaxels(sorted_spax)
    new_sorted_metal = []
    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
        else:
            new_sorted_metal = np.append(new_sorted_metal,0)
    q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    sig = 0.999999426696856
    q1new = q1[np.where(q1 > 0)]
    q2new = q2[np.where(q2 > 0)]
    q3new = q3[np.where(q3 > 0)]
    q4new = q4[np.where(q4 > 0)]
    ks12, p12 = stats.ks_2samp(q1, q2)
    ks13, p13 = stats.ks_2samp(q1, q3)
    ks14, p14 = stats.ks_2samp(q1, q4)
    ks23, p23 = stats.ks_2samp(q2, q3)
    ks24, p24 = stats.ks_2samp(q2, q4)
    ks34, p34 = stats.ks_2samp(q3, q4)
    if len(q1new) > len(q1)//2 and len(q2new) > len(q2)//2:
        if 1-p12 < (sig):
            count12 = count12 + 1
            diff_q.append("q1 and 2 are different")
    if len(q1new) > len(q1)//2 and len(q3new) > (len(q3)//2):
        if 1-p13 < (sig):
            count13 = count13 + 1
            diff_q.append("q1 and 3 are different")
    if len(q1new) > len(q1)//2 and len(q4new) > len(q4)//2:
        if 1-p14 < (sig):
            count14 = count14 + 1
            diff_q.append("q1 and 4 are different")
    if len(q2new) > len(q2)//2 and len(q3new) > (len(q3)//2):
        if 1-p23 < (sig):
            count23 = count23 + 1
            diff_q.append("q2 and 3 are different")
    if len(q2new) > len(q2)//2 and len(q4new) > len(q4)//2:
        if 1- p24 < (sig):
            count24 = count24 + 1
            diff_q.append("q2 and 4 are different")
    if len(q4new) > len(q4)//2 and len(q3new) > (len(q3)//2):
        if 1-p34 < (sig):
            count34 = count34 + 1
            diff_q.append("q3 and 4 are different")
list_x = []
list_y = []
list_x = ['1-2','1-3','3-4','2-4','1-4','2-3']

count12=(count12/2700)*100
count13=(count13/2700)*100
count14=(count14/2700)*100
count23= (count23/2700)*100
count24 = (count24/2700)*100
count34 =(count34/2700)*100

list_y=[count12,count13,count14,count23,count24,count34]

plt.scatter(list_x,list_y)
plt.xlabel('comparison quadrants')
plt.ylabel("% of galaxies > 5 sigma ")
plt.title('Galaxies symmetry')
savefig('Galaxies_percent_quadrants.pdf', bbox_inches='tight')
show()
