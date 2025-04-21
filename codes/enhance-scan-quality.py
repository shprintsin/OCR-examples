import os
import subprocess

# the command:  "magick image.jpeg  -resize 200%  -auto-level  -threshold 70%  output1.png"
# need to install magick on path
INPUT_PATH='images/'
OUTPUT_DIR='output/'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
# need to check quality by tweeking the threshold
for file in os.listdir('images'):
    input_file = os.path.join(INPUT_PATH, file)
    output_file= os.path.join(OUTPUT_DIR, file)
    subprocess.run(['magick',INPUT_PATH'-resize', '200%', '-auto-level', '-threshold', f'68%', output_file])
    print(f"Processed {input_file} to {output_file}")
