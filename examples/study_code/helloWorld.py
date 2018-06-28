#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-28 上午9:38
# @Author         : Tom.Lee
# @File           : helloWorld.py
# @Product        : PyCharm
# @Docs           : https://github.com/tensorflow/tensorflow#try-your-first-tensorflow-program
#                   http://www.tensorfly.cn/tfdoc/get_started/basic_usage.html
# @Source         : 

"""
使用 TensorFlow, 你必须明白 TensorFlow:
1.使用图 (graph) 来表示计算任务.
2.在被称之为 会话 (Session) 的上下文 (context) 中执行图.
3.使用 tensor 表示数据.
4.通过 变量 (Variable) 维护状态.
5.使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据


TensorFlow 是一个编程系统, 使用图来表示计算任务. 图中的节点被称之为 op (operation 的缩写).
一个 op 获得 0 个或多个 Tensor, 执行计算, 产生 0 个或多个 Tensor. 每个 Tensor 是一个类型化的多维数组.
例如, 你可以将一小组图像集表示为一个四维浮点数数组, 这四个维度分别是 [batch, height, width, channels].

一个 TensorFlow 图描述了计算的过程. 为了进行计算, 图必须在 会话 里被启动.
会话 将图的 op 分发到诸如 CPU 或 GPU 之类的 设备 上, 同时提供执行 op 的方法.
这些方法执行后, 将产生的 tensor 返回. 在 Python 语言中, 返回的 tensor 是 numpy ndarray 对象;
在 C 和 C++ 语言中, 返回的 tensor 是 tensorflow::Tensor 实例.


计算图
    TensorFlow 程序通常被组织成一个构建阶段和一个执行阶段. 在构建阶段, op 的执行步骤 被描述成一个图.
    在执行阶段, 使用会话执行执行图中的 op.
    例如, 通常在构建阶段创建一个图来表示和训练神经网络, 然后在执行阶段反复执行图中的训练 op.
    TensorFlow 支持 C, C++, Python 编程语言. 目前, TensorFlow 的 Python 库更加易用,
    它提供了大量的辅助函数来简化构建图的工作, 这些函数尚未被 C 和 C++ 库支持.
    三种语言的会话库 (session libraries) 是一致的.


构建图
    构建图的第一步, 是创建源 op (source op). 源 op 不需要任何输入, 例如 常量 (Constant).
    源 op 的输出被传递给其它 op 做运算.
    Python 库中, op 构造器的返回值代表被构造出的 op 的输出, 这些返回值可以传递给其它 op 构造器作为输入.
    TensorFlow Python 库有一个默认图 (default graph), op 构造器可以为其增加节点.
    这个默认图对 许多程序来说已经足够用了. 阅读 Graph 类 文档 来了解如何管理多个图.
"""

from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


if __name__ == '__main__':
    print("TensorFlow version: {}".format(tf.VERSION))

    hello = tf.constant('TensorFlow Say    : Hello World!')
    # sess = tf.Session()
    # sess.run(hello)
    # 'Hello, TensorFlow!'
    # a = tf.constant(10)
    # b = tf.constant(32)
    # sess.run(a + b)
    # sess.close()
    with tf.Session() as sess:
        print(sess.run(hello))
        a = tf.constant(10)
        b = tf.constant(32)
        print(sess.run(a + b))
