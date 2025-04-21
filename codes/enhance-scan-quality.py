import os
import subprocess
import sys
# "magick image.jpeg  -resize 200%  -auto-level  -threshold 70%  output1.png"
# need to checl quality by tweeking the threshold
for file in os.listdir('images'):
    subprocess.run(['magick','images/'+file, '-resize', '200%', '-auto-level', '-threshold', f'68%', f'output/{file}.png'])
    print(f'output/{file}.png')
