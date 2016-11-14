# -*- coding: utf-8 -*-
"""
Task 0000:
add a red coloured number on the top right hand corner of an image.
"""


from PIL import Image, ImageDraw, ImageFont
import os, sys
from random import randint

def draw_number(image,number):
    """put the number on the top right hand side of the image."""
    #make a blank image for the text, initialized to transparent text colour
    txt=Image.new('RGBA',im.size,(255,255,255,0))#mode, size, colour
    #get a font
    font_sz=int((min(im.size))/6)
    fnt=ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', font_sz)
    #get a drawing context
    d=ImageDraw.Draw(txt)
    #draw text
    d.text((im.size[0]-font_sz,10),number, font=fnt,fill=(255,0,0,128))#corrdinate, etxt, font, colour scheme
    return txt

if __name__=='__main__':
    for infile in sys.argv[1:]:
        #get an image
        im=Image.open(infile).convert('RGBA')
        #generate a random number between 0 to 9
        number=str(randint(0,9))
        #draw the number
        im_number=draw_number(im,number)
        #combine two images
        outimage=Image.alpha_composite(im, im_number)
        #save the outimage as a JPEG file
        outfile=os.path.splitext(infile)[0]+'_number'
        outimage.save(outfile,'JPEG')
        outimage.show()

    
