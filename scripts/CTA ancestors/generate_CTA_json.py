from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
import json
if __name__ == '__main__':
    df = pd.read_excel(join(realpath('.'), 'CTA_types' , 'CTA_unique_types.xlsx'), header=0)
    types = df['types'].to_list()
    flat_types = []
    for t in types:
        current_types = t.split(',')
        for ct in current_types:
            flat_types += [ct]


    # make the flat_types as keys in the dict
    cta = {}
    [cta.update({t:{}}) for t in flat_types]

    with open(join(realpath('.'), 'CTA_types' , 'CTA_biodivtab_WD_gt_ancestor.json'), 'w') as file:
        json.dump(cta, file, indent=6)

