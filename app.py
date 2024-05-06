import os

from flask import Flask, render_template, request, jsonify
# from smart_open.s3 import DEFAULT_HOST
import spider as info
# import rosetype_show
import spider_pro1 as spider_show
import spider as spider_show1
import result
from pypinyin import lazy_pinyin

app = Flask(__name__)

# 定时刷新
# from flask_apscheduler import APScheduler

emo = []
emotion_datas = []
data_li = []
x_data = []
x_data1 = []
data, emotion_categorys = [], []
centernumber, score, score2 = [], [], []
category, text_category, points = [], [], []
ProvinceName = None

class Config(object):  # 创建配置，用类
    # 任务列表
    JOBS = [
        {  # 第二个任务，每隔5S执行一次
            'id': 'job2',
            'func': 'app:method_test',  # 方法名
            # 'args': (1, 2),  # 入参
            'trigger': 'interval',  # interval表示循环任务
            'seconds': 86400,
        }
    ]


# i = 0
def delete_files(dir):
    for filename in os.listdir(dir):  # 获取文件夹内所有文件的文件名
        if filename.endswith('.flv'):  # 若文件名满足指定条件
            os.remove(os.path.join(dir, filename))  # 删除符合条件的文件
            # print("{} deleted.".format(filename))           ##输出提示


def attr(ProvinceName):
    # print('Tick2 !')
    global emo, data, emotion_categorys, centernumber, score, score2, category, text_category, points, LDA_UPs_value, LDA_title_value, LDA_theme_value
    from kmeans_中文 import kmeans_last
    from LDA import LDA, LDA_UPs, LDA_title
    from LDA_category import LDA_c
    LDA_theme_value = LDA(ProvinceName)
    LDA_theme_value = LDA_theme_value.values.tolist()
    LDA_UPs_value = LDA_UPs(ProvinceName)
    LDA_UPs_value = LDA_UPs_value.values.tolist()
    LDA_title_value = LDA_title(ProvinceName)
    LDA_title_value = LDA_title_value.values.tolist()

    # emo = result.emo()
    emo = [34, 64, 98, 0.3469, 0.6531]

    centernumber, score, score2 = result.ev(ProvinceName)
    category, text_category, points = kmeans_last(12, ProvinceName)
    LDA_c(ProvinceName)
    data, emotion_categorys = result.emo_category(ProvinceName)
    print('END !')


def method_test(ProvinceName):
    print('正在分析数据')
    import spider_pro
    # spider_pro.tiktok_scraper(ProvinceName)
    global x_data
    x_data = spider_show.tiktok_scraper(ProvinceName)
    import del_https
    del_https.delete(ProvinceName)
    print('spider success!')
    import deal_csv as deal
    deal.deal_csv(ProvinceName)
    print('attr complete!')
    attr(ProvinceName)
    print('clear!')
    delete_files('./video')


app.config.from_object(Config())  # 为实例化的flask引入配置

# scheduler = APScheduler()
# scheduler.init_app(app)
# scheduler.start()

flag = True


@app.route('/')
def init():
    global flag
    # 定时设置
    if (flag):
        flag = False
        return render_template("map.html")
    else:
        pass
        return render_template("505.html")

@app.route('/', methods=['POST'])
def handle_province():
    data = request.get_json()  # 获取 JSON 数据
    ProvinceName = data['province']
    pinyin_str = ''.join(lazy_pinyin(ProvinceName))
    ProvinceName = pinyin_str
    global pro, data_li
    pro = ProvinceName
    # data_li = spider_show.tiktok_scraper(pro)
    # 从 JSON 数据中获取省份名称
    print('省份：', ProvinceName)
    method_test(ProvinceName)

    return ProvinceName

@app.route('/index')
def Datacages_Homeindex():
    return render_template('Homeindex.html')

# @app.route('/index0')
# def Datacages_Homeindex0():
#     return render_template('Homeindex.html')


@app.route('/index1')
def index1():
    # x_data1 = spider_show1.spider()
    # print('x_data1:',x_data1)
    # x_data = spider_show.tiktok_scraper(pro)
    # print('x_data:', x_data)
    info = []
    dic = {}
    i = 0
    while i < len(x_data[0]):
        dic['标题'] = x_data[0][i]
        dic['作者'] = x_data[3][i]
        dic['播放量'] = x_data[1][i]
        dic['弹幕量'] = x_data[2][i]
        dic['综合评分'] = x_data[4][i]
        dic['视频地址'] = x_data[5][i]
        info.append(dic)
        dic = {}
        i += 1
    return render_template('index1.html', item=[], alarm={'alarm': len(x_data[0]), 'fault': len(set(x_data[3]))},
                           x_data=x_data, info=info)


# from kmeans_中文 import kmeans_last
# category, text_category, points = kmeans_last(12)
@app.route('/index2')
def index2():
    name = []
    num = []
    data = []
    # from kmeans_中文 import kmeans_last
    # category, text_category, points = kmeans_last(12)
    number = len(category)
    data.append(['score', 'amount', '类别'])
    for iterm in category:
        name.append(iterm[0])
        num.append(iterm[1])
        data.append([iterm[0], iterm[1], number])
        number -= 1
    # print(points)
    return render_template('index2.html', points=points, category_name=name, category_num=num
                           , number=len(name), sum=len(points), data=data)


@app.route('/index3')
def index3():
    # x_data = spider_show.tiktok_scraper(pro)
    info = []
    dic = {}
    i = 0
    while i < len(x_data[0]):
        dic['标题'] = x_data[0][i]
        dic['作者'] = x_data[3][i]
        info.append(dic)
        dic = {}
        i += 1
    return render_template('index3.html', alarm={'alarm': len(x_data[0]), 'fault': len(set(x_data[3]))}, x_data=x_data,
                           info=info, LDA_UPs=LDA_UPs_value, LDA_title=LDA_title_value, LDA_theme=LDA_theme_value)


@app.route('/index4')
def index4():
    return render_template('index4.html')


# emo = result.emo()
@app.route('/index5', methods=["GET", "POST"])
def index5():
    return render_template('index5.html', emotion=emo)


def sum(list):
    sums = 0
    for i in range(0, len(list)):
        sums += list[i]
    return sums


@app.route('/index6')
def index6():
    global data, negative_rateRates, positive_rateRates, emotion_categorys, emotion_datas
    # print('emotion_categorys', emotion_categorys)
    if len(data) != 0:
        data0 = list(data[0])
        # print(data0)
        data1 = list(data[1])
        # print(type(data1))
        data2 = list(data[2])
        data3 = list(data[3])
        data4 = list(data[4])
        data5 = list(data[5])
        positiveSum = sum(data2)
        negativeSum = sum(data1)
        numSum = sum(data3)
        # print('positiveSum',positiveSum)
        # print('negativeSum', negativeSum)
        # print('numSum', numSum)
        negative_rateRates = negativeSum / numSum
        positive_rateRates = positiveSum / numSum
        # print('data',data)
    else:
        data0 = []
        # print(data0)
        data1 = []
        # print(type(data1))
        data2 = []
        data3 = []
        data4 = []
        data5 = []
        positiveSum = 0
        negativeSum = 0
        numSum = 0
        negative_rateRates = 0
        positive_rateRates = 0
    i = 0
    dic = {}
    for iterm in emotion_categorys:
        i += 1
        dic['category'] = i
        dic['positive'] = iterm[1]
        dic['negative'] = iterm[0]
        dic['positive rate'] = iterm[4]
        dic['negative rate'] = iterm[3]
        emotion_datas.append(dic)
        dic = {}
    # print('emotion_datas', emotion_datas)
    # print(data)
    return render_template('index6.html', categorys=data0, negative=data1, positive=data2, num=data3,
                           negative_rate=data4,
                           positive_rate=data5, emotion_datas=emotion_datas, number=len(data0),
                           positiveSum=positiveSum, negativeSum=negativeSum, numSum=numSum,
                           negative_rateRate=round((negative_rateRates * 100), 4),
                           positive_rateRate=round((positive_rateRates * 100), 4)
                           )


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(e):
    return render_template('500.html'), 500


Tnumber = 20


# centernumber, score, score2 = result.ev()
@app.route('/param2')
def param2():
    global centernumber, score, score2
    # print(centernumber)
    # print(score)
    return render_template('param2.html', centernumber=centernumber, score=score, score2=score2, Tnumber=Tnumber)

