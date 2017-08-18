import glob
import cv2
import random

size_x = 227
size_y = 227

paths = [ano_path for ano_path in glob.glob('/home/ubuntu/downloaded_images/yard.*.jpg')]
cnt = 0
for file_path in paths:
    print str(cnt)+' : '+file_path
    in_img = cv2.imread(file_path)
    height, width = in_img.shape[:2]

    #crop image
    for i in range(10):
        rand_x = random.randint(0,width-size_x-1)
        rand_y = random.randint(0,height-size_y-1)
        #save image
        dst = in_img[rand_y:rand_y+size_y, rand_x:rand_x+size_x]
        fn = '/home/ubuntu/images/yard.%d.jpg' % (cnt+len(paths)*i)
        cv2.imwrite(fn, dst)

    cnt = cnt + 1
