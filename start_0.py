import ssl
import urllib.request
from urllib.request import urlopen
from PIL import Image
import os
ssl._create_default_https_context = ssl._create_unverified_context

class jpg_scraper:

    def __init__(self, html_ref="https://www.photo.rmn.fr/Package/2C6NU0ZFGW4V",file_ref="img",root_html="https://www.photo.rmn.fr"):

        self.html_ref = html_ref
        self.file_ref=file_ref
        self.root_html = root_html
        if not os.path.isdir(file_ref):
            os.makedirs(file_ref)

    def find_img(self,a):
        new_a=[]
        for a_e in a:
            for i in range(len(a_e)-4):
                if a_e[i:i+4]=='.jpg':
                    new_a.append(a_e[1:i+4])
        return new_a
        



    def dl_jpg(self):
        a = str(urllib.request.urlopen(self.html_ref).read())
        a0 = a.split(' src=')
        new_a = self.find_img(a0)
        
        for a in new_a:
            a_22= a.split("/")
            filename = a_22[-1]
            
            try:
                urllib.request.urlretrieve("{}{}".format(self.root_html,a), os.path.join(sel.file_ref,filename))
            except urllib.error.URLError:
                print("urlerror")
                print("{}{}".format(self.root_html,a))
        return(new_a)

#a = jpg_scraper()
#a.dl_jpg()