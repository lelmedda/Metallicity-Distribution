'''

May be needed:
    # Save  galaxy_id & num_inconsistent_quads @ certain Center in pickle file
    filename = "num_inconsistent_quadrants_{}.pickle".format(center)
    save_into_pickle(d, filename)
'''

def save_into_pickle(dictionary, filename):
    '''
    The following will be saved into file:
            ‘galaxy_id’,
            ‘num_inconsistent_quadrants_center’
    '''
    file_to_write = open(filename, "w")
    pickle.dump(dictionary, file_to_write)
    return

def retreive_from_pickle():
    '''
    retreive this dictionary from pickle file
    '''
    return

def save_all(galaxy_id, inc_quad_list):
    '''
    Create 5 dictionaries where galaxy_id: num_inconsistent_quads
    Center designation will be saved as filename
    '''
    galaxies_classified_C[ inc_quad_list[0]] =  galaxy_cat_list.append(galaxy_id)
    galaxies_classified_UR[ inc_quad_list[1]] =  galaxy_cat_list.append(galaxy_id)
    galaxies_classified_BL[ inc_quad_list[2]] =  galaxy_cat_list.append(galaxy_id)
    galaxies_classified_BR[ inc_quad_list[3]] =  galaxy_cat_list.append(galaxy_id)
    galaxies_classified_UL[ inc_quad_list[4]] =  galaxy_cat_list.append(galaxy_id)
    galaxies_classified = []
    galaxies_classified.extend([galaxies_classified_C, galaxies_classified_UR,
                    galaxies_classified_BL, galaxies_classified_BR, galaxies_classified_UL])
    return galaxies_classified

def classify_galaxies(galaxies_inconsistent_quadrants_count):
    '''
    Input:
        galaxies_inconsistent_quadrants_count[galaxy_id] = number_inconsistent_quadrants
    Output:
        Galaxies_classified[ ‘num_inconsistent_quadrants_C’ ] = galaxy_cat_list
    '''
    galaxies_classified = {}
    total_galaxies_num = len(galaxies_inconsistent_quadrants_count.keys())

    for galaxy_id in galaxies_inconsistent_quadrants_count.keys():
        # if key already encountered, add galaxy to existing list
        # otherwise initialize new list
        if galaxy_id in galaxies_classified.keys():
            inc_quad_list = galaxies_inconsistent_quadrants_count[galaxy_id]
            save_all(galaxy_id, inc_quad_list)
        else:
            galaxy_cat_list = []
            galaxy_cat_list.append(galaxy_id)
            galaxies_classified[ count ] =  galaxy_cat_list.append(galaxy_id)

    return galaxies_classified, total_galaxies_num

def galaxy_classification_percentage(galaxies_classified, total_galaxies_num):
    '''
    Def:
        galaxy_category: from 0 to 6 such that
        0 means the null hypothesis is true
        and 6 that it is false.

    Input:
        Galaxies_classified[ ‘num_inconsistent_quadrants_C’ ] = galaxy_cat_list
    Output:
        fraction_galaxy_cat[‘num_inconsistent_quadrants_C’] = number of galaxies in each galaxy category fomr our sample
    '''
    fraction_galaxy_cat = {}

    # For each number of inconsistent_quadrants, get number of galaxies
    for count in  galaxies_classified.keys():
        num_galaxies = len(galaxies_classified[count])
        percentage = num_galaxies* total_galaxies_num/100
        fraction_galaxy_cat[count] = percentage

    return fraction_galaxy_cat

def plot_percentage(fraction_galaxy_cat):
    # Get data
    galaxy_categories = fraction_galaxy_cat.keys()
    galaxy_percentage = fraction_galaxy_cat.values()
    # Plot figure
    #FIGURE OUT WHAT KIND OF PLT PLOT!
    # google something like : circular percentagge fraction plot
    (galaxy_categories, galaxy_percentage)
    # Save figure
    return

def get_error():
    '''
    Determine how changing the center, changes the null hypothesis
    '''
    # LOOK AT CODE BELOW #Uncertainties in Reasearch Tracker
    # for each center, plot the distribution
    # for each galaxy,
        # save the number of category it belongs to depending on center point used
    return

def main():

        #   Get number of inconsistent quadrants foreach galaxy

    galaxies_inconsistent_quadrants_count = get_galaxies_inconsistent_quadrants_count()
    print("galaxies_inconsistent_quadrants_count", galaxies_inconsistent_quadrants_count)

        #
    #galaxies_classified, total_galaxies_num = classify_galaxies(galaxies_inconsistent_quadrants_count)
    #print("galaxies_classified", galaxies_classified)
    #fraction_galaxy_cat = galaxy_classification_percentage(galaxies_classified, total_galaxies_num)
    #print("fraction_galaxy_cat", fraction_galaxy_cat)
    #plot_percentage(fraction_galaxy_cat)

main()
