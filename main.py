import json
import os
from PIL import Image
from ast import literal_eval as make_tuple

def main():
    with open('config.json') as f:
        config = json.load(f)
        print(config)
    
    dir = r'./pics'
    out = r'./out'
    for filename in os.listdir(dir):
        im = Image.open(os.path.join(dir, filename))

        # Get the size of the image
        width, height = im.size

        for colour_to in config['colour_to']:
            # Process every pixel
            for x in range(width):
                for y in range(height):
                    current_pixel_colour = im.getpixel((x, y))
                    if current_pixel_colour == make_tuple(config['colour_from']):
                        im.putpixel((x, y), make_tuple(colour_to))

            im.save(os.path.join(out, ' '.join([colour_to, filename])))

if __name__ == "__main__":
    main()