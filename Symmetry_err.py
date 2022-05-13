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
from scipy.stats import sem



def get_quadrants_center(new_sorted_metal, x, y):
    '''
    Divide into 4 quadrants

        q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
        q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
        q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
        q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]

    '''
    # should this actually be a minus or +
    q1 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q2 = new_sorted_metal[np.where((x < (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    q3 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y > (min(y)+max(y))//2))]
    q4 = new_sorted_metal[np.where((x > (min(x)+ max(x))//2) & (y < (min(y)+max(y))//2))]
    return q1, q2, q3, q4

def get_quadrants_BL(new_sorted_metal, x, y):
    '''
    Center is Bottom Right
    '''
    q1 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    q2 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    q3 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y > ( (min(y)+max(y) )//2 ) -1 ))]
    q4 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    # print("(min(x)+ max(x))//2)", (min(x)+ max(x))//2))
    # print(" max(x)", max(x))
    # print(" min(x)", min(x))
    return q1, q2, q3, q4

def get_quadrants_BR(new_sorted_metal, x, y):
    '''
    Center is Bottom Right
    '''
    q1 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) +1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    q2 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) +1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    q3 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) +1) & (y > ( (min(y)+max(y) )//2 ) -1 ))]
    q4 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) +1) & (y < ( (min(y)+max(y) )//2 ) -1 ))]
    return q1, q2, q3, q4

def get_quadrants_UL(new_sorted_metal, x, y):
    '''
    Center is Upper Left
    '''
    q1 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    q2 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    q3 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y > ( (min(y)+max(y) )//2 ) +1 ) )]
    q4 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    return q1, q2, q3, q4

def get_quadrants_UR(new_sorted_metal, x, y):
    '''
    Center is Upper Right
    '''
    q1 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    q2 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    q3 = new_sorted_metal[ np.where( (x < ( (min(x)+ max(x) )//2 ) -1) & (y > ( (min(y)+max(y) )//2 ) +1 ) )]
    q4 = new_sorted_metal[ np.where( (x > ( (min(x)+ max(x) )//2 ) -1) & (y < ( (min(y)+max(y) )//2 ) +1 ) )]
    return q1, q2, q3, q4

def get_quad(center, x,y,new_sorted_metal):
    # Takes in quad_center_pt
    # returns quadrants
    if center == 'C':
        q1, q2, q3, q4 = get_quadrants_center(new_sorted_metal, x, y)
        #count = get_count(q1, q2, q3, q4)
        #inconsistant_quads['C'] = count
    if center == 'BL':
        q1, q2, q3, q4 = get_quadrants_BL(new_sorted_metal, x, y)
        #count = get_count(q1, q2, q3, q4)
        #inconsistant_quads['BL'] = count
    if center == 'BR':
        q1, q2, q3, q4 = get_quadrants_BR(new_sorted_metal, x, y)
        #count = get_count(q1, q2, q3, q4)
        #inconsistant_quads['BR'] = count
    if center == 'UL':
        q1, q2, q3, q4 = get_quadrants_UL(new_sorted_metal, x, y)
        #count = get_count(q1, q2, q3, q4)
        #inconsistant_quads['UL'] = count
    if center == 'UR':
        q1, q2, q3, q4 = get_quadrants_UR(new_sorted_metal, x, y)
    return q1, q2, q3, q4

def get_count_list(x,y,new_sorted_metal):
    sig = 0.999999426696856
    inc_quad_list  = ['C', 'BL', 'BR', 'UL', 'UR']
    count_list = []
    for quad in inc_quad_list:
        # Reset count for next quadrants
        count = 0

        print("quad", quad)

        # get quadrant, use it
        # get 2nd quadrant and use it, ...
        # save counts related to each quadrant in order of inc_quad_list.
        # such as center is 0, Bottom Left is 1, etc ...
        q1, q2, q3, q4 = get_quad(quad, x,y,new_sorted_metal)
        #print("q1, q2, q3, q4 ", q1, q2, q3, q4 )

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
                #diff_q.append("q1 and 2 are different")
        if len(q1new) > len(q1)//2 and len(q3new) > (len(q3)//2):
            if 1-p13 < (sig):
                count = count + 1
                #diff_q.append("q1 and 3 are different")
        if len(q1new) > len(q1)//2 and len(q4new) > len(q4)//2:
            if 1-p14 < (sig):
                count = count + 1
                #diff_q.append("q1 and 4 are different")
        if len(q2new) > len(q2)//2 and len(q3new) > (len(q3)//2):
            if 1-p23 < (sig):
                count = count + 1
                #diff_q.append("q2 and 3 are different")
        if len(q2new) > len(q2)//2 and len(q4new) > len(q4)//2:
            if 1- p24 < (sig):
                count = count + 1
                #diff_q.append("q2 and 4 are different")
        if len(q4new) > len(q4)//2 and len(q3new) > (len(q3)//2):
            if 1-p34 < (sig):
                count = count + 1
                #diff_q.append("q3 and 4 are different")

        print("count",count)
        #
        # Saver all 5 counts in count_list
        count_list.append(count)
        print("count_list",count_list)

    return count_list

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


#print('row',rows)
#print('d',spaxid)
#print('f',ID )
#print('e',z )


spaxid=rows[:,0]
ID = rows[:,1]
z=rows[:,2].astype(float)


#print(spaxid)
#print(ID )
#print(z )

xy = spaxid
symmetric_galaxies = []
d = {}
find_quadrant = {}
count = 0
#diff_q = []

print('len(np.unique(ID))', len(np.unique(ID)))
# e count used for printing when testing
e = 0
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

    # Clean data of Nan/ Nonetype values
    new_sorted_metal = []
    for entryy in sorted_metal:
        if np.isfinite(entryy) == True:
            new_sorted_metal = np.append(new_sorted_metal, entryy)
        else:
            new_sorted_metal = np.append(new_sorted_metal,0)

    # Take in spaxels(x,y) and their metallicity

    #print("(min(x)+ max(x))//2", (min(x)+ max(x))//2)
    #print("(max(x)", max(x))
    #print("(min(x)", min(x))
    #print("count",count)

    #   Divide into 4 quadrants
    #q1, q2, q3, q4 = get_quadrants_center(new_sorted_metal, x, y)
    count_list = get_count_list(x,y,new_sorted_metal)

    def get_error(error_counts):
        # calculate standard error of the mean
            # ddof : Degree of freedom correction for Standard Deviation.
        count_error = sem(error_counts)
        return count_error



    # After got all 5 values, save counts of current galaxy_id
    d[np.unique(ID)[i]] = [count_list[0],     get_error(count_list[1:5]), count_list]

    e = e+1

    if e==10:
        break

print("d", d)


    #find_quadrant[np.unique(ID)[i]] = diff_q

#plt.hist(d.values(), bins = 'rice', histtype='stepfilled', color='blue')
#plt.xlabel('inconsistant quadrants')
#plt.ylabel("Number of galaxies")
#plt.title('Galaxies symmetry')
#savefig('Galaxies symmetry_test.pdf', bbox_inches='tight')
#show()
