import tensorflow as tf
import tensorflow.keras as ks
from ._DarkConv import DarkConv


@ks.utils.register_keras_serializable(package='yolo')
class CSPConnect(ks.layers.Layer):

  def __init__(
      self,
      filters,
      filter_reduce=2,
      activation="mish",
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros',
      bias_regularizer=None,
      weight_decay=None,
      use_bn=True,
      use_sync_bn=False,
      norm_momentum=0.99,
      norm_epsilon=0.001,
      **kwargs):

    super().__init__(**kwargs)
    #layer params
    self._filters = filters
    self._filter_reduce = filter_reduce
    self._activation = activation

    #convoultion params
    self._kernel_initializer = kernel_initializer
    self._bias_initializer = bias_initializer
    self._weight_decay = weight_decay
    self._bias_regularizer = bias_regularizer
    self._use_bn = use_bn
    self._use_sync_bn = use_sync_bn
    self._norm_moment = norm_momentum
    self._norm_epsilon = norm_epsilon
    return

  def build(self, input_shape):
    self._conv1 = DarkConv(filters=self._filters // self._filter_reduce,
                           kernel_size=(1, 1),
                           strides=(1, 1),
                           kernel_initializer=self._kernel_initializer,
                           bias_initializer=self._bias_initializer,
                           bias_regularizer=self._bias_regularizer,
                           weight_decay=self._weight_decay,
                           use_bn=self._use_bn,
                           use_sync_bn=self._use_sync_bn,
                           norm_momentum=self._norm_moment,
                           norm_epsilon=self._norm_epsilon,
                           activation=self._activation)
    self._concat = ks.layers.Concatenate(axis=-1)
    self._conv2 = DarkConv(filters=self._filters,
                           kernel_size=(1, 1),
                           strides=(1, 1),
                           kernel_initializer=self._kernel_initializer,
                           bias_initializer=self._bias_initializer,
                           bias_regularizer=self._bias_regularizer,
                           weight_decay=self._weight_decay,
                           use_bn=self._use_bn,
                           use_sync_bn=self._use_sync_bn,
                           norm_momentum=self._norm_moment,
                           norm_epsilon=self._norm_epsilon,
                           activation=self._activation)
    return

  def call(self, inputs):
    x_prev, x_csp = inputs
    x = self._conv1(x_prev)
    x = self._concat([x, x_csp])
    x = self._conv2(x)
    return x
