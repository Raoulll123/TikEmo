# -*- coding:utf-8 -*-
import datetime
import gc
import os
import time

import jieba.analyse
import jieba.analyse as analyse
import jieba
import pandas as pd
from gensim import corpora, models, similarities
import gensim
import numpy as np
import matplotlib.pyplot as plt
# from pprint import pprint
import io
import sys
import urllib.request
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码
date = time.strftime("%Y-%m-%d", time.localtime(time.time()))


# # 获取今天（现在时间）
# today = datetime.datetime.today()
# # 昨天
# yesterday = today - datetime.timedelta(days=1)
# date = yesterday.strftime("%Y-%m-%d")


# 基于 LDA 主题模型进行关键词提取
# 语料是一个关于汽车的短文本，下面通过 Gensim 库完成基于 LDA 的关键字提取。
# 整个过程的步骤为：文件加载 -> jieba 分词 -> 去停用词 -> 构建词袋模型 -> LDA 模型训练 -> 结果可视化
def LDA(ProvinceName):
    # 设置文件路径
    dir = "./"
    stop_words = "".join([dir, 'stopword.txt'])
    # 定义停用词
    # 不设置quoting，默认会去除英文双引号，只留下英文双引号内的内容，设置quoting = 3，会如实读取内容
    stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\n", names=['stopword'], encoding='utf-8')
    print(stopwords.head())
    stopwords = stopwords['stopword'].values

    filename = "./sentences/" + date + '_' + ProvinceName +  ".txt"

    if os.path.exists(filename):
        # 加载语料
        lines = []
        with open(filename, "r", encoding='utf-8') as f:
            for line in f.readlines():
                lines.append(line.strip('\n'))  # 去掉列表中每一个元素的换行符


        # pprint(lines)
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


        # 我们打印所有10个主题，每个主题显示10个词
        for topic in lda.print_topics(num_topics=10, num_words=10):
            print(topic[1])

        topics_words = []  # 创建一个空的列表来存储每个主题的词和对应的概率
        for i, topic in enumerate(lda.print_topics(num_topics=10, num_words=10)):
            words_probs = topic[1].split(" + ")
            words_probs = [(word_prob.split("*")[1].strip('"'), float(word_prob.split("*")[0])) for word_prob in
                           words_probs]
            topics_words.extend(words_probs)
        # 显示中文matplotlib
        plt.rcParams['font.sans-serif'] = [u'SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # 在可视化部分，我们首先画出了九个主题的7个词的概率分布图
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
        plt.suptitle(u'TikTok Top topics & Probability', fontsize=18)
        plt.savefig("./static/LDA/TikTok_theme.png", dpi=800, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
        # plt.show()
        topics_words = pd.DataFrame(topics_words, columns=['word', 'probability'])
        print("topics_words:", topics_words)
        return topics_words
    else:
        pass
    gc.collect()





def LDA_UPs(ProvinceName):
    # 设置文件路径
    dir = "./"
    stop_words = "".join([dir, 'stopword.txt'])
    # 定义停用词
    # 不设置quoting，默认会去除英文双引号，只留下英文双引号内的内容，设置quoting = 3，会如实读取内容
    stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\n", names=['stopword'], encoding='utf-8')
    print(stopwords.head())
    stopwords = stopwords['stopword'].values

    date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    path = './TikTokData_' + date +  '_' + ProvinceName + '_.csv'

    # path = './TikTokData_'+'2021-03-30 06'+'_.csv'

    df = pd.read_csv(path, skiprows=0)
    UPs = list(df['作者'])
    # 加载语料
    lines = UPs

    # pprint(lines)
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

    topics_words = []  # 创建一个空的列表来存储每个主题的词和对应的概率
    for i, topic in enumerate(lda.print_topics(num_topics=10, num_words=10)):
        words_probs = topic[1].split(" + ")
        words_probs = [(word_prob.split("*")[1].strip('"'), float(word_prob.split("*")[0])) for word_prob in words_probs]
        topics_words.extend(words_probs)
    # 显示中文matplotlib
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 在可视化部分，我们首先画出了九个主题的7个词的概率分布图
    num_show_term = 10  # 每个主题下显示几个词
    num_topics = 10
    # for i, k in enumerate(range(num_topics)):
    #     ax = plt.subplot(10, 1, i + 1, label='ax'+str(i))
    #     # get_topic_terms 方法以（词汇 id，概率）的形式返回指定主题的重要词汇，调用方式为：get_topic_terms(topicid, topn=10)
    #     item_dis_all = lda.get_topic_terms(topicid=k)
    #     # print(item_dis_all)
    #     item_dis = np.array(item_dis_all[:num_show_term])
    #     ax.plot(range(num_show_term), item_dis[:, 1], 'g*')
    #     item_word_id = item_dis[:, 0].astype(np.int)
    #     word = [dictionary.id2token[i] for i in item_word_id]
    #     ax.set_ylabel(u"概率")
    #     for j in range(num_show_term):
    #         ax.text(j, item_dis[j, 1], word[j], bbox=dict(facecolor='green', alpha=0.1))
    # plt.suptitle(u'TikTok Top topics & Probability of influencer', fontsize=18)
    # plt.savefig("./static/LDA/TikTok_theme_UPs.png", dpi=800, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
    # plt.show()
    gc.collect()
    topics_words = pd.DataFrame(topics_words, columns=['word', 'probability'])
    print("topics_words:",topics_words)
    return topics_words

    # 设置文件路径
def LDA_title(ProvinceName):
    dir = "./"
    stop_words = "".join([dir, 'stopword.txt'])
    # 定义停用词
    # 不设置quoting，默认会去除英文双引号，只留下英文双引号内的内容，设置quoting = 3，会如实读取内容
    stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\n", names=['stopword'], encoding='utf-8')
    print(stopwords.head())
    stopwords = stopwords['stopword'].values

    date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    path = './TikTokData_' + date + '_' + ProvinceName + '_.csv'

    # path = './TikTokData_'+'2021-03-30 06'+'_.csv'

    df = pd.read_csv(path, skiprows=0)
    title = list(df['标题'])
    # 加载语料
    lines = title

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

    title_topics_words = []  # 创建一个空的列表来存储每个主题的词和对应的概率
    for i, topic in enumerate(lda.print_topics(num_topics=10, num_words=10)):
        words_probs = topic[1].split(" + ")
        words_probs = [(word_prob.split("*")[1].strip('"'), float(word_prob.split("*")[0])) for word_prob in words_probs]
        title_topics_words.extend(words_probs)

    # 显示中文matplotlib
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 在可视化部分，我们首先画出了九个主题的7个词的概率分布图
    num_show_term = 10  # 每个主题下显示几个词
    num_topics = 10
    # for i, k in enumerate(range(num_topics)):
    #     ax = plt.subplot(10, 1, i + 1)
    #     # get_topic_terms 方法以（词汇 id，概率）的形式返回指定主题的重要词汇，调用方式为：get_topic_terms(topicid, topn=10)
    #     item_dis_all = lda.get_topic_terms(topicid=k)
    #     # print(item_dis_all)
    #     item_dis = np.array(item_dis_all[:num_show_term])
    #     ax.plot(range(num_show_term), item_dis[:, 1], 'g*')
    #     item_word_id = item_dis[:, 0].astype(np.int)
    #     word = [dictionary.id2token[i] for i in item_word_id]
    #     ax.set_ylabel(u"概率")
    #     for j in range(num_show_term):
    #         ax.text(j, item_dis[j, 1], word[j], bbox=dict(facecolor='green', alpha=0.1))
    # plt.suptitle(u'TikTok Top topics & Probability of influencer', fontsize=18)
    # plt.savefig("./static/LDA/TikTok_theme_title.png", dpi=800, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
    # plt.show()
    gc.collect()
    title_topics_words = pd.DataFrame(title_topics_words, columns=['word', 'probability'])
    return title_topics_words
