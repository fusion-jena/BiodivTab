from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random

if __name__ == '__main__':
    filename = 'befchina_1'

    augmented_path = join(realpath('.'), 'augmented',filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = join(realpath('.'), 'data')



    # change month into Year + changing format
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Month'].to_list()
    new_list = ['{0} ({1})'.format(item.split('_')[1],item.split('_')[0]) for item in list]

    df['Month'] = pd.Series(new_list)
    df.rename(columns={'Month': 'Year'}, inplace=True)

    df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)

    #####################################################################################
    # set focus on the month again with different format
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Month'].to_list()
    new_list = ['{0} ({1})'.format(item.split('_')[1],item.split('_')[0]) for item in list]

    df['Month'] = pd.Series(new_list)

    df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    #####################################################################################
    # random drops
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Planted_Species'].to_list()
    ln = len(list)

    # set 50% of the cells into Unknown (increase knowledge gab)
    for _ in range(int(ln / 2)):
        i = random.randint(0, ln-1)
        list[i] = 'Unknown Species'

    df['Planted_Species'] = pd.Series(list)
    df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)
    # print(df.head(5))
