from os import mkdir, listdir
from os.path import join, realpath, exists
import pandas as pd
import numpy as np


Round = 'Round 3.3'
Year = '2021'

Results_Path = join(realpath('.'), 'Data_Explore_Results')
Data_Path = join(realpath('.'), 'Data', Year, Round, 'tables')
###############################################################

if not exists(Results_Path):
    mkdir(Results_Path)

def get_attributes(table):
    tab_path = join(Data_Path, table)
    df = pd.read_csv(tab_path)

    df_rows, df_cols = df.shape
    df_cells = df_cols * df_rows
    return df_rows, df_cols, df_cells

if __name__ == '__main__':
    tables = listdir(Data_Path)
    rows, cols, cells = [], [], []
    for table in tables:
        tRows, tCols, tCells = get_attributes(table)
        rows = rows + [tRows]
        cols = cols + [tCols]
        cells = cells + [tCells]

    df = pd.DataFrame(data={'rows':rows, 'cols': cols, 'cells': cells})
    df.to_csv(join(Results_Path, '{0}_{1}_statistics.csv'.format(Year, Round)))

    avgRows = np.average(rows)
    stdRows = np.std(rows)
    print('Rows:', avgRows, '+-', stdRows)

    avgCols = np.average(cols)
    stdCols = np.std(cols)
    print('Cols:', avgCols, '+-', stdCols)

    avgCells = np.average(cells)
    stdCells = np.std(cells)
    print('Cells:', avgCells, '+-', stdCells)



