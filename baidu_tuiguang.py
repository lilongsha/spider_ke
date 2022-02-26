import chardet as chardet
from bs4 import BeautifulSoup
from urllib import request


def process_tuiguang(url, project_name, file):
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
    get_tuiguang(html=html, project_name=project_name, file=file)


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
