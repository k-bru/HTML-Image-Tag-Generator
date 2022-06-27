from PIL import Image
from tkinter.filedialog import askopenfilename
import pyperclip

#File user prompt
filename = askopenfilename()

#Open file
im = Image.open(filename)

#Assess width and height
w, h = im.size

#Generate string
imageTag = f"<img src=\"{filename}\" width=\"{w}\" height=\"{h}\" alt=\"\">"

#Copy to clipboard
pyperclip.copy(imageTag)