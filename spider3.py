import pandas
import pandas as pd
import requests
import time

def spider(ProvinceName):
    url_dict = {
        '排名':'https://api.Bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }

    for i in url_dict.items():
        url = i[1]
        tab_name = i[0]
        title_list = []
        play_cnt_list = []  # 播放数
        danmu_cnt_list = []  # 弹幕数
        author_list = []
        video_url = []
        #coin_cnt_list = []  # 投币数
        like_cnt_list = []  # 点赞数
        #share_cnt_list = []  # 分享数
        #favorite_cnt_list = []  # 收藏数
        try:
            r = requests.get(url, headers=headers)
            print(r.status_code)
            json_data = r.json()
            list_data = json_data['data']['list']

            for data in list_data:
                title_list.append(data['title'])
                play_cnt_list.append(data['stat']['view'])
                danmu_cnt_list.append(data['stat']['danmaku'])
                author_list.append(data['owner']['name'])
                video_url.append('https://www.douyin.com/video/' + data['bvid'])
                #coin_cnt_list.append(data['stat']['coin']))
                like_cnt_list.append(data['stat']['like'])
                #share_cnt_list.append(data['stat']['share']
                #favorite_cnt_list.append(data['stat']['favorite'])

        except Exception as e:
            print("爬取失败:{}".format(str(e)))
        df = pd.DataFrame(
            {'标题': title_list,
             '播放量': play_cnt_list,
             '弹幕量': danmu_cnt_list,
             '作者': author_list,
             '综合得分': like_cnt_list,
             '视频地址': video_url,
             #'投币数': coin_cnt_list,
             #'分享数': share_cnt_list,
             #'收藏数': favorite_cnt_list,
             })
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        df.to_csv('TikTokData_'+day+'_'+ProvinceName+'_.csv'.format(tab_name), index=False,encoding='utf_8_sig')
    # print('写入成功: ' + 'TikTokData_'+day+'.csv'.format(tab_name))

spider('sichuan')