# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from urllib import request
from bs4 import BeautifulSoup
import re
import os


# url 图片连接
# path 图片存储目录
def save_img(img_url, img_path):
    # print(img_url, img_path)
    img_url = str(img_url)
    img_name = img_url[img_url.rfind('/'):]
    filepath = img_path + img_name
    # print(filepath)
    request.urlretrieve(url=img_url, filename=filepath)
    return filepath


def process_html(html_context, project_name, all_task):
    soup = BeautifulSoup(html_context)
    # 通过标签获取图片分类对应id
    li_tags = soup.select('.photo-type > li')
    key = {}
    for li in li_tags:
        text = li.text
        text = re.sub('\s*', '', text)
        key[li.attrs['data-type']] = text

    # 通过data-type获取对应的img标签
    for k in key:
        div = soup.find_all('div', attrs={"data-type": k})
        ul = div[0].findNext('ul')
        img_tags = ul.select('img')
        img_urls = []
        for img in img_tags:
            img_url = str(img.attrs['src'])
            if img_url.find('!') > 0:
                img_url = img_url.split('!')[0]
            if img_url.find('?') > 0:
                img_url = img_url.split('?')[0]
            img_urls.append(img_url)
        key[k] = {key[k]: img_urls}

    # 遍历key下载图片
    for k in key:
        for t in key[k]:
            path = project_name + '/' + t
            if not os.path.exists(path):
                os.mkdir(path)
            for v in key[k][t]:
                # print(v)
                # print(t)
                all_task.append(pool.submit(save_img, img_url=v, img_path=path))
                # print(task.result())
                # save_img(img_url=v, img_path=path)


if __name__ == '__main__':
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=50)
    all_task = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
    }
    # 楼盘名称 楼盘链接
    projects = [['', '']]
    for project in projects:
        # 楼盘名称，用于创建目录
        name = project[0]
        # 楼盘图片页面url
        url = project[1]
        req = request.Request(url=url, headers=headers)
        response = request.urlopen(req)
        html = response.read()
        if not os.path.exists(name):
            os.mkdir(name)
        # thread = pool.submit(process_html, html_context=html, project_name=name, all_task=all_task)
        # all_task.append(pool.submit(process_html, html_context=html, project_name=name, all_task=all_task))
        process_html(html_context=html, project_name=name, all_task=all_task)

    print(len(all_task))
    wait(all_task)
    pool.shutdown()
    end = time.time()
    print('共耗时：', end - start)
