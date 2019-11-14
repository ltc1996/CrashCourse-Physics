# -*- coding: UTF-8 -*-
__author__ = 'ltc1996'
__date__ = '2019-11-14'
__version__ = '1.0'

import os


def ass2txt(filename):
    """
    change the order of the filename and .ass -> .txt
    :param filename:  str
    :return: str
    """
    file_split = filename.split('#')
    # print(file_split)
    num = file_split[1][: -4]
    num = '0' * (len(num) < 2) + num
    suf = file_split[0].split('-')[:: -1]
    suf[0] = ' '.join([i for i in suf[0].split(' ') if i])
    # print(suf, num)
    des_file = "{} #{} {}.txt".format(suf[0], num, suf[1])
    return des_file


def convert(filename):
    """
    read the .ass file, delete the timeline and font info, et al.
    then write the translation to a .txt named after this .ass
    :param filename: [str]
    :return: NONE
    """
    des_file = ass2txt(filename)
    fo = open(des_file, 'w', encoding='UTF-8')
    with open(filename, 'r', encoding='UTF-8', errors='ignore') as file_to_convert:
        lines = file_to_convert.readlines()
        for line in lines:
            if '翻译' in line or '批注' in line:
                continue
            if line[: 8] == 'Dialogue':
                fo.write(line[47:] + '\n' * ('ch,,' in line))
        fo.close()
        print("{} is done".format(filename))


def main():
    cur_dir = os.getcwd()
    file_to_convert = []
    # size_to_convert = 0
    for root, dirs, files in os.walk(cur_dir):
        for file in files:
            if file.lower().endswith('.ass'):
                file_to_convert.append(file)
                # size_to_convert = os.path.getsize(file)
    for file in file_to_convert:
        convert(file)
    print('All Done')


if __name__ == '__main__':
    main()
