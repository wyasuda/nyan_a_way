import numpy as np
import glob
import caffe
import cv2


caffe.set_mode_gpu()

# load ImageNet labels
label_file = '/home/ubuntu/synset_words.txt'
labels = np.loadtxt(label_file, str, delimiter='\t')

# Make classifier.
classifier = caffe.Classifier('/home/ubuntu/SqueezeNet/SqueezeNet_v1.1/deploy_v1.1.prototxt',
    '/home/ubuntu/SqueezeNet/SqueezeNet_v1.1/squeezenet_v1.1.caffemodel',
    image_dims=[227,227], mean=np.load('/home/ubuntu/ilsvrc_2012_mean.npy'),
    raw_scale=255.0,
    channel_swap=[2,1,0])

cat_cnt = 0
paths = [temp_path for temp_path in glob.glob("/home/ubuntu/nyan_a_way/google_cat_dog_img/cat.*.jpg")]　←①

for file_path in paths:
    print file_path
    cv_img = cv2.imread(file_path)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    cv_float = cv_img.astype(np.float32)
    cv_float /= 255.0
    predictions = classifier.predict([cv_float], False)
    out_label = labels[predictions[0].argmax()]
    print 'output label:', out_label
    if out_label.find('tabby cat') != -1 or \
    out_label.find('tiger cat') != -1 or \
    out_label.find('Persian cat') != -1 or \
    out_label.find('Siamese cat') != -1 or \
    out_label.find('Egyptian cat') != -1:
        cat_cnt = cat_cnt + 1
        print '********** this is cat! **********'
    print ""

print 'Total number of images:', len(paths)
print 'Number of detected cats:', cat_cnt
