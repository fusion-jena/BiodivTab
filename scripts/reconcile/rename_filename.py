from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
import uuid

if __name__ == '__main__':
    data_path = join(realpath('.'), 'data')
    filenames = listdir(data_path)
    # print(filenames)

    for filename in filenames:

        new_filename = str(uuid.uuid4().hex)

        reconsuled_data_path = join(realpath('.'), 'reconciled', new_filename)
        if not exists(reconsuled_data_path):
            makedirs(reconsuled_data_path)

        try:
            # make tables
            df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
            # print(df.head(5))

            df.to_excel(join(reconsuled_data_path, new_filename + '.xlsx'), index=0)

            # make cea targets
            df_current_cea = pd.read_excel(join(data_path, filename, filename + '_CEA.xlsx'), header=0,
                                           usecols=[0, 1, 2, 3, 4, 5])
            oldlst = df_current_cea['filename'].to_list()
            oldlst = [new_filename for filename in oldlst]
            df_current_cea['filename'] = pd.Series(oldlst)

            df_current_cea.to_excel(join(reconsuled_data_path, new_filename + '_CEA.xlsx'), index=0)

            # print(df_current_cea.head(5))

            df_current_cta = pd.read_excel(join(data_path, filename, filename + '_CTA.xlsx'), header=0,
                                           usecols=[0, 1, 2, 3])

            oldlst = df_current_cta['filename'].to_list()
            oldlst = [new_filename for filename in oldlst]
            df_current_cta['filename'] = pd.Series(oldlst)

            # print(df_current_cea.head(5))

            df_current_cta.to_excel(join(reconsuled_data_path, new_filename + '_CTA.xlsx'), index=0)
        except KeyError:
            print(filename)
            break