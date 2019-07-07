# def jpeg_res(filename):
#     This function prints the resolution of the jpeg image file passed into it

# with open('C:\\Users\\Pratima Hake\\Desktop\\prati.jpg','rb') as img_file:
#
#
#         # height of image (in 2 bytes) is at 164th position C:\\Users\\Pratima Hake\\Desktop\\pgh.jpg'
#         img=img_file.seek(163)#(start,stop,end)
#         print(img)
#
#         # read the 2 bytes
#         a = img_file.read(2)
#         print(a)
#
#         #calculate height
#         height= (a[0]<< 8)+a[1]
#         print(height)
#
#         #next two byte
#         a=img_file.read(2)
#         print(a)
#
#         #calculate width b'\x03\x00'
#         width=(a[0]<<8)+a[1]
#         print(width)
# print("the resolution of the image is ",width, 'x', height)
# jpeg_res('C:\\Users\\Pratima Hake\\Desktop\\pgh.jpg')



def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)

       # calculate height
       height = (a[0] << 8) + a[1]

       # next 2 bytes is width
       a = img_file.read(2)

       # calculate width
       width = (a[0] << 8) + a[1]

   print("The resolution of the image is",width,"x",height)

jpeg_res("C:\\Users\\Pratima Hake\\Desktop\\prati.jpg")



