import csv
import sys


def import_csv():
    dict0 = []
    print("sysver:", sys.version)
    if sys.version >= '3':
        with open('lexique.csv', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                dict0.append(row)
    else:
        with open('lexique.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                dict0.append(row)

    # dict1 = sorted(dict0, key=lambda x: float(x['8_freqlemlivres']), reverse=True)
    # for r in dict1:
        # print(r['1_ortho'] + " " + r['3_lemme'] + " " + r['8_freqlemlivres'])

    return dict0

