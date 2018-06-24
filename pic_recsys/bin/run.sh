#!/bin/bash

TOKEN_FILE=$1_token
COMMAND=$2

ROOT_PATH='./etc/'
pid=$(cat ${ROOT_PATH}${TOKEN_FILE})
if [ $pid -ne 0 ] ;
then
    exit 1
fi

echo $$ > ${ROOT_PATH}${TOKEN_FILE}

$COMMAND

echo '0' > ${ROOT_PATH}${TOKEN_FILE}
