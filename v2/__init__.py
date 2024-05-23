import json
import os
import re

from v2.downloader import Downloader
from v2.api.req_aweme_post import ReqUserAwemePost
from v2.log import logger
import util


def save_author(author, path):
    util.create_dir_if_nt(path)
    with open(path, 'w') as f:
        f.write(json.dumps(author, ensure_ascii=False))
        f.close()


def save_meta_data(aweme_list):
    author = aweme_list[0].get('author')
    name = author.get('nickname')
    pwd = os.getcwd()

    save_author(author, os.path.join(pwd, 'lib', name, 'author.json'))

    for a in aweme_list:
        file_name = pwd + os.path.sep + 'lib' + os.path.sep + name + os.path.sep + f'aweme_list_{a.get('preview_title')}.json'
        util.create_dir_if_nt(file_name)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(a, ensure_ascii=False))
            f.close()


def save_user_video(url, base_dir='.data'):
    # 获取sec_user_id
    req = ReqUserAwemePost.from_url(url, base_dir=base_dir)
    if req is None:
        logger.error('实例化失败, 请检查url是否正确')
        return
    user_aweme_list = req.req_user_aweme_list()
    # 保存原始数据
    save_meta_data(user_aweme_list)
    # 保存视频
    req.downloader.save_video_aweme_list(user_aweme_list)


def main():
    # 获取用户输入
    print("请输入用户主页链接, "
          "比如: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz")
    while True:
        url = input('请在此后粘贴链接(输入q退出):')
        # 检查输入
        if url is None or len(url) == 0:
            print('输入为空, 请重新输入')
        elif url == 'q':
            print('退出')
            exit(0)
        elif re.match(r'https://www.douyin.com/user/[\w-]+', url) is None:
            print('请输入用户主页链接!, 请重新输入')
        else:
            break
    # todo 剔除参数
    print('输入正确, 开始下载', url)
    save_user_video(url)


def app_run(url, save_path):
    if re.match(r'https://www.douyin.com/user/[\w-]+', url) is None:
        print('请输入用户主页链接!, 请重新输入')
    print('输入正确, 开始下载', url)
    save_user_video(url, save_path)


if __name__ == '__main__':
    main()

# 鞠婧祎: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz
# 硝子: https://www.douyin.com/user/MS4wLjABAAAAz5T3wByqOvoXvrPbSQm1etY2ZVMXfazRgA07EjfmqHw?enter_from=personal_homepage&enter_method=follow_list&is_search=0&list_name=follow&nt=1&tab_name=follow_lish
# frontend_store: https://www.douyin.com/user/MS4wLjABAAAAgowPJlq0WZkQNORH7TZ6sdksuxlrEXzYHVyJvF8cvu9ksUTaFYsMc5AWe1T_zfJ0?is_search=0&list_name=follow&nt=0
# 森棋: https://www.douyin.com/user/MS4wLjABAAAAcW1HyIA_Ws6h0033Gxy3CQ0HWcwpw3ZghE_MpNE7u0g?is_search=0&list_name=follow&nt=0
# Nini: https://www.douyin.com/user/MS4wLjABAAAAuFW9aZJo8BBbcMg_p6Zydn0Nco_nxsiNI4-y8JoTnNx86Ey-Ia_JyWrf2gMdFedx
# 陈奕诺🍡: https://www.douyin.com/user/MS4wLjABAAAAkPSjLbWC9UuQAg6BmdtMxyWKJ_BRNcjfm658G8woY3D5rjsz5XuW20KgdpKQDh2P
# 渔总up: https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU
# 昱景影视: https://www.douyin.com/user/MS4wLjABAAAAgy0q1SoRu4RouWv803O8t-KtW7LVIc1dRWKTZgeHfO-6Q1-ZcZf6IiqkEBwd6tAi?vid=7320200627093572914
