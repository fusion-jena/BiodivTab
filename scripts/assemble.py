from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd

if __name__ == '__main__':
    tables_path = join(realpath('.'), 'assembled', 'tables')
    targets_path = join(realpath('.'), 'assembled', 'targets')
    gt_path = join(realpath('.'), 'assembled', 'gt')
    if not exists(targets_path):
        makedirs(targets_path)
    if not exists(tables_path):
        makedirs(tables_path)
    if not exists(gt_path):
        makedirs(gt_path)

    data_path = join(realpath('.'), 'reconciled')
    filenames = listdir(data_path)
    print(filenames)

    df_cea = None
    df_cta = None

    df_gt_cea = None
    df_gt_cta = None

    for filename in filenames:
        # make tables
        df = pd.read_excel(join(data_path, filename, filename+'.xlsx'))
        print (df.head(5))

        df.to_csv(join(tables_path, filename+'.csv'), index=0)

        # make cea targets
        df_current_cea = pd.read_excel(join(data_path, filename, filename + '_CEA.xlsx'), header=None,
                                       usecols=[0,1,2], skiprows=1)
        print(df_current_cea.head(5))

        if df_cea is None:
            df_cea = df_current_cea
        else:
            df_cea = df_cea.append(df_current_cea, ignore_index=True)

        # make cta targets
        df_current_cta = pd.read_excel(join(data_path, filename, filename + '_CTA.xlsx'), header=None,
                                       usecols=[0, 1], skiprows=1)
        if df_cta is None:
            df_cta = df_current_cta
        else:
            df_cta = df_cta.append(df_current_cta, ignore_index=True)

        # make cea gt
        df_current_gt_cea = pd.read_excel(join(data_path, filename, filename + '_CEA.xlsx'), header=None,
                                       usecols=[0, 1, 2, 4], skiprows=1)
        print(df_current_gt_cea.head(5))

        if df_gt_cea is None:
            df_gt_cea = df_current_gt_cea
        else:
            df_gt_cea = df_gt_cea.append(df_current_gt_cea, ignore_index=True)

        # make cta gt
        df_current_gt_cta = pd.read_excel(join(data_path, filename, filename + '_CTA.xlsx'), header=None,
                                       usecols=[0, 1, 2], skiprows=1)
        print(df_current_gt_cta.head(5))

        if df_gt_cta is None:
            df_gt_cta = df_current_gt_cta
        else:
            df_gt_cta = df_gt_cta.append(df_current_gt_cta, ignore_index=True)

    # write targets
    df_cea.to_csv(join(targets_path, 'CEA_biodivtab_2021_Targets.csv'), index=0)
    df_cta.to_csv(join(targets_path, 'CTA_biodivtab_2021_Targets.csv'), index=0)

    # write gt
    df_gt_cea.to_csv(join(gt_path, 'CEA_biodivtab_2021_gt.csv'), index=0)
    df_gt_cta.to_csv(join(gt_path, 'CTA_biodivtab_2021_gt.csv'), index=0)

    # create json of CTA ancestors
    # load CTA gt, pick solution column
    # hit wikidata proxy to retrieve P31 with weight = 1
    # hit wikidata proxy to retrieve P279 with weight = 2
    # create a dictionary as CTA 2T tables

