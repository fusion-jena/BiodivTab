from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
import random


def set_NIL_values(list, portion=0.5, NIL_value='N/A'):
    ln = len(list)
    for _ in range(int(portion *  ln)):
        i = random.randint(0, ln - 1)
        list[i] = NIL_value
    return list

if __name__ == '__main__':
    filename = 'dataworld_10 (4)'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = realpath(join(realpath('.'), '..', '..', 'input_data', 'data.world'))

    # too sparse table
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['superkingdom'].to_list()
    newList = set_NIL_values(list1,portion=0.5, NIL_value='undetermined')
    df['superkingdom'] = pd.Series(newList)

    list1 = df['phylum'].to_list()
    newList = set_NIL_values(list1, portion=0.5, NIL_value='undetermined')
    df['phylum'] = pd.Series(newList)

    list1 = df['class'].to_list()
    newList = set_NIL_values(list1, portion=0.5, NIL_value='undetermined')
    df['class'] = pd.Series(newList)

    list1 = df['order'].to_list()
    newList = set_NIL_values(list1, portion=0.5, NIL_value='N/A')
    df['order'] = pd.Series(newList)

    list1 = df['family'].to_list()
    newList = set_NIL_values(list1, portion=0.7, NIL_value='N/A')
    df['family'] = pd.Series(newList)

    list1 = df['genus'].to_list()
    newList = set_NIL_values(list1, portion=0.7, NIL_value='N/A')
    df['genus'] = pd.Series(newList)

    df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)
