#!/bin/bash

ROOT_PATH='./'

pid=$(cat ${ROOT_PATH}d_token)
if [ $pid -ne 0 ] ;
then
    exit 1
fi

echo $$ > ${ROOT_PATH}d_token

python e621_parser.py download
#tail -f ${ROOT_PATH}e621_parser.log

echo '0' > ${ROOT_PATH}d_token
