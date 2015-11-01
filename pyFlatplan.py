#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
Github      :
description : Build a flatplan from page images, just like a mosaic.
              Could be useful when exporting jpg pages from Adobe InDesign.
              Imagemagick is required to use pyFlatplan. It can be downloaded at www.imagemagick.org

'''


import sys
import re
import argparse
import os


description ="""

Build a flatplan from page images, just like a mosaic.
Could be useful when exporting jpg pages from Adobe InDesign.

Imagemagick is required to use pyFlatplan. It can be downloaded at www.imagemagick.org
"""


# Natural sorting of files not using leading zeros.
# Based on the answer of Mark Byers on StackOverflow.
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)


def main():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-input', nargs='+', required=True, help='Image list or wildcard pattern')
    parser.add_argument('-output', required=False, default='flatplan.jpg', help='output file (default: flatplan.jpg')
    parser.add_argument('-thumb', type=int, required=False, default=256, help='Thumbnail size (default: 256)')
    parser.add_argument('-column', type=int, required=False, default=5, help='Flatplan number of columns  (default: 5)')
    parser.add_argument('-background', required=False, default="#EFFEFFEFF", help='Background color, use double quote marks (default: "#EFFEFFEFF"')

    args = parser.parse_args()

    thumb_size = args.thumb
    nb_columns = args.column
    output_file = args.output
    background_color = args.background

    # fetching the file list ans ordering it naturally
    file_list = natural_sort( args.input)

    image_list_string = ' '.join(file_list)

    cmd = "montage -background '"+ background_color + "' " + image_list_string + " -tile " + str(nb_columns) + "x -geometry " + "x" + str(thumb_size) + "+" + str(int(thumb_size/10)) + "+" + str(int(thumb_size/10)) + " " + output_file

    print("Flatplan inprogress...")

    os.system(cmd)

    print("Done!")


if __name__ == '__main__':
    main()
