# -*- coding:utf-8 -*-
import gc

import jieba.analyse
import jieba.analyse as analyse
import jieba
import pandas as pd
from gensim import corpora, models, similarities
import gensim
import numpy as np
import matplotlib.pyplot as plt


def LDA_category(texts, number,ProvinceName):
    lines = []
    # 设置文件路径
    dir = "./"
    stop_words = "".join([dir, 'stopword.txt'])
    # 定义停用词
    # 不设置quoting，默认会去除英文双引号，只留下英文双引号内的内容，设置quoting = 3，会如实读取内容
    stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\n", names=['stopword'], encoding='utf-8')
    print(stopwords.head())
    stopwords = stopwords['stopword'].values

    lines = texts
    # 开始分词
    sentences = []
    for line in lines:
        try:
            segs = jieba.lcut(line)
            segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
            segs = list(filter(lambda x: x not in stopwords, segs))  # 去掉停用词
            sentences.append(segs)
        except Exception:
            print(line)
            continue

    # 构建词袋模型
    # print(sentences)
    # print(sentences[0])
    dictionary = corpora.Dictionary(sentences)
    # print(dictionary)
    # print(dictionary.token2id)
    # print(dictionary.dfs)

    # 词频向量
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    # lda模型，num_topics是主题的个数，这里定义了10个
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
    print("主题向量：\n", )
    # pprint(list(lda[corpus]))

    # 我们查一下第1号分类，其中最常出现的5个词是：
    # print(lda.print_topic(1, topn=5))

    # 我们打印所有10个主题，每个主题显示10个词
    for topic in lda.print_topics(num_topics=10, num_words=10):
        print(topic[1])

    # 显示中文matplotlib
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 在可视化部分，我们首先画出了10个主题的10个词的概率分布图
    num_show_term = 10  # 每个主题下显示几个词
    num_topics = 10
    for i, k in enumerate(range(num_topics)):
        ax = plt.subplot(10, 1, i + 1)
        # get_topic_terms 方法以（词汇 id，概率）的形式返回指定主题的重要词汇，调用方式为：get_topic_terms(topicid, topn=10)
        item_dis_all = lda.get_topic_terms(topicid=k)
        # print(item_dis_all)
        item_dis = np.array(item_dis_all[:num_show_term])
        ax.plot(range(num_show_term), item_dis[:, 1], 'g*')
        item_word_id = item_dis[:, 0].astype(np.int)
        word = [dictionary.id2token[i] for i in item_word_id]
        ax.set_ylabel(u"概率")
        for j in range(num_show_term):
            ax.text(j, item_dis[j, 1], word[j], bbox=dict(facecolor='green', alpha=0.1))
    plt.suptitle(u'TikTok热榜:Top10-topics&Probability of 10-keywords', fontsize=18)
    plt.savefig("./static/LDA/TikTok_theme_category" + str(number) + ".png", dpi=800,
                bbox_inches='tight')  # 解决图片不清晰，不完整的问题
    # plt.show()



def LDA_c(ProvinceName):
    from kmeans_中文 import kmeans_last
    category, text_category, points = kmeans_last(12, ProvinceName)
    num = len(text_category)
    if len(text_category[0]) != 0:
        for i in range(0, num):
            LDA_category(text_category[i], i + 1, ProvinceName)
    else:
        pass
    print('END!')
    gc.collect()
