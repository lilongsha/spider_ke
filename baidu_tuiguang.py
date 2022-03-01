import chardet as chardet
from bs4 import BeautifulSoup
from urllib import request
import re


def process_tuiguang(url, search_key, file, file1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
        'Cookie': 'BIDUPSID=CB232A22CB07A941940465447484E00A; PSTM=1641614665; '
                  'BAIDUID=CB232A22CB07A9419348875C929279AF:FG=1; '
                  '__yjs_duid=1_64a904247bba971a2e431be4c0ea2fae1641622926192; BD_UPN=123253; '
                  'BDUSS=UxUDl'
                  '-enc3dlBqVkQtdGRzVHItMG9tNFJRSWdiSTRITUhqQjdZUUZOfkZwVEZpRVFBQUFBJCQAAAAAAAAAAAEAAAC3axh'
                  '-c2V40KE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMUYCmLFGApiS1; BDUSS_BFESS=UxUDl-enc3dlBqVkQtdGRzVHItMG9tNFJRSWdiSTRITUhqQjdZUUZOfkZwVEZpRVFBQUFBJCQAAAAAAAAAAAEAAAC3axh-c2V40KE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMUYCmLFGApiS1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-%3A; delPer=0; BD_CK_SAM=1; PSINO=1; BAIDUID_BFESS=CB232A22CB07A9419348875C929279AF:FG=1; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1645600980,1645602337,1645671670,1645688404; H_PS_PSSID=35837_34430_35105_31660_35767_35865_34584_35948_35956_26350_35881_22158; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1645691062; BA_HECTOR=2401212lak810k2lch1h1eg610r; sugstore=1; COOKIE_SESSION=114_0_8_8_2_12_0_0_8_6_0_7_0_0_0_0_1645690117_0_1645691188%7C9%23212_81_1645671881%7C9; H_PS_645EC=e389h4To9wadTJ%2BN5KkBsznF1y25bs3P2CjdlU%2FEWZUvpKXrnwG8RKOJl5Sbj45KajRx '
    }
    req = request.Request(url=url, headers=headers)
    # 访问页面，并获取从服务器的回应，如果是HTTPS？
    response = request.urlopen(req)
    # print(response.geturl() + '\n')
    # print(response.info())
    # print(response.getcode())

    # 读取页面
    html = response.read()
    # print(html)

    # 检测页面使用的编码
    # charset = chardet.detect(html)
    # print(charset)
    # 解码：获得易于阅读的网页源码
    # html = html.decode(charset['encoding']).encode('utf-8')
    get_tuiguang1(html=html, search_key=search_key, file=file, file1=file1)


def get_tuiguang(html, project_name, file):
    soup = BeautifulSoup(html)
    tags = soup.select("span .ec-tuiguang")
    flag = 0
    for tag in tags:
        if tag.text == '广告':
            flag = flag + 1
    text = project_name + '\t' + str(flag) + '\n'
    file.writelines(text)
    file.flush()


def process_a(s1, search_key, file):
    s1 = str(s1)
    s1 = re.sub('<a(\\ [a-z|A-Z|-]*\\=[a-z|A-Z|0-9|:|\.|/|_|\\?|\\|\\-|\\=|\\&|\\;|\\"|\\%|\\#]*)*>', '', s1)
    s1 = re.sub('</a>', '', s1)
    list = re.findall('<font color=\\"#CC0000\\">(\S*)</font>', s1)
    red_key = []
    for li in list:
        red_key.append(li)
    s1 = re.sub('<font color=\\"#CC0000\\">', '', s1)
    s1 = re.sub('</font>', '', s1)
    is_include_key = "不包含"
    is_include_key_flag = 0
    is_include_key1 = "不包含"
    is_include_key_flag1 = 0
    if s1.find(search_key) > 0:
        is_include_key = "包含"
        is_include_key_flag = 1
    search_key1 = re.sub("投稿", "", search_key);
    if s1.find(search_key1) > 0:
        is_include_key1 = "包含"
        is_include_key_flag1 = 1

    text = search_key + '\t' + str(red_key) + '\t' + is_include_key + '\t' + is_include_key1 + '\t' + s1 + '\n'
    file.writelines(text)

    return is_include_key_flag, is_include_key_flag1


def get_tuiguang1(html, search_key, file, file1):
    soup = BeautifulSoup(html)
    soup.prettify()
    # 根列表
    root_div = soup.select("div #content_left")
    # print(root_div)
    # 获取根div下的每一个广告div
    ad_divs = root_div[0].find_all("div", attrs={"class": "_2z1q32z"})
    is_include_search_key = 0
    is_include_search_key1 = 0
    for ad in ad_divs:
        containers = ad.find_all("div", attrs={"class": "wbrjf67"})
        for container in containers:
            if len(container["class"]) < 2:
                # print(container["class"])
                a_list = container.select('a')
                # print(a_list)
                for a in a_list:
                    i, j = process_a(a, search_key=search_key, file=file)
                    is_include_search_key = is_include_search_key + i
                    is_include_search_key1 = is_include_search_key1 + j
    text = str(search_key) + '\t' + str(is_include_search_key) + '\t' + str(is_include_search_key1) + '\n'
    file1.writelines(text)
    file1.flush()
    file.writelines(text)
    file.flush()

