#!/bin/bash
dirpath=$1
cd "$dirpath/comments/"
for i in {0..5}
do
        espeak -s 200 -g 12 -f $i.txt --stdout  | ffmpeg -i - -ar 44100 -ac 2 -ab 192k -f mp3 $i.mp3
        time=$(mp3info -p "%S" $i.mp3)
        echo $time
        ffmpeg -y -framerate 1/$time -start_number 0 -i $dirpath/images/$i.png -i $i.mp3 -vf 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1' -c:v libx264 -r 25 -pix_fmt yuv420p -c:a aac -strict experimental -shortest -max_muxing_queue_size 9999 $dirpath/videos/$i.mp4
done

cd $dirpath/title
espeak -s 200 -g 12 -f title.txt --stdout | ffmpeg -i - -ar 44100 -ac 2 -ab 192k -f mp3 title.mp3
time=$(mp3info -p "%S" title.mp3)
ffmpeg -y -framerate 1/$time -start_number 1 -i title.png -i title.mp3 -vf 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1' -c:v libx264 -r 25 -pix_fmt yuv420p -c:a aac -strict experimental -shortest -max_muxing_queue_size 9999 $dirpath/videos/title.mp4

cd $dirpath/videos/
ffmpeg -f concat -i inputs.txt -c copy output.mp4
