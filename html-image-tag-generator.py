from PIL import Image
from tkinter.filedialog import askopenfilename
import pyperclip

#This program assumes a simple folder structure in which the images are stored within a single subfolder stored in the same location as index.html
#Can be simply edited to your own path after pasting results, code is simple enough to fully edit it to your own path
#Example 
# "images/imagename.png" -GOOD
# "images/smallimages/imagename.png" -Will only copy "smallimages/imagename.png" to clipboard

#File user prompt
filename = askopenfilename()

#Open file
im = Image.open(filename)

#Split the path, only using the final two indexes (folder/filename.png)
filename = filename.split("/")

#If you need to go add an additional folder, simply add "{filename[-3]}/" at the start of the f-string. Repeat with additional indexes if necessary
string = f"{filename[-2]}/{filename[-1]}"

#Assess width and height
w, h = im.size

#Generate string
#Alt text will be blank
imageTag = f"<img src=\"{string}\" width=\"{w}\" height=\"{h}\" alt=\"\">"

#Copy to clipboard
pyperclip.copy(imageTag)
