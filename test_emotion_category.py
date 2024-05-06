from __future__ import print_function

import gc
import json
import six
import paddlehub as hub


def emotion_category(texts):
    emotion_list = []
    # 加载senta模型
    senta = hub.Module(name="senta_bilstm")
    # 把要测试的短文本以str格式放到这个列表里
    test_text = texts
    # 指定模型输入
    input_dict = {"text": test_text}
    # 把数据喂给senta模型的文本分类函数
    results = senta.sentiment_classify(data=input_dict)
    # 遍历分析每个短文本
    for index, text in enumerate(test_text):
        results[index]["text"] = text
    for index, result in enumerate(results):
        if six.PY2:
            print(json.dumps(results[index], encoding="utf8", ensure_ascii=False))
        else:
            # print('text: {},    predict: {}'.format(results[index]['text'], results[index]['sentiment_key']))
            # print('text: {},    predict: {}'.format(results[index]['text'], results[index]['sentiment_key']))
            emotion_list.append(results[index]['sentiment_key'])

    negative = emotion_list.count('negative')
    positive = emotion_list.count('positive')
    num = len(emotion_list)
    negative_rate = float(negative / num)
    positive_rate = float(positive / num)
    emotion = [negative, positive, num, negative_rate, positive_rate]

    print(emotion)
    return emotion


def e_category():
    global emotion_categorys
    from kmeans_中文 import kmeans_last
    emotion_categorys = []
    category, text_category, points = kmeans_last(12)
    if len(text_category[0]) != 0:
        for texts in text_category:
            emotion = emotion_category(texts)
            emotion_categorys.append(emotion)
    else:
        pass
    print('emotion_categorys',emotion_categorys)
    return emotion_categorys

e_category()