#	QR Code Generator v1.5.3a
#
#	Created by Brandon Hines
#
#   January 18, 2022

import os
import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath

cwd = os.getcwd()

URL = input('What would you like your QR code to say or link to? Enter text or a web address.\n')
print('QR code will pooint to \'' + URL + '\'.\n')

# Gather QR code foreground color
qrFillColor = input("What would you like your QR code\'s foreground color to be? You can enter a color like blue or a hex code like #0000FF (including the hash.) The default is black.\n")
print('Foreground color is set to ' + qrFillColor + '.\n')

# Gather QR code background color
qrBackColor = input("What would you like your QR code\'s background color to be? You can enter a color like green or a hex code like #00FF00 (including the hash.) The default is white.\n")
print('Background color is set to ' + qrBackColor + '.\n')

# Gather QR code filename
filename = input("What would you like your QR code\'s filename to be? The file extension (.png) will be added automatically.\n")

# Sanitize QR code filename
print(f"\nIf needed, \"{filename}\" has been renamed to ensure compatability with most modern devices. {filename} -> {sanitize_filename(filename)}.png\n")

# Gather filepath
filepath = input('Where would you like to save your QR code? You are currently running this script from ' + cwd + '\n')

print('\nMaking QR code image...\n')

# Join filename + filepath
output = os.path.join(sanitize_filepath(filepath, platform='auto'), sanitize_filename(filename))

customQR = input('Would you like to add rounded corners to your QR code image?\n')
if customQR.lower() == "yes" or "y" or "yeah" or "yep" or "sure" or "hai" or "un":
    try:
        qrCode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)

        img = qrCode.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

        img.save(output + '.png')

    except ValueError:
        print('You did not enter a valid color or hex code. Please try again.\n')

else:
    qrCode = qrcode.QRCode(
        version=8,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    try:
        img = qrCode.make_image(fill_color=str(qrFillColor), back_color=str(qrBackColor))

        qrCode.add_data(str(URL))
        qrCode.make(fit=True)

        img.save(output + '.png')

    except ValueError:
        print('You did not enter a valid color or hex code. Please try again.\n')

# Print confirmation message and end script
print('Your QR code has been saved to ' + output + '.png.')
