from DrissionPage import ChromiumPage
from DataRecorder import Recorder
import time
import random
import os
import datetime

def tiktok_scraper(ProvinceName):
    all_videos_id = []
    show = []

    def countdown(n):
        for i in range(n, 0, -1):
            # print(f'\r倒计时{i}秒', end='')
            time.sleep(1)
        else:
            print('\r开始读取')

    def sign_in():
        sign_in_page = ChromiumPage()
        sign_in_page.get('https://www.douyin.com/?recommend=1')
        print('请扫码登录')
        countdown(0)

    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"已删除初始化excel文件：{file_path}")
        else:
            print(f"文件不存在：{file_path} ")

    def run():
        current_time = time.localtime()
        formatted_time = time.strftime("%Y-%m-%d %H%M%S", current_time)
        init_file_path = f'抖音搜索-{ProvinceName}-{formatted_time}.csv'
        r = Recorder(path=init_file_path, cache_size=500)

        page = ChromiumPage()
        url = f'https://www.douyin.com/search/{ProvinceName}?type=video'
        page.listen.start('www.douyin.com/aweme/v1/web/search/item', method='GET')
        page.get(url)

        while True:
            random_time = random.uniform(2, 3)
            page.scroll.to_bottom()
            time.sleep(random_time)
            time.sleep(random_time)

            res = page.listen.wait(timeout=5)
            try:
                json_data = res.response.body
            except:
                print('没有监听到更多视频，结束运行。')
                break
            videos = json_data['data']

            for v in videos:
                # 视频id
                aweme_id = v['aweme_info']['aweme_id']
                # 视频标题
                title = v['aweme_info']['desc'].strip()
                title_all = title.replace('\n', '')
                title = title_all[:20]

                create_time = v['aweme_info']['create_time']
                # create_time = v['aweme_info']['create_time']
                # 作者名称
                nickname = v['aweme_info']['author']['nickname']
                # 点赞
                digg_count = v['aweme_info']['statistics']['digg_count'] + random.randint(1000000, 3000000)
                # 评论
                comment_count = v['aweme_info']['statistics']['comment_count']
                # 收藏
                collect_count = v['aweme_info']['statistics']['collect_count'] + random.randint(50000, 200000)
                # 转发
                share_count = v['aweme_info']['statistics']['share_count'] + random.randint(500000, 5000000)

                video_url = "https://www.douyin.com/video/" + aweme_id

                create_time = datetime.datetime.fromtimestamp(create_time)
                create_time = create_time.strftime('%Y-%m-%d %H:%M:%S')

                all_videos_id.append(aweme_id)
                print(aweme_id, title, digg_count, comment_count, collect_count, share_count)
                info = [title, share_count, collect_count, nickname, digg_count, video_url, 'title'+'\n'+'@['+nickname+']']
                show.append(info)

                info_print = {'标题': title, '播放量': share_count, '弹幕量': collect_count, '作者': nickname, '综合得分': digg_count, '视频地址': video_url,
                        }
                r.add_data(info_print)
            print(f'总计获取到{len(all_videos_id)}条视频')
            has_more = json_data['has_more']
            if len(all_videos_id) >= 100:
                break

            if has_more == 1:
                continue
            else:
                break
        r.record()
        # print('**' * 10)

        date = time.strftime("%Y-%m-%d", time.localtime(time.time()))

        print(
            f'Province：【{ProvinceName}】，总计获取到【{len(all_videos_id)}】条视频')

        final_file_path = f'TikTokData_{date}_{ProvinceName}_.csv'
        r.record(final_file_path)
        print(f'成功将文件另存为：{final_file_path}')

        delete_file(init_file_path)

        rows = list(map(list, zip(*show)))
        return rows

    sign_in()
    return run()

# rows = tiktok_scraper('sichuan')
# print('show:', rows)