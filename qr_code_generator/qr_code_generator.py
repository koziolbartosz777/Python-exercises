import qrcode

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\bkozi\\Desktop\\Nauka\\PYTHON BARTEK\\qr_code_generator" 

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)