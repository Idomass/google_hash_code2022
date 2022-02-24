#! /bin/bash

for file in inputs/*; do
    ./main.py $file
    cp output /mnt/c/Users/idoma/Documents/`basename $file`
done
