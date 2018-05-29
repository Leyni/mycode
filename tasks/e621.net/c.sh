#!/bin/bash

ROOT_PATH='./'

pid=$(cat ${ROOT_PATH}c_token)
if [ $pid -ne 0 ] ;
then
    exit 1
fi

echo $$ > ${ROOT_PATH}c_token

while read line
do
    echo $line
    python e621_parser.py comic $line
done < /var/services/homes/leyni/CloudStation/Drive/Entertain/Picture/source/ComicFurry/list.txt

#cat /dev/null > /var/services/homes/leyni/CloudStation/Drive/Entertain/Picture/source/ComicFurry/list.txt 

echo '0' > ${ROOT_PATH}c_token
