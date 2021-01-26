import pyqrcode, png
from pyqrcode import QRCode 

content = input("Please enter your content: ")
  
# Generate QR code 
url = pyqrcode.create(content) 

# Ask for output format
while True:
    mode = input("Output format (svg/png): ")
    if(mode == "svg" or mode == "png"):
        break

# Ask for filename
while True:
    name = input("Name of the outputfile (without fileending): ")
    if(name != ""):
        break

# generate the png/svg
if(mode == 'svg'):
    url.svg(name + '.svg', scale = 10) 
elif(mode == 'png'):
    url.png(name + ".png", scale = 8)
    
print("Your QR-code has been generated sucessfully.")