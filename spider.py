# -*- coding:utf-8 -*-
# import ssl
#
# import requests
# import parsel
# import csv
# import time
#
#
#
# def spider():
#     # 全局取消证书验证
#     ssl._create_default_https_context = ssl._create_unverified_context
#
#     # import urllib3  # 使用这个方法就OK了
#     # urllib3.disable_warnings()  # 忽略警告
#
#     date = time.strftime("%Y-%m-%d %H", time.localtime(time.time()))
#     # time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
#     # f = open('TikTokData_'+date+'_.csv', mode='a', encoding='utf-8-sig', newline='')
#     # csv_writer = csv.DictWriter(f, fieldnames=['标题', '播放量', '弹幕量', '作者', '综合得分', '视频地址'])
#     # csv_writer.writeheader()
#     url = 'https://www.TikTok.com/v/popular/rank/all?spm_id_from=333.851.b_7072696d61727950616765546162.3'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
#     }
#     response = requests.get(url=url, headers=headers)
#     selector = parsel.Selector(response.text)
#     lis = selector.css('.rank-list li')
#     dit = {}
#     show = [[], [], [], [], [], [],[]]
#     for li in lis:
#         title = li.css('.info a::text').get()  # 标题
#         bf_info = li.css('div.content > div.info > div.detail > span:nth-child(1)::text').get().strip()  # 播放量
#         dm_info = li.css('div.content > div.info > div.detail > span:nth-child(2)::text').get().strip()  # 弹幕量
#         bq_info = li.css('div.content > div.info > div.detail > a > span::text').get().strip()  # 作者
#         score = li.css('.pts div::text').get()  # 综合得分
#         page_url = li.css('.img a::attr(href)').get()  # 视频地址
#         dit = {
#             '标题': title,
#             '播放量': bf_info,
#             '弹幕量': dm_info,
#             '作者': bq_info,
#             '综合得分': score,
#             '视频地址': page_url,
#         }
#         if('万'in bf_info):
#             num = str(bf_info).strip('万')
#             bf_info = float(num)*1000
#         if ('万' in dm_info):
#             num = str(dm_info).strip('万')
#             dm_info = float(num) * 1000
#         show[0].append(title)
#         show[1].append(bf_info)
#         show[2].append(dm_info)
#         show[3].append(bq_info)
#         show[4].append(int(score))
#         show[5].append('http:'+page_url)
#         show[6].append(title+'\n'+'@['+bq_info+']')
#         # csv_writer.writerow(dit)
#         # print(dit)
#     # print('调用')
#     print(show)
#     return show
# spider()

import pandas
import pandas as pd
import requests
import time

def spider():
    url_dict = {
        '排名':'https://api.Bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    show = [[], [], [], [], [], [], []]
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

                show[0].append(data['title'])
                show[1].append(data['stat']['view'])
                show[2].append(data['stat']['danmaku'])
                show[3].append(data['owner']['name'])
                show[4].append(data['stat']['like'])
                show[5].append('https://www.douyin.com/video/' + data['bvid'])
                show[6].append('title'+'\n'+'@['+data['owner']['name']+']')

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
        # df.to_csv('TikTokData_'+day+'_.csv'.format(tab_name), index=False,encoding='utf_8_sig')
        # print('写入成功: ' + 'TikTokData_'+day+'.csv'.format(tab_name))
    return show
#
# show = spider()
# print(show)