#!/bin/bash
dirpath=$1
source <(cat $dirpath/configuration/config.ini | $dirpath/configuration/config_parser.py)
title=$(cat $dirpath/title/title.txt | sed 's/[][]//g')
youtube-upload --title="$title" --client-secrets=${youtube[client_secret]} $dirpath/videos/output.mp4 
