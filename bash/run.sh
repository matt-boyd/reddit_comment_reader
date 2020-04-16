#!/bin/bash
dirpath=Enter your full directory path here
python3 $dirpath/python/get_sources.py
bash $dirpath/bash/textToSpeech.sh $dirpath
bash $dirpath/bash/yt-uploader.sh $dirpath
bash $dirpath/bash/cleanup.sh $dirpath
