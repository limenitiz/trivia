import os
from enum import Enum


def consist_of(item, list_items):
    for i in list_items:
        if item.find(i) != -1:
            return True
    return False


def parse_filenames_from_root(root='.', include_words=None, exclude_words=None):
    if include_words is None:
        return None

    if exclude_words is None:
        exclude_words = [__file__]
    else:
        exclude_words.append(__file__)

    listdir = []
    for dp, dn, filenames in os.walk(root):
        for filename in filenames:
            path_from_root = os.path.join(dp, filename)

            if consist_of(path_from_root, include_words) and \
                    not consist_of(path_from_root, exclude_words):
                listdir.append(path_from_root)

    return listdir


class ReadMode(Enum):
    read = 'r'
    read_byte = 'rb'


class WriteMode(Enum):
    write = 'w'
    write_byte = 'wb'
    append = 'a'
    append_byte = 'ab'


def merge_files(filenames, path=os.getcwd(), print_progress=True,
                output_filename='merge_files.txt', encoding='utf-8', file_tag='// @filename',
                read_mode=ReadMode.read, write_mode=WriteMode.append):

    for filename in filenames:
        if print_progress:
            print("\t processing file : ", filename)

        with open(path + "/" + filename, read_mode.value, encoding=encoding) as file, \
                open(path + "/" + output_filename, write_mode.value, encoding=encoding) as new_file:

            new_file.write(file_tag + filename + "\n")

            for line in file:
                new_file.write(line)

            # space between files
            new_file.write("\n\n")


print("\n", "<--    start merge     -->", "\n")
merge_files(parse_filenames_from_root(include_words=['.html', '.css', '.js']))
print("\n", "<-- successfully merge -->", "\n")
