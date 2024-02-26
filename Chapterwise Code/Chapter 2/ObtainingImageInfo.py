import exifread
f=open('D://Dataset//4.1.04.tiff','rb')
tags = exifread.process_file(f,details=False)
for x in tags:
    print(x.ljust(32),":",tags[x])




