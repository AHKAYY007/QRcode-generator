import qrcode
import image

qr = qrcode.QRCode(
    version = 40,
    box_size = 10,
    border = 5
)

data = "https://yourtwitterhandle.com"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = 'black', back_color = '#808000')
img.save('yourtwitterhandle.png')