from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random

if __name__ == '__main__':
    filename = 'dataworld_1'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = join(realpath('.'), 'data')

    # drop the scientific name col 1 and keep the annotations from common name (col 0)
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # df.drop(labels='scientific_name', inplace=True, axis=1)
    # df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)

    ############################################################################################
    # keep only common name (sample with one column)
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # ser = df['species_common_name']
    # new_df = pd.DataFrame(ser)
    # new_df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    ############################################################################################
    # # taxon class col 2 - 70% unknowns and keep the common name huge knowledge gap
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list = df['taxonclass'].to_list()
    # ln = len(list)
    #
    # for _ in range(int(0.75 *  ln)):
    #     i = random.randint(0, ln - 1)
    #     list[i] = 'Unknown Class'
    #
    # df['taxonclass'] = pd.Series(list)
    # df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)
    ############################################################################################
    # append common_name and scientific_name in one column
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['species_common_name'].to_list()
    list2 = df['scientific_name'].to_list()
    newList = ['{0},{1}'.format(i1, i2) for i1,i2 in zip(list1, list2)]
    df['species_common_name'] = pd.Series(newList)
    df.rename(columns={'species_common_name': 'species'}, inplace=True)
    df.drop(labels='scientific_name', axis=1, inplace=True)
    df.to_excel(join(augmented_path, filename + '_04.xlsx'), index=0)

    ############################################################################################
    # append scientific name and taxon class in the same column
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['scientific_name'].to_list()
    # list2 = df['taxonclass'].to_list()
    # newList = ['{0},{1}'.format(i1, i2) for i1,i2 in zip(list1, list2)]
    # df['scientific_name'] = pd.Series(newList)
    # df.rename(columns={'scientific_name': 'species'}, inplace=True)
    # df.drop(labels='taxonclass', axis=1, inplace=True)
    # df.to_excel(join(augmented_path, filename + '_05.xlsx'), index=0)

    ############################################################################################
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['scientific_name'].to_list()
    # list2 = df['taxonclass'].to_list()
    # newList = ['{0},{1}'.format(i2, i1) for i1,i2 in zip(list1, list2)]
    # df['scientific_name'] = pd.Series(newList)
    # df.rename(columns={'scientific_name': 'taxon_class'}, inplace=True)
    # df.drop(labels='taxonclass', axis=1, inplace=True)
    # df.to_excel(join(augmented_path, filename + '_06.xlsx'), index=0)
    ############################################################################################

    # [Manual] create a duplicate CEA mappings for the common name (col 0)
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    df.to_excel(join(augmented_path, filename + '_07.xlsx'), index=0)