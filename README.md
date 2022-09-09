# Meme Generator

This fun project that outputs an image (of a dog) and quote (from a dog) in the form of a meme using separate text and image inputs.

## Command Line Interface module

There is a command line interface module that receives user inputs in the form of:

-- path - for the image path
-- body - for the quote body
-- author -- for the author name

The program then outputs a meme with the user-provided quote overlaying the user_provided image.

## Web interface module

The web interface module allows for two ways to generate memes:

Random Memes: There is a web interface module that generates random memes from a set of images in an image folder and a set of quotes in a quote folder.

User Generated Memes:  The web interface allows for users to enter the url of an image and user-entered quote body and author to generate a meme as well.

# Module Code and Structure

This module was written in python and calls the pdftotext application in the instance where a quote is being read from a pdf document.  

The command line interface module is run from the meme.py file
The web interface module is run from the app.py file

The requirements can be found in the requirements.txt documentation