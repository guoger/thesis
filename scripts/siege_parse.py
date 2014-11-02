#!/bin/python
import sys

def extract_value(key, filename):
    """ find the value according to the key string in the file """
    f = open(filename, 'r')
    concurrencies = []
    values = []
    for line in f:
        # if line.startswith('==='):
        #     concurrencies.append(int(line.split()[1]))
        if line.startswith('** Pre'):
            concurrencies.append(int(line.split()[2]))
        elif line.startswith(key):
            for element in line.split():
                try:
                    val = float(element)
                    values.append(val)
                except ValueError:
                    pass

    f.close()
    return (concurrencies, values)

if __name__=="__main__":
    a,b = extract_value('Longest', "odroid_apache_small_text")
    print a
    print b
