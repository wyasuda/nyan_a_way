import csv
import os
import time
from PIL import Image
import urllib

Image.LOAD_TRUNCATED_IMAGES = True

all_tgt = ["cat", "dog", "person", "yard"]

for cur_tgt in all_tgt:
    print '\nClass : ' + str(cur_tgt) + '\n\n'
    f1 = open('/home/ubuntu/labels_'+str(cur_tgt)+'.csv', 'r')
    reader1 = csv.reader(f1)
    f2 = open('/home/ubuntu/2017_07/train/images.csv', 'r')
    reader2 = csv.reader(f2)
    confidence = 1.0
    if cur_tgt == 'yard':
        confidence = 0.9

    cnt = 0
    for row1 in reader1:

        if float(row1[3]) == confidence:

            for row2 in reader2:
                if row1[0] == row2[0]:
                    break
            print str(cnt)+' : '+row2[2]

            #load image
            urlimg = urllib.urlopen(row2[2])
            try:
                img = Image.open(urlimg)
            except:
                continue # skip if error happened

            fname = '/home/ubuntu/downloaded_images/'+str(cur_tgt)+'.'+str(cnt)+'.jpg'
            if urlimg.url.find('unavailable') == -1:
                if cur_tgt != 'yard':
                    #resize image
                    ratio = img.width / 227.0
                    if img.height < img.width:
                        ratio = img.height / 227.0
                    img_resize = img.resize((int(round(img.width/ratio)), int(round(img.height/ratio))))
                    img_resize.save(fname)
                else:
                    img.save(fname)

                cnt = cnt + 1
                if 10000 <= cnt:
                    break
    f1.close()
    f2.close()
