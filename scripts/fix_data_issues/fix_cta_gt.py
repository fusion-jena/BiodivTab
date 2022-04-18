from os.path import join, realpath
import pandas as pd

# Press the green button in the gutter to run the script.
from astropy.modeling._projections import ceas2x

if __name__ == '__main__':
    cta_gt = join(realpath('.'), 'gt', 'CTA_biodivtab_2021_gt.csv')
    df = pd.read_csv(cta_gt, header=None, index_col=None, names=['filename', 'col', 'solution'])
    print(df.head(10))
    solutions = df['solution']
    extra_spaces = 0
    for i, s in enumerate(solutions):
        if ' ' in s:
            print(s)
            extra_spaces+=1
            df.at[i, 'solution'] = s.replace(' ', '')
    print('----------------------------')
    print('{} extra spaces were found and fixed'.format(extra_spaces))
    for i, s in enumerate(solutions):
        df.at[i, 'solution'] = s.replace('https://www.wikidata.org/wiki/', 'https://www.wikidata.org/entity/')

    print(df.head(10))

    df.to_csv('new_cta_gt.csv', index=None, header=None)