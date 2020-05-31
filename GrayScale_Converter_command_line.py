import cv2
import numpy as np
import sys
import os
import argparse

def folder(args):
    file=str(args.inp)
    result_path=str(args.out)
    items=os.listdir(file)
    i=0
    for item in items:
        path=file+"\\" +item
        print (path)
        image = cv2.imread(path)
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converting image to gray
        new_path=result_path+"\\"+"image"+str(i)+".jpg"
        print (new_path)
        cv2.imwrite(new_path,gray_image)   # saves gray image to disk
        i=i+1
    cv2.imshow('color_image',image)
    cv2.imshow('gray_image',gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def file(args):
    path=str(args.inp)
    result_path=str(args.out)
    image = cv2.imread(path)
    gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converting image to gray
    new_path=result_path+"\\"+"image"+".jpg"
    print (new_path)
    cv2.imwrite(new_path,gray_image)   # saves gray image to disk
    cv2.imshow('color_image',image)
    cv2.imshow('gray_image',gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_folder = subparsers.add_parser('folder',help="Give the input path with images to be converted and output path to save the converted images")
parser_folder.add_argument('inp',type=str)
parser_folder.add_argument('out',type=str)
parser_folder.set_defaults(func=folder)

parser_file = subparsers.add_parser('file',help="Give the input path with the image name and the extension and output path to save the converted image")
parser_file.add_argument('inp',type=str)
parser_file.add_argument('out',type=str)
parser_file.set_defaults(func=file)

args = parser.parse_args()
args.func(args)
