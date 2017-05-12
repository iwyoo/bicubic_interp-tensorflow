import tensorflow as tf
from bicubic_interp import bicubic_interp_2d
import numpy as np

x = tf.constant(
  np.array(range(9), dtype=np.float32).reshape([1, 3, 3, 1]))

size = [6,6]
y = bicubic_interp_2d(x, size)
z = tf.image.resize_bicubic(x, size)

sess = tf.Session()
x_ = sess.run(x)
y_ = sess.run(y)
z_ = sess.run(z)

print x_[0,:,:,0]
print y_[0,:,:,0]
print z_[0,:,:,0]
