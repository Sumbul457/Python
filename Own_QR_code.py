
import qrcode

data = "Tabassum Shamim" # can add website link, other links of any sorce you want

qr = qrcode.make(data)

qr.save("qrcode.png") # save the qr code as a .png file

print("QR code Generated Successfully!")