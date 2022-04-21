from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random
import calendar

def insert_rand_char(word):
    wLn = len(word)
    ins_i = random.randint(0, wLn - 1)
    # to be insterted = ascii(a), ascii(z)
    char = chr(random.randint(ord('a'), ord('z')))
    return word[:ins_i] + char + word[ins_i + 1:]


def delete_rand_char(word):
    wLn = len(word)
    del_i = random.randint(0, wLn - 1)
    return word[:del_i] + word[del_i + 1:]


def get_month(number):
    return calendar.month_name[number]

def set_NIL_values(list, portion=0.5, NIL_value='N/A'):
    ln = len(list)
    for _ in range(int(portion *  ln)):
        i = random.randint(0, ln - 1)
        list[i] = NIL_value
    return list

if __name__ == '__main__':
    filename = 'Bexis-24867_2_data'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = realpath(join(realpath('.'), '..', '..', 'input_data', 'bexis'))

    # # change headers
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # df.rename(columns={'latitude': 'lat', 'longitude': 'long', 'soli_type': 'type', 'soil_temperature_change': 'soli_temp'}, inplace=True)
    # df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)
    #
    # # Unknown soil_type 50%
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['soil_type'].to_list()
    # list1 = set_NIL_values(list1)
    # df['soil_type'] = pd.Series(list1)
    # df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    # spelling mistakes in soil_type and unknown column
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['soil_type'].to_list()
    for i, val in enumerate(list1):
        if i % 2 == 0:
            val = delete_rand_char(val)
            val = insert_rand_char(val)
            # val = insert_rand_char(val)
        list1[i] = val
    df['soil_type'] = pd.Series(list1)
    df.rename( columns={'soil_type': 'col1'}, inplace=True)
    df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)



