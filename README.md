# bicubic_interp-tensorflow
A differentiable bicubic interpolation module for TensorFlow

### Exmple : test.py
```tf.image.resize_bicubic``` doesn't support its gradients for speed issues.
It works different for boundary condition with ```tf.image.resize_bicubic```.
(It is intended and will not be fixed.). You can use "endpoint=False" if you want to the original boundary condition.

```
input : [3, 3]
[[ 0.  1.  2.]
 [ 3.  4.  5.]
 [ 6.  7.  8.]]

tf.image.resize_bicubic : [6, 6]
[[ 0.       0.40625  1.       1.59375  2.       2.09375]
 [ 1.21875  1.625    2.21875  2.8125   3.21875  3.3125 ]
 [ 3.       3.40625  4.       4.59375  5.       5.09375]
 [ 4.78125  5.1875   5.78125  6.375    6.78125  6.875  ]
 [ 6.       6.40625  7.       7.59375  8.       8.09375]
 [ 6.28125  6.6875   7.28125  7.875    8.28125  8.375  ]]

bicubic_interp_2d : [6, 6]
[[ 0.          0.32800001  0.78400004  1.21599996  1.67200005  2.        ]
 [ 0.98400003  1.31200004  1.76800013  2.20000005  2.65600014  2.98399997]
 [ 2.352       2.68000007  3.13600016  3.56799984  4.02400017  4.35200024]
 [ 3.648       3.97600007  4.43200016  4.86400032  5.31999969  5.64799976]
 [ 5.01599979  5.34400034  5.80000019  6.23200035  6.68799973  7.01599979]
 [ 6.          6.32800007  6.78399992  7.21600008  7.67199993  8.        ]]

bicubic_interp_2d w/ endpoint=False: [6, 6]
[[ 0.      0.4375  1.      1.5625  2.      2.0625]
 [ 1.3125  1.75    2.3125  2.875   3.3125  3.375 ]
 [ 3.      3.4375  4.      4.5625  5.      5.0625]
 [ 4.6875  5.125   5.6875  6.25    6.6875  6.75  ]
 [ 6.      6.4375  7.      7.5625  8.      8.0625]
 [ 6.1875  6.625   7.1875  7.75    8.1875  8.25  ]]
```

### Reference 
http://blog.demofox.org/2015/08/15/resizing-images-with-bicubic-interpolation/
