#!/bin/bash

ROOT_PATH='/Users/kongfanyang/Documents/Sync/Entertain/picture/'

pid=$(cat ${ROOT_PATH}p_token)
if [ $pid -ne 0 ] ;
then
    exit 1
fi

echo $$ > ${ROOT_PATH}p_token

python e621_parser.py preview
#tail -f ${ROOT_PATH}e621_parser.log

echo '0' > ${ROOT_PATH}p_token

