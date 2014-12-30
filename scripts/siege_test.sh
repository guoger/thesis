#!/bin/bash

# Usage: ./siege_test.sh target_url output_file

if [ -e $2 ]
then
    rm $2
fi

for i in 10 20 40 60 80 100 120 140 160 180 200
do
    echo Concurrency: $i
    echo == $i >> $2
    siege -b -t1m -c$i $1 &>> $2
    echo Stop, sleep for 120s
    #sleep 10
    #echo Restart php-fpm
    #ssh root@192.168.100.2 'service php5-fpm restart'
    sleep 120
    #echo restart apache server
    #ssh root@10.0.2.1 'service apache2 restart'
done

echo Done!!!
