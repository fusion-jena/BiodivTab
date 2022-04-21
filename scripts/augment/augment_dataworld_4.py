from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random
import calendar


def get_month(number):
    return calendar.month_name[number]


def get_month_abbr(number):
    return calendar.month_abbr[number]


if __name__ == '__main__':
    filename = 'dataworld_4'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = realpath(join(realpath('.'), '..', '..', 'input_data', 'data.world'))

    # correct River name (use full name)
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['hucname'].to_list()
    newList = []
    for river in list1:
        if river in ['Cumberland', 'Kentucky', 'Big Sandy', 'Potomac', 'Kanawha', 'Monongahela', 'Allegheny'
            , 'Delaware', 'Susquehanna', 'Chowan -']:
            river += ' River'
        newList += [river]
    df['hucname'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)

    # fix longitude and latitude names
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    df.rename(columns={'lat_dd': 'latitude', 'lon_dd': 'longitude'}, inplace=True)
    df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    # append species and genus -> species
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['species'].to_list()
    list2 = df['genus'].to_list()
    newList = ['{0},{1}'.format(i1, i2) for i1, i2 in zip(list1, list2)]
    df['species'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)

    # append genus and species -> genus
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['species'].to_list()
    list2 = df['genus'].to_list()
    newList = ['{0},{1}'.format(i2, i1) for i1, i2 in zip(list1, list2)]
    df['genus'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_04.xlsx'), index=0)

    # append month and year -> Month
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['month'].to_list()
    list2 = df['year'].to_list()
    newList = ['{0}-{1}'.format(i1, i2) for i1, i2 in zip(list1, list2)]
    df['month'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_05.xlsx'), index=0)

    # append year and month -> year
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['month'].to_list()
    list2 = df['year'].to_list()
    newList = ['{0}/{1}'.format(i2, get_month(i1)) for i1, i2 in zip(list1, list2)]
    df['year'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_06.xlsx'), index=0)

    # abbreviate month and year -> Month
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['month'].to_list()
    list2 = df['year'].to_list()
    newList = ['{0}-{1}'.format(get_month_abbr(i1), i2) for i1, i2 in zip(list1, list2)]
    df['month'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_07.xlsx'), index=0)

    # abbreviate species A.xxx
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['species'].to_list()
    newList = ['{}.{}'.format(item.split(' ')[0][0], item.split(' ')[1]) for item in list1]
    df['species'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_08.xlsx'), index=0)

    # Unknown genus 50%
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['genus'].to_list()
    ln = len(list1)

    for _ in range(int(0.5 * ln)):
        i = random.randint(0, ln - 1)
        list1[i] = 'Unknown Genus'

    df['genus'] = pd.Series(list1)
    df.to_excel(join(augmented_path, filename + '_09.xlsx'), index=0)
