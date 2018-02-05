import tensorflow as tf
from bicubic_interp import bicubic_interp_2d
import numpy as np

import time

n = 6
x = tf.constant(
  np.array(range(n*n), dtype=np.float32).reshape([1, n, n, 1]))

size = [3,3]

t0 = time.time()
y0 = bicubic_interp_2d(x, size)
y1 = bicubic_interp_2d(x, size, endpoint=True)
#print "Gen graph : ", time.time() - t0
z = tf.image.resize_bicubic(x, size)

sess = tf.Session()
x_ = sess.run(x)
t0 = time.time()
y0_ = sess.run(y0)
y1_ = sess.run(y1)
#print "Interp : ", time.time() - t0
z_ = sess.run(z)

print "input : [{}, {}]".format(n, n)
print x_[0,:,:,0]
print ""

print "tf.image.resize_bicubic : {}".format(size)
print z_[0,:,:,0]
print ""

print "bicubic_interp_2d : {}".format(size)
print y0_[0,:,:,0]
print ""

print "bicubic_interp_2d w/ endpoint=True : {}".format(size)
print y1_[0,:,:,0]
