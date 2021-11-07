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
    '''
        Get the following rows from database:
        paxID, objID, KE08 FROM dr14_metallicities
    
    '''
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
    
    #   This should select the spaxel ID, the objid, and the metallicity quantity from the database.
    rows = np.asarray(rows)
    spaxid=rows[:,0]
    ID = rows[:,1]
    z=rows[:,2].astype(float)
    
    return  spaxid, ID, z 


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

def get_center(new_sorted_metal,x,y):
    '''
        Divide into 4 quadrants
    '''
    
    # should this actually be a minus or +
    q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))] 
    
    '''
    # can I/ should I leave the same and then add the -1 to each term
    # print("(min(x)+ max(x))//2)", (min(x)+ max(x))//2))
    # print(" max(x)", max(x))
    # print(" min(x)", min(x))
    q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))] 
    '''
    
    return q1, q2, q3, q4

def clean_data(sorted_metal):
  '''
     Clean data of Nan/ Nonetype values
  '''
    new_sorted_metal = []
    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
        else:
            new_sorted_metal = np.append(new_sorted_metal,0)
    return new_sorted_metal 

def get_count(q1, q2, q3, q4):
     '''
     If most quadrants data are non null,
       & check distribution and update count accordingly,
     Otherwise disregard the quadrant.
    '''
    
     #   Make list with non null values only
     #   to get number of null values in each quadrant
    q1new = q1[np.where(q1 > 0)]
    # too see change of what's going on here print(q1new )
    q2new = q2[np.where(q2 > 0)]
    q3new = q3[np.where(q3 > 0)]
    q4new = q4[np.where(q4 > 0)]

    #   Get k and p value of each quadrant
    ks12, p12 = stats.ks_2samp(q1, q2)
    ks13, p13 = stats.ks_2samp(q1, q3)
    ks14, p14 = stats.ks_2samp(q1, q4)
    ks23, p23 = stats.ks_2samp(q2, q3)
    ks24, p24 = stats.ks_2samp(q2, q4)
    ks34, p34 = stats.ks_2samp(q3, q4)
    
    if len(q1new) > len(q1)//2 and len(q2new) > len(q2)//2:
        if 1-p12 < (sig):
            count = count + 1
           # diff_q.append("q1 and 2 are different")
    if len(q1new) > len(q1)//2 and len(q3new) > (len(q3)//2):
        if 1-p13 < (sig):
            count = count + 1
          #  diff_q.append("q1 and 3 are different")
    if len(q1new) > len(q1)//2 and len(q4new) > len(q4)//2:
        if 1-p14 < (sig):
            count = count + 1
           # diff_q.append("q1 and 4 are different")
    if len(q2new) > len(q2)//2 and len(q3new) > (len(q3)//2):
        if 1-p23 < (sig):
            count = count + 1
         #   diff_q.append("q2 and 3 are different")
    if len(q2new) > len(q2)//2 and len(q4new) > len(q4)//2:
        if 1- p24 < (sig):
            count = count + 1
        #    diff_q.append("q2 and 4 are different")
    if len(q4new) > len(q4)//2 and len(q3new) > (len(q3)//2):
        if 1-p34 < (sig):
            count = count + 1
          #  diff_q.append("q3 and 4 are different")
    return count

def plot(d):
    '''
        Plot count 
    '''
    plt.hist(d.values(), bins = 'rice', histtype='stepfilled', color='blue')
    plt.xlabel('inconsistant quadrants')
    plt.ylabel("Number of galaxies")
    plt.title('Galaxies symmetry')
    savefig('Galaxies symmetry_test.pdf', bbox_inches='tight')
    show()

def main():
    #   Get data
    spaxid, ID, z = get_data()

    #   Initialize main variables
    sig = 0.999999426696856
    xy = spaxid
    symmetric_galaxies = []
    d = {}
    find_quadrant = {}
    count = 0
    diff_q = []
    
    # Get count of each galaxy
    for i in range(0,len(np.unique(ID))):
        slice_xy = xy[np.where(ID==(np.unique(ID)[i]))]
        slice_z = z[np.where(ID==(np.unique(ID)[i]))]
        
        # find indices of sorted array
        sort_ind = slice_xy.argsort()
        
        # sort spaxels and metalicities arrays
        sorted_spax = slice_xy[sort_ind]            
        sorted_metal = slice_z[sort_ind]
        
        # get coordonates of spax & metalicities
        x, y = break_spaxels(sorted_spax)
        metal_arr = clean_data(sorted_metal)
       
       # Get 4 quadrants 
        q1, q2, q3, q4 = get_center(metal_arr, x, y)
        # print(q1)

        #  Get num quadrants belonging to the same sample distribution
        count = get_count(q1, q2, q3, q4)

        # Save number of consistent quadrants in the galaxy
        # and reset count for next galaxy
        d[np.unique(ID)[i]] = count
        count = 0

       # find_quadrant[np.unique(ID)[i]] = diff_q
    
     # Save dict to CSV file 
        
        # ADD CSV CODE HERE
        
     # Plot 
     #plot(d)
        

