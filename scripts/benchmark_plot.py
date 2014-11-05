#!/bin/bash

import sys
import siege_parse as sp
import matplotlib.pyplot as plt

def odroid_small_plot():
    c1, t1 = sp.extract_value('Transactions',
            'odroid/odroid_apache_small_text')
    c2, t2 = sp.extract_value('Transactions', 'odroid/odroid_nginx_small_text')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=3,label="Apache")
    ax.plot(c2,t2,'b',linewidth=3,label="Nginx")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Web server test by Transfering small file on Odroid')
    fig.savefig('output/odroid_small_text.png')

def odroid_big_plot():
    c1, t1 = sp.extract_value('Transactions', 'odroid/odroid_apache_big_jpg')
    c2, t2 = sp.extract_value('Transactions', 'odroid/odroid_nginx_big_jpg')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=3,label="Apache")
    ax.plot(c2,t2,'b',linewidth=3,label="Nginx")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Web server test by Transfering big file on Odroid')
    fig.savefig('output/odroid_big_jpg.png')

def rpi_small_plot():
    c1, t1 = sp.extract_value('Transactions', 'rpi/rpi_apache_small_text')
    c2, t2 = sp.extract_value('Transactions', 'rpi/rpi_nginx_small_text')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=3,label="Apache")
    ax.plot(c2,t2,'b',linewidth=3,label="Nginx")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Web server test by Transfering small file on Raspberry Pi')
    fig.savefig('output/rpi_small_text.png')

def rpi_big_plot():
    c1, t1 = sp.extract_value('Transactions', 'rpi/rpi_apache_big_jpg')
    c2, t2 = sp.extract_value('Transactions', 'rpi/rpi_nginx_big_jpg')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=3,label="Apache")
    ax.plot(c2,t2,'b',linewidth=3,label="Nginx")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Web server test by Transfering large file on Raspberry Pi')
    fig.savefig('output/rpi_big_jpg.png')

def simple_php():
    c1, t1 = sp.extract_value('Transactions', 'rpi/simple_php')
    c2, t2 = sp.extract_value('Transactions', 'odroid/simple_php')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=3,label="RPI")
    ax.plot(c2,t2,'b',linewidth=3,label="ODROID")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Benchmark of simple PHP processing')
    fig.savefig('output/simple_php.png')

def moodle_index():
    c1, t1 = sp.extract_value('Transactions', 'odroid/moodle_index')
    c2, t2 = sp.extract_value('Availability', 'odroid/moodle_index')
    #c2, t2 = sp.extract_value('Response', 'odroid/moodle_index')
    c2 = [c-5 for c in c1]
    fig, ax_trans = plt.subplots()
    ax_trans.plot(c1,t1,'r',linewidth=3,label="Transactions")
    #ax.plot(c2,t2,'b',label="ODROID")
    #ax_trans.legend(loc=7)
    ax_trans.set_xlabel('Level of Concurrency')
    ax_trans.set_ylabel('# of Transactions')
    for l in ax_trans.get_yticklabels():
        l.set_color('r')

    ax_avail = ax_trans.twinx()
    ax_avail.bar(c2,t2,width=5,color='b',alpha=0.4)
    #ax_avail.plot(c1,t2,'|',label="Availability")
    #ax_avail.hist2d(x=c1,y=t2)
    ax_avail.set_ylabel('Availability (%)')
    for l in ax_avail.get_yticklabels():
        l.set_color('b')

    ax_trans.set_title('Moodle index page PHP processing on Odroid')
    fig.savefig('output/moodle_index.png')

def moodle_index_2():
    c1, t1 = sp.extract_value('Transaction ', 'odroid/moodle_index')
    c2, t2 = sp.extract_value('Response', 'odroid/moodle_index')
    #c2, t2 = sp.extract_value('Response', 'odroid/moodle_index')
    c2 = [c-5 for c in c1]
    c1 = [c-10 for c in c1]

    fig, ax_trans = plt.subplots()
    ax_avail = ax_trans.twinx()


    ax_trans.bar(c1,t1,width=5,color='r')
    ax_trans.set_xlabel('Level of Concurrency')
    ax_trans.set_ylabel('Transaction Rate (trans/sec)')
    for l in ax_trans.get_yticklabels():
        l.set_color('r')

    ax_avail.bar(c2,t2,width=5,color='b')
    ax_avail.set_ylabel('Average Response Time (sec)')
    for l in ax_avail.get_yticklabels():
        l.set_color('b')

    ax_trans.set_title('Moodle index page PHP processing on Odroid')
    fig.savefig('output/moodle_index_2.png')

def simple_php_max_res():
    c1, t1 = sp.extract_value('Longest', 'rpi/simple_php')
    c2, t2 = sp.extract_value('Longest', 'odroid/simple_php')
    c2 = [c-3 for c in c1]
    c1 = [c-6 for c in c1]
    fig, ax = plt.subplots()

    ax.bar(c1,t1,color='r',width=3,label="RPI")
    ax.bar(c2,t2,color='b',width=3,label="ODROID")
    ax.legend(loc=3)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('Response Time (sec)')
    ax.set_title('Benchmark of simple PHP processing')
    ax.set_ylim([0, 35])
    fig.savefig('output/simple_php_max_res.png')

def moodle_index_standalone_and_phpalone():
    c1, t1 = sp.extract_value('Transactions', 'odroid/standalone')
    c2, t2 = sp.extract_value('Transactions', 'odroid/moodle_index')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=2,label="standalone")
    ax.plot(c2,t2,'b',linewidth=2,label="PHP only")
    ax.legend(loc=7)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Odroid as a standalone server and PHP server')
    ax.set_ylim([0,1500])
    fig.savefig('output/standalone.png')
    
def moodle_index_cluster():
    c1, t1 = sp.extract_value('Transactions', 'odroid/standalone')
    c2, t2 = sp.extract_value('Transactions', 'cluster/2-php-server')
    #c3, t3 = sp.extract_value('Transactions', 'cluster/cluster-121')
    #c4, t4 = sp.extract_value('Transactions', 'cluster/3-php-server')
    fig, ax = plt.subplots()
    ax.plot(c1,t1,'r',linewidth=2,label="Standalone Installation")
    ax.plot(c2,t2,'b',linewidth=2,label="MySQL in Odroid (2 PHP server)")
    #ax.plot(c3,t3,'g',linewidth=2,label="MySQL in Raspberry Pi (2 PHP server)")
    #ax.plot(c4,t4,'y',linewidth=2,label="cluster3php")
    
    ax.legend(loc=0)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('# of Transactions')
    ax.set_title('Cluster capacity with Multiple PHP server')
    ax.set_ylim([0,2500])
    fig.savefig('output/clever_cluster.png')
    
def moodle_index_res():
    c1, t1 = sp.extract_value('Response', 'odroid/standalone')
    c2, t2 = sp.extract_value('Response', 'odroid/moodle_index')
    c2 = [c-3 for c in c1]
    c1 = [c-6 for c in c1]
    fig, ax = plt.subplots()

    ax.bar(c1,t1,color='r',width=3,label="standalone")
    ax.bar(c2,t2,color='b',width=3,label="PHP only")
    ax.legend(loc=0)
    ax.set_xlabel('Level of Concurrency')
    ax.set_ylabel('Response Time (sec)')
    ax.set_title('Odroid as a standalone server and PHP server')
    ax.set_ylim([0, 12])
    fig.savefig('output/standalone_res.png')


def main():
    #odroid_small_plot()
    #odroid_big_plot()
    #rpi_small_plot()
    #rpi_big_plot()
    #simple_php()
    #moodle_index()
    #moodle_index_2()
    #simple_php_max_res()
    #moodle_index_standalone_and_phpalone()
    #moodle_index_res()
    moodle_index_cluster()

if __name__=="__main__":
    main()
