#!/bin/bash

mysql -uleyni -p -e "select rec_status,count(*) as cnt from pic_rec.sample_e621_set group by rec_status;;select label_status, count(1) as cnt from pic_rec.sample_e621_set group by label_status;"
