import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.linkedin.com/in/diya-ghosh-415307293/")
qr.make(fit=True)
Image=qr.make_image(fill_color="purple",back_color="White")
Image.save("Linkedin.png")







