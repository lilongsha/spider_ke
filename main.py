# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import urllib

from baidu_tuiguang import process_tuiguang

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keys = []
    file = open('out.txt', mode='a+')
    for key in keys:
        en_key = urllib.parse.quote(key)
        url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=CB232A279AF63626&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn' \
              '=baiduhome_pg&wd=' + en_key + '&rsv_spt=1&oq=' + urllib.parse.quote(en_key) + \
              '&rsv_pq=a80ecafe00053866&rsv_t=5f69mWz9v8uHH%2FZsVvtwft4pq%2FGlFPreH' \
              '%2B8tdLwVKS0gdbm9ztpWFrBIC5lXXtVTFgx1&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug1=1&rsv_sug7' \
              '=100&rsv_sug2=0&rsv_btype=t&inputT=4&rsv_sug4=1286&bs=' + en_key + \
              '&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=6&_cr1=43455 '
        process_tuiguang(url=url, project_name=key, file=file)
    file.close()
