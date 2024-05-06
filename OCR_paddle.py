# -*- coding:utf-8 -*-
import gc
import os
import time



date = time.strftime("%Y-%m-%d", time.localtime(time.time()))


# filename = './sentences/' + date + '.txt'


def delete_files(dir):
    for filename in os.listdir(dir):  # 获取文件夹内所有文件的文件名
        if filename.endswith('.flv'):  # 若文件名满足指定条件
            os.remove(os.path.join(dir, filename))  # 删除符合条件的文件
            #  print("{} deleted.".format(filename))           ##输出提示


def delete_files1(dir):
    for filename in os.listdir(dir):  # 获取文件夹内所有文件的文件名
        if filename.endswith('_.jpg'):  # 若文件名满足指定条件
            os.remove(os.path.join(dir, filename))  # 删除符合条件的文件
            #  print("{} deleted.".format(filename))           ##输出提示


def delete_files2(dir):
    for filename in os.listdir(dir):  # 获取文件夹内所有文件的文件名
        if filename.endswith('.jpg'):  # 若文件名满足指定条件
            os.remove(os.path.join(dir, filename))  # 删除符合条件的文件
            # print("{} deleted.".format(filename))           ##输出提示


def OCR(title):
    import paddlehub as hub
    import cv2
    filename = './sentences/' + date + '.txt'
    delete_files1('./img')
    ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")  # 加载移动端预训练模型

    # ocr = hub.Module(name="chinese_ocr_db_crnn_server") #服务器端可以加载大模型，效果更好

    def geturlPath():
        global ppa
        # 指定路径
        path = r'./img/'
        # 返回指定路径的文件夹名称
        dirs = os.listdir(path)
        # 循环遍历该目录下的照片
        for dir in dirs:
            # 拼接字符串
            ppa = path + dir
            # 判断是否为照片
            if not os.path.isdir(ppa):
                # 使用生成器循环输出
                yield ppa

    def test_img_path():
        paths = []
        for Path in geturlPath():
            paths.append(Path)
        return paths

    test_img_path = test_img_path()

    np_images = [cv2.imread(image_path) for image_path in test_img_path]  # 读取测试文件夹test.txt中的照片路径

    results = ocr.recognize_text(
        images=np_images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
        use_gpu=True,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
        output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
        visualization=False,  # 是否将识别结果保存为图片文件；
        box_thresh=0.5,  # 检测文本框置信度的阈值；
        text_thresh=0.5)  # 识别中文文本置信度的阈值；

    if os.path.exists(filename):  # True/False
        with open(filename, mode='a', encoding='utf-8') as f:
            f.write('\n')
            f.write(title)
        for result in results:
            data = result['data']
            save_path = result['save_path']
            for infomation in data:
                # print(infomation['text'], infomation['confidence'], infomation['text_box_position'])
                with open(filename, mode='a', encoding='utf-8') as f:
                    f.write(' ' + infomation['text'])
    else:
        with open(filename, mode='a') as f:
            f.write(title)
        for result in results:
            data = result['data']
            save_path = result['save_path']
            for infomation in data:
                # print(infomation['text'], infomation['confidence'], infomation['text_box_position'])
                with open(filename, mode='a', encoding='utf-8') as f:
                    f.write(' ' + infomation['text'])
                    # print(infomation['text'])
    # delete_files('./video')
    delete_files2('./img')
    gc.collect()



def OCR():
    import paddlehub as hub
    import cv2
    filename = './sentences/' + date + '.txt'
    delete_files1('./img')
    ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")  # 加载移动端预训练模型

    # ocr = hub.Module(name="chinese_ocr_db_crnn_server") #服务器端可以加载大模型，效果更好

    def geturlPath():
        global ppa
        # 指定路径
        path = r'./img/'
        # 返回指定路径的文件夹名称
        dirs = os.listdir(path)
        # 循环遍历该目录下的照片
        for dir in dirs:
            # 拼接字符串
            ppa = path + dir
            # 判断是否为照片
            if not os.path.isdir(ppa):
                # 使用生成器循环输出
                yield ppa

    def test_img_path():
        paths = []
        for Path in geturlPath():
            paths.append(Path)
        return paths

    test_img_path = test_img_path()

    np_images = [cv2.imread(image_path) for image_path in test_img_path]  # 读取测试文件夹test.txt中的照片路径

    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    results = ocr.recognize_text(
        images=np_images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
        use_gpu=True,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
        output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
        visualization=False,  # 是否将识别结果保存为图片文件；
        box_thresh=0.5,  # 检测文本框置信度的阈值；
        text_thresh=0.5)  # 识别中文文本置信度的阈值；

    if os.path.exists(filename):  # True/False
        with open(filename, mode='a', encoding='utf-8') as f:
            f.write('\n')
        for result in results:
            data = result['data']
            save_path = result['save_path']
            for infomation in data:
                # print(infomation['text'], infomation['confidence'], infomation['text_box_position'])
                with open(filename, mode='a', encoding='utf-8') as f:
                    f.write(' ' + infomation['text'])
    else:
        for result in results:
            data = result['data']
            save_path = result['save_path']
            for infomation in data:
                # print(infomation['text'], infomation['confidence'], infomation['text_box_position'])
                with open(filename, mode='a', encoding='utf-8') as f:
                    f.write(' ' + infomation['text'])
                    # print(infomation['text'])
    # delete_files('./video')
    delete_files2('./img')
    gc.collect()

# OCR()

# delete_files('./video')

# print('text:', text)


