#!/usr/bin/python
# -*- coding: utf-8 -*-
# from SimpleCV import Image, Color, Displayr
from SimpleCV import *
from sys import argv


if len(argv) > 1:
    imageSrcName = argv[1]
else:
    imageSrcName = "http://emtempo.com.br/"

img = Image(imageSrcName)

feats = img.findKeypoints()

feats.draw(color=Color.RED)

img.show()

roi = ROI(feats)

newImage = roi.crop()

newImage.save("crop_"+imageSrcName)

filename = raw_input()
