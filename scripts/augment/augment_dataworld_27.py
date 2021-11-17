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

if __name__ == '__main__':
    filename = 'dataworld_27'

    augmented_path = join(realpath('.'), 'augmented', filename)
    if not exists(augmented_path):
        makedirs(augmented_path)

    data_path = join(realpath('.'), 'data')

    # # merge animal_type and sex_upon_outcome
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['sex_upon_outcome'].to_list()
    # list2 = df['animal_type'].to_list()
    # newList = []
    # for sex, type in zip(list1, list2):
    #     if sex == 'Unknown':
    #         newList += [type]
    #     else:
    #         newList += [sex + " " + type]
    # df['animal_type'] = pd.Series(newList)
    # df.to_excel(join(augmented_path, filename + '_01.xlsx'), index=0)
    #
    # # Noise to merged animal_type and sex_upon_outcome
    # df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    # list1 = df['sex_upon_outcome'].to_list()
    # list2 = df['animal_type'].to_list()
    # newList = []
    # for sex, type in zip(list1, list2):
    #     if sex == 'Unknown':
    #         newList += [type]
    #     else:
    #         newList += [sex + " " + type]
    #
    # # apply noise here
    # for i, val in enumerate(newList):
    #     if len(val) > 5 and i % 2 == 0:
    #         val = delete_rand_char(val)
    #         val = insert_rand_char(val)
    #         val = insert_rand_char(val)
    #     newList[i] = val
    # df['animal_type'] = pd.Series(newList)
    # df.to_excel(join(augmented_path, filename + '_02.xlsx'), index=0)

    # Noise to merged animal_type and sex_upon_outcome and the stand alone sex_upon_outcome
    df = pd.read_excel(join(data_path, filename, filename + '.xlsx'))
    list1 = df['sex_upon_outcome'].to_list()
    list2 = df['animal_type'].to_list()
    newList = []
    for sex, type in zip(list1, list2):
        if sex == 'Unknown':
            newList += [type]
        else:
            newList += [sex + " " + type]

    # apply noise here
    for i, val in enumerate(newList):
        if len(val) > 5 and i % 2 == 0:
            val = delete_rand_char(val)
            val = insert_rand_char(val)
            val = insert_rand_char(val)
        newList[i] = val
    df['animal_type'] = pd.Series(newList)

    # apply noise to sex_upon_outcome
    sex_newList = []
    for i, val in enumerate(list1):
        if len(val) > 5 and i % 2 == 0:
            val = delete_rand_char(val)
            val = insert_rand_char(val)
            val = insert_rand_char(val)
        sex_newList += [val]
    df['sex_upon_outcome'] = pd.Series(sex_newList)
    df.to_excel(join(augmented_path, filename + '_03.xlsx'), index=0)