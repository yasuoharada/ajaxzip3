#!/usr/bin/env python

# dataフォルダ内の郵便番号データをJSONP形式にしてzipdataフォルダ内に保存します

import glob

for file in glob.glob('data/*.json'):
    print file, '-'*20
    f = open('zipdata/' + file[5:-2], "w")
    f.write("zipfile(")
    for line in open(file, 'r'):
        f.write(line)
    f.write(");\n")
    f.close()

