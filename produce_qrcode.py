import qrcode
from PIL import Image
 
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)
qr.add_data("超神二维码")
qr.make(fit=True)
img = qr.make_image()
img.save("qrcode1.png")