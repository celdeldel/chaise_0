import ssl
import urllib.request
from urllib.request import urlopen
from PIL import Image
import os
ssl._create_default_https_context = ssl._create_unverified_context


html_ref = "https://www.photo.rmn.fr/Package/2C6NU0ZFGW4V"
file_ref="img"
root_html = "https://www.photo.rmn.fr"
if not os.path.isdir(file_ref):
    os.makedirs(file_ref)

def find_img(a):
    new_a=[]
    for a_e in a:
        for i in range(len(a_e)-4):
            if a_e[i:i+4]=='.jpg':
                new_a.append(a_e[1:i+4])
    return new_a
        



def dl_jpg(adr_html=html_ref, file_root=file_ref, root_h=root_html):
    a = str(urllib.request.urlopen(adr_html).read())
    a0 = a.split(' src=')
    new_a = find_img(a0)
    
    for a in new_a:
        a_22= a.split("/")
        filename = a_22[-1]
        
        try:
            urllib.request.urlretrieve("{}{}".format(root_h,a), os.path.join(file_root,filename))
        except urllib.error.URLError:
            print("urlerror")
            print("{}{}".format(root_h,a))
    return(new_a)

new_a=dl_jpg()
print(new_a)



#a = str(urllib.request.urlopen(html_ref).read())
#print(type(a))
#a0=a.split(" src=")
#print(a0)