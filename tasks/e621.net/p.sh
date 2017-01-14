#!/bin/bash

python e621_parser.py preview &

ROOT_PATH='/Users/kongfanyang/Documents/Sync/Entertain/picture/'
tail -f ${ROOT_PATH}e621_parser.log
