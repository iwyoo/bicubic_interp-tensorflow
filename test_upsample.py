import tensorflow as tf
from bicubic_interp import bicubic_interp_2d
import numpy as np

import time

n = 3
x = tf.constant(
  np.array(range(n*n), dtype=np.float32).reshape([1, n, n, 1]))

size = [6,6]

t0 = time.time()
y0 = bicubic_interp_2d(x, size)
y1 = bicubic_interp_2d(x, size, endpoint=True)
z = tf.image.resize_bicubic(x, size)

sess = tf.Session()
x_ = sess.run(x)
t0 = time.time()
y0_ = sess.run(y0)
y1_ = sess.run(y1)
z_ = sess.run(z)

print "input : [3, 3]"
print x_[0,:,:,0]
print ""

print "tf.image.resize_bicubic : {}".format([6,6])
print z_[0,:,:,0]
print ""

print "bicubic_interp_2d : {}".format([6,6])
print y0_[0,:,:,0]
print ""

print "bicubic_interp_2d w/ endpoint=True : {}".format([6,6])
print y1_[0,:,:,0]
