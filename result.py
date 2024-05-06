


def emo(ProvinceName):
    import emotion_分析 as emotion0
    emotin = emotion0.emotion()
    return emotin

def ev(ProvinceName):
    from kmeans_中文 import test
    Tnumber = 20
    centernumber, score, score2 = test(Tnumber,ProvinceName)
    return centernumber, score, score2

def emo_category(ProvinceName):
    # from emotion_category import e_category
    # emotion_categorys = e_category()

    emotion_categorys = [[7, 11, 18, 0.3889, 0.6111], [1, 2, 3, 0.3333, 0.6666], [0, 3, 3, 0.0, 1.0], [2, 4, 6, 0.3333, 0.6666], [2, 15, 17, 0.1176, 0.8824], [0, 3, 3, 0.0, 1.0], [14, 17, 31, 0.4516, 0.5484], [3, 0, 3, 1.0, 0.0], [3, 8, 11, 0.2727, 0.7273], [0, 1, 1, 0.0, 1.0], [1, 0, 1, 1.0, 0.0], [1, 0, 1, 1.0, 0.0]]

    result = []
    positive = []
    negative = []
    num = []
    positive_rate = []
    negative_rate = []
    categorys = ['category'+str(i+1) for i in range(0,len(emotion_categorys))]
    result.append(categorys)
    for iterm in emotion_categorys:
        negative.append(iterm[0])
        positive.append(iterm[1])
        num.append(iterm[2])
        negative_rate.append(iterm[3])
        positive_rate.append(iterm[4])
    result.append(negative)
    result.append(positive)
    result.append(num)
    result.append(negative_rate)
    result.append(positive_rate)

    return result, emotion_categorys
