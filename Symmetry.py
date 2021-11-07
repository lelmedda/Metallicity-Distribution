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

def get_data():
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

   # initialize arrays for the spaxel ID, the objid, and the metallicity quantity
    spaxid=np.asarray([])
    ID = np.asarray([])
    z = np.asarray([])
    
   
    #print('row',rows)
    #print('d',spaxid)
    #print('f',ID )
    #print('e',z )
    
    #   This should select the spaxel ID, the objid, and the metallicity quantity from the database.
    rows = np.asarray(rows)
        
    spaxid=rows[:,0]
    ID = rows[:,1]
    z=rows[:,2].astype(float)


    #print(spaxid)
    #print(ID )
    #print(z )
    return  spaxid, ID, z 

xy = spaxid
symmetric_galaxies = []
d = {}
find_quadrant = {}
count = 0
diff_q = []

def break_spaxels(xy):
    '''
      Split spaxid to two arrays x and y
    '''
    x=np.asarray([])
    y=np.asarray([])
    
    for entry in xy:
        coord=entry.split('_')
        x=np.append(x, float(coord[1]))
        y=np.append(y, float(coord[2]))
        
    return x, y

spaxid, ID, z = get_data()

for i in range(0,len(np.unique(ID))):
    slice_xy=xy[np.where(ID==(np.unique(ID)[i]))]
    slice_z=z[np.where(ID==(np.unique(ID)[i]))]
    sort=slice_xy.argsort()
    sorted_spax=slice_xy[sort]
    sorted_metal=slice_z[sort]
    
    # break_spaxels(xy) use to be here

    x, y = break_spaxels(sorted_spax)
    new_sorted_metal = []

    # Clean data of Nan/ Nonetype values
    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
        else:
            new_sorted_metal = np.append(new_sorted_metal,0)

    sig = 0.999999426696856

    print("(min(x)+ max(x))//2", (min(x)+ max(x))//2)
    print("(max(x)", max(x))
    print("(min(x)", min(x))

    #   Divide into 4 quadrants
    q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]

    #   Make list with non null values only
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

    #   Check whether most values are in the quadrant are non null, if so then increment.
    #   Otherwise disregard the quadrant.
    if len(q1new) > len(q1)//2 and len(q2new) > len(q2)//2:
        if 1-p12 < (sig):
            count = count + 1
            diff_q.append("q1 and 2 are different")
    if len(q1new) > len(q1)//2 and len(q3new) > (len(q3)//2):
        if 1-p13 < (sig):
            count = count + 1
            diff_q.append("q1 and 3 are different")
    if len(q1new) > len(q1)//2 and len(q4new) > len(q4)//2:
        if 1-p14 < (sig):
            count = count + 1
            diff_q.append("q1 and 4 are different")
    if len(q2new) > len(q2)//2 and len(q3new) > (len(q3)//2):
        if 1-p23 < (sig):
            count = count + 1
            diff_q.append("q2 and 3 are different")
    if len(q2new) > len(q2)//2 and len(q4new) > len(q4)//2:
        if 1- p24 < (sig):
            count = count + 1
            diff_q.append("q2 and 4 are different")
    if len(q4new) > len(q4)//2 and len(q3new) > (len(q3)//2):
        if 1-p34 < (sig):
            count = count + 1
            diff_q.append("q3 and 4 are different")

    # Saver count
    d[np.unique(ID)[i]] = count

    # Reset count for next galaxy
    count = 0

    find_quadrant[np.unique(ID)[i]] = diff_q

plt.hist(d.values(), bins = 'rice', histtype='stepfilled', color='blue')
plt.xlabel('inconsistant quadrants')
plt.ylabel("Number of galaxies")
plt.title('Galaxies symmetry')
savefig('Galaxies symmetry_test.pdf', bbox_inches='tight')
show()
