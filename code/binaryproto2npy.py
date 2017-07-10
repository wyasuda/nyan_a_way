import caffe
import numpy as np

f_binaryproto = '/home/ubuntu/mean.binaryproto'
f_npy = '/home/ubuntu/mean.npy'

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( f_binaryproto, 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save( f_npy, out )
