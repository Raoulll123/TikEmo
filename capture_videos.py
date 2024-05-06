# -*- coding:utf-8 -*-
import gc
import math
import os
import deal_水印 as deal
import cv2
import tensorflow as tf


# 两帧差法获得视频关键帧

# vedio path(可改)
# video_full_path = "./video/太倒霉啦！！！！！.flv"


def capture(video_full_path):
    cap = cv2.VideoCapture(video_full_path)  # 读取视频
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("[INFO] {} total frames in video".format(total))
    # print(cap.isOpened())
    frame_count = 1  # 帧序号
    success = True
    a = total/10000
    if math.floor(a)==0 or math.floor(a)==1 or math.floor(a)==2 or math.floor(a)==3 \
            or math.floor(a)==4 or math.floor(a)==5 or math.floor(a)==6 :
        timeF = 100  # 获取帧时间间隔
    else:
        timeF = math.floor(total/10000)*15
    # i = 0
    while success:
        success, frame = cap.read()  # 读取视频帧
        # print('Read a new frame: ', success)
        if frame is not None:
            if frame_count % timeF == 0:
                # name = './' + str(math.floor(frame_count / timeF))
                name = './img/' + str(math.floor(frame_count / timeF))
                cv2.imwrite(name + '_.jpg', frame)  # 命名帧
                deal.deal_suiyin(name + '_.jpg', name + '.jpg')
            frame_count = frame_count + 1  # 读取下一帧
            # i += 1
    cap.release()
    with tf.device('/cpu:0'):  # 运算设备CPU
        a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
        b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
    with tf.device('/gpu:1'):  # 运算设备GPU
        c = a + b
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
    sess.run(tf.global_variables_initializer())  # GPU运行
    print(sess.run(c))
    gc.collect()

# tensorflow测试
# hello = tf.constant('hello, world!')
# sess=tf.Session()
# print(sess.run(hello))
# capture(video_full_path)