from os.path import join, realpath, exists
from os import listdir, makedirs
import pandas as pd
from random import randrange
import random

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

if __name__ == '__main__':
    filename = 'dataworld_2'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = join(realpath('.'), 'data')

    # # merge airport_name & aircraft_airline_operator ==> airport_name
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['airport_name'].to_list()
    # list2 = df['aircraft_airline_operator'].to_list()
    # newList = ['{0},{1}'.format(i1, i2) for i1,i2 in zip(list1, list2)]
    # df['airport_name'] = pd.Series(newList)
    # df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)
    ############################################################################################
    # # merge aircraft_airline_operator & airport_name ==> aircraft_airline_operator
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['airport_name'].to_list()
    # list2 = df['aircraft_airline_operator'].to_list()
    # newList = ['{0},{1}'.format(i2, i1) for i1, i2 in zip(list1, list2)]
    # df['aircraft_airline_operator'] = pd.Series(newList)
    # df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    ############################################################################################
    # More N/A for Us states origin_state
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list = df['origin_state'].to_list()
    # ln = len(list)
    #
    # for _ in range(int(0.5 *  ln)):
    #     i = random.randint(0, ln - 1)
    #     list[i] = 'N/A'
    #
    # df['origin_state'] = pd.Series(list)
    # df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)

    ############################################################################################
    # Append US or United States to origin_state
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list = df['origin_state'].to_list()
    #
    # list = ["{} (United States)".format(i) for i in list ]
    #
    # df['origin_state'] = pd.Series(list)
    # df.to_excel(join(augmented_path, filename + '_04.xlsx'), index=0)
    ############################################################################################
    # Noise to origin_state (randomly insert char and delete char)
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list = df['origin_state'].to_list()

    newList = []
    for i, word in enumerate(list):
        newWord = word
        try:
            if len(word) > 2 and i % 2 == 0:
                newWord = delete_rand_char(newWord)
                newWord = insert_rand_char(newWord)
            newList += [newWord]
        except:
            newList += ['N/A']
            continue

    df['origin_state'] = pd.Series(newList)
    df.to_excel(join(augmented_path, filename + '_05.xlsx'), index=0)

