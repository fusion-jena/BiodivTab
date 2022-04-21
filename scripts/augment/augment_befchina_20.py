from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random

if __name__ == '__main__':
    filename = 'befchina_20'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = realpath(join(realpath('.'), '..', '..', 'input_data', 'befchina'))

    # append only one true Uni
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Sample.Collector'].to_list()
    new_list = ['{0} ({1})'.format(item, 'University of Halle-Wittenberg') if
                item == 'David Eichenberg' else item for item in list ]

    df['Sample.Collector'] = pd.Series(new_list)

    df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)

    #####################################################################################

    # append another true institue (not exsiting in Wikidata with Chiristian)
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Sample.Collector'].to_list()
    new_list = ['{0} ({1})'.format(item, 'University of Halle-Wittenberg') if
                item == 'David Eichenberg' else item for item in list ]

    new_list = ['{0} ({1})'.format(item, 'German Centre for Integrative Biodiversity Research (iDiv)')
                if
                item == 'Christian Ristok' else item for item in new_list]

    df['Sample.Collector'] = pd.Series(new_list)

    df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)
    #####################################################################################

    # Noisy university Universität Hamburg with Wenzel Kröber
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Sample.Collector'].to_list()
    new_list = ['{0} ({1})'.format(item, 'University of Halle-Wittenberg') if
                item == 'David Eichenberg' else item for item in list]

    new_list = ['{0} ({1})'.format(item, 'German Centre for Integrative Biodiversity Research (iDiv)')
                if
                item == 'Christian Ristok' else item for item in new_list]

    new_list = ['{0} ({1})'.format(item, 'Universität Hamburg')
                if
                item == 'Wenzel Kroeber' else item for item in new_list]

    df['Sample.Collector'] = pd.Series(new_list)

    df.to_excel(join(augmented_path, filename + '_03.xlsx'), encoding='utf-8', index=0)
    #####################################################################################

    # switch focus to University instead of researcher
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Sample.Collector'].to_list()

    new_list = ['{0} - {1}'.format('University of Halle-Wittenberg', item) if
                item == 'David Eichenberg' else item for item in list]

    new_list = ['{0} - {1}'.format('German Centre for Integrative Biodiversity Research (iDiv)', item)
                if item == 'Christian Ristok' else item for item in new_list]

    df['Sample.Collector'] = pd.Series(new_list)

    # df.rename(columns={'Sample.Collector', 'University'}, inplace=True) # NY: renamed that manually
    # df.rename(columns={'Month': 'Year'}, inplace=True)

    df.to_excel(join(augmented_path, filename + '_04.xlsx'), index=0)
    #####################################################################################

    # abbreviate species
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['Species'].to_list()

    new_list = ['{0}. {1}'.format(item.split(' ')[0][0:2], item.split(' ')[1]) for item in list ]
    df['Species'] = pd.Series(new_list)

    df.to_excel(join(augmented_path, filename + '_05.xlsx'), index=0)