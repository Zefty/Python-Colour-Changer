import pandas as pd 
from tqdm import tqdm
import os
from PIL import Image, ImageColor
from ast import literal_eval as make_tuple
COLOR_FROM = '#000000'

def main():
    # Load colours 
    colours = pd.read_csv('colours.csv')
    print('Processing the following colours ...')
    print(colours)
    
    # Set directory paths 
    dir = r'./pics'
    out = r'./out'

    for filename in os.listdir(dir):
        print('Processing {} with the above colours, please wait ...'.format(filename))
        filenameSplit = filename.split('.')

        for _, r in tqdm(colours.iterrows(), total = len(colours.index)):
            # Get the size of the image
            im = Image.open(os.path.join(dir, filename))
            width, height = im.size
            # Process every pixel
            for x in range(width):
                for y in range(height):
                    current_pixel_colour = im.getpixel((x, y))
                    if current_pixel_colour == ImageColor.getcolor(COLOR_FROM, "RGB"):
                        im.putpixel((x, y), ImageColor.getcolor(r['Hex'], "RGB"))

            im.save(os.path.join(out, ' '.join([filenameSplit[0], 'in', r['Name']]) + '.' + filenameSplit[1]))

if __name__ == "__main__":
    main()