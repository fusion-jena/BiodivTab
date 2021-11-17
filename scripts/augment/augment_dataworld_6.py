from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd

if __name__ == '__main__':
    filename = 'dataworld_6'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = join(realpath('.'), 'data')

    # Unit column
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['name'].to_list()
    unitList = []
    for val in list1:
        if 'mg/kg' in val:
            unitList += ['mg/kg of {}'.format(val.split('_')[1])]
        else:
            unitList += ['N/A']
    df['unit'] = pd.Series(unitList)
    df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)
