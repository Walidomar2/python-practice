####################################################################################
# Author: Walid Omar
# Brief: A Python script that uses the 'qrcode' library to generate a QR code for a
#        given text (usually a URL). The script defines a function, qrcodeGenerator,
#        which takes the input text, creates a QRCode object with specified parameters,
#        generates the QR code image, and saves it.
####################################################################################

import qrcode

def qrcodeGenerator(text):
    
    qr = qrcode.QRCode(
        version = 4,
        error_correction  = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,   
    )
    
    qr.add_data(text)
    qr.make(fit = True)
    
    img = qr.make_image(fill_color ="black", back_color="white")
    img.save("qrcodeimg.png")


userURL = input("Enter your url: ").strip()

if not isinstance(userURL, str):
    raise ValueError("userInput must be a string.")
    
else:
    qrcodeGenerator(userURL)





