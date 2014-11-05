#!/bin/bash

import sys
import csv
import matplotlib.pyplot as plt

def parse_val(filename, key):
    vals = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=' ', skipinitialspace=True)
        for item in reader:
            vals.append(int(item[key]))

    return vals

def plot_cpu_rpi(filename):
    sy = parse_val(filename, 'sy')
    us = parse_val(filename, 'us')

    #print us, sy
    total = [x + y for x, y in zip(sy, us)]
    x = range(0, len(sy))

    fig, ax = plt.subplots() 
    ax.stackplot(x, sy, us, colors=('red', 'green'))
    #ax.plot(x, total)
    #ax.fill_between(x, sy, total, color='g')
    #ax.fill_between(x, sy, 0, color='r')
    ax.set_ylabel('CPU usage (%)')
    ax.set_ylim([0, 100])
    ax.set_xlim([0, 71])
    ax.set_title('CPU usage of Raspberry Pi during Siege test')
    fig.savefig('output/cpusage_rpi.png')

def plot_cpu_odroid(filename):
    sy = parse_val(filename, 'sy')
    us = parse_val(filename, 'us')

    #print us, sy
    total = [x + y for x, y in zip(sy, us)]
    x = range(0, len(sy))

    fig, ax = plt.subplots() 
    ax.stackplot(x, sy, us, colors=('red', 'green'))
    #ax.plot(x, total)
    #ax.fill_between(x, sy, total, color='g')
    #ax.fill_between(x, sy, 0, color='r')
    ax.set_ylabel('CPU usage (%)')
    ax.set_xlim([0, 71])
    ax.set_ylim([0, 100])
    ax.set_title('CPU usage of Odroid during Siege test')
    fig.savefig('output/cpusage_odr.png')

def main():
    #plot_cpu('cluster/cpu-db')
    plot_cpu_odroid('cluster/cpu-php')

if __name__=="__main__":
    main()
