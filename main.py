# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import urllib
import re

from baidu_tuiguang import process_tuiguang

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # keys = []
    # with open('key.txt') as key_txt:
    #     lines = key_txt.readlines()
    #
    # for line in lines:
    #     keys.append(line.replace('\n', ''))
    #
    # file = open('out.xlsx', mode='a+')
    # file1 = open('out1.xlsx', mode='a+')
    # for key in keys:
    #     en_key = urllib.parse.quote(key)
    #     url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=CB232A279AF63626&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn' \
    #           '=baiduhome_pg&wd=' + en_key + '&rsv_spt=1&oq=' + urllib.parse.quote(en_key) + \
    #           '&rsv_pq=a80ecafe00053866&rsv_t=5f69mWz9v8uHH%2FZsVvtwft4pq%2FGlFPreH' \
    #           '%2B8tdLwVKS0gdbm9ztpWFrBIC5lXXtVTFgx1&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug1=1&rsv_sug7' \
    #           '=100&rsv_sug2=0&rsv_btype=t&inputT=4&rsv_sug4=1286&bs=' + en_key + \
    #           '&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=6&_cr1=43455 '
    #     process_tuiguang(url=url, search_key=key, file=file, file1=file1)
    # file.close()
    # file1.close()

    s1 = '<a data-landurl="https://isite.baidu.com/site/wjzgvb9z/630679e0-c77d-4921-859e-d0c0625386d8#bd-chamu014?fid=rHRsrj04njc4P1b3rHRvrH0kP-tkPHnYg1D&amp;ch=4&amp;bfid=fbuFw0cKSFbK0na7t3n005370fDIBbbadx3-R6Y000K5T_x-Ns0000Y0wsD2_t1ftVik1Up34iHNOUMh1Up34Tpq126VES1QvU5vz8bV1rA4JI2edUe2EUxS1EZq5d7Z&amp;bd_vid=rHRsrj04njc4P1b3rHRvrH0kP-tkPHnYg17xnH0s" href="http://www.baidu.com/baidu.php?url=af0000KpxzUee8WytrS1fptt1Ku-xzPGuRonctQyepNZsthBe07HQG08AY64dnpKG02o_yxTO7gyllxm3rvQS8_cPENML_p2kTzJPkICRFF9ZVBryBa_9yRFePkN5eI9iygg9OZZbTsLj4bfJulhCFM8YJtJ7SRaFn5YUd8mxcODoEDo11QyrZHwzpv_CSOMXK6SESh2gzD_SI6lWchchc8RxIKI.DR_NR2Ar5Od66xAS6MzEukmDfwECF63nEjJSBOxssI5A1GtIlUnt5W3LuS1xbo1ePvqrXlzA1GzU8r1G8vxqaSe5jR1GsyNqMxgBmhOxOdk1uUrzQQjvxhoE31xEOlOChOx_ex1ulZUSUqSQO_pJO-d9JmerVSEDkoEsxg6_9OtZ3OyOOsywnSPjW7uu83SPhE4xxdEEu8lrrxOgYOqBzz1OsUEYrgC1O-W____Oe7MKZt_MQfodY5SFOUgO_3S5mOqOtEqZOuOBNNOer5WvxCmOugblxSQ1OAEtOYxerelrZuxOkN1XL_OvEEbHIO_GzXxS1YxWg4Oz5u88tx4ZySe-SWDkPSOOoWhzvIbyyZ_OPgxkhOxOdOwPSOuvOh1YrLtLetgOmdNS5w7SOuAGJIGHz3qis1f_Ihz1GLJ0.U1Yk0ZDq_t1ftVik1Up34fKspynqnfKsTv-MUWYYuhuBuH6vnHRknycYPvRknhF-nHFWnHfdujT4ujN9ufKY5Igq8XUPVoW-koLnJ0KGUHYkPHnY0ATqUvwlnfKdpHdBmy-bIfKspyfqnHn0mv-b5HnzPsKVIjY3PWc4g1DsnHIxnW0vn-tznjRkg1DsnH-xn1msnNt4nHT30AVG5H00TMfqPWmz0AFG5HDdr7tznjwxPH010AdW5HKxnHbkrHTdn1fzPNtkg1csPH7xnH0krNtsg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYznHDdPHc4PWRd0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVmhwbX0KGuAnqiDFK0ZKCIZbq0Zw9ThI-IjY1nNt1nHwxnWR0IZN15HnkrHc3nWfznHn1nW64rHTkPHb0ThNkIjYkPWfvnHDknjbkrjnv0ZPGujY3nvm1rjNWnj0snjD4rym30AP1UHYdwWDdfHm1wbFKPDw7rH640A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn7ts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqwbRsrR7anWPKnHnvnWu7wbfvnW7Arj0vnjRzf161nW61wRn3nRn1rjPARYIniRN2RYdP0Zwzmyw-5H00mhwGujdjfWc1nbDznbPanjIKrHfkrHnYrj6LPRn4nWbzP1-Kw6KEm1Yk0AFY5Hn0Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnHbWnznknH6LnWmYPjnYc1m3PH0WPW6dna3snj0snj0Wnin1c10WnHTWna3sPj0sn1bWni3snj0knj00XZPYIHY1rjnLn1bkPsKkgLmqna31n7tsQW0sg108njKxna3snNtsQW0vg108rjuxna3sn7tknW60mMPxTZFEuA-b5H00ThqGuhk9u1Y10APv5fKGTdqWTADqn0KWTjYs0AN1IjYs0APzm1YvrH01&amp;us=newvui&amp;xst=TjYznHDdPHc4PWRd0ynqwbRsrR7anWPKnHnvnWu7wbfvnW7Arj0vnjRzf161nW61wRn3nRn1rjPARYIniRN2RYdP0ycqfYczn1FKnWFjfW0LfHbYnHb1Pj63P1NjrHc4nWT4fRmKT1Y4PH03njbsnWbLrH64PHm4njDvg1Ddn1wxn07L5Igq8XUPVoW-koLnJ07k5U5nY5QR_Tvv8rRKIHY1rjnLn1bkPs7Y5HDvPjmknHDsrHcKUgDqn0cs0BYKmv6quhPxTAnKUZRqn07WUWdBmy-bIy9EUyNxTATKnH6krHbvrj6Lr0&amp;word=" target="_blank">'
    s1 = str(s1)
    s1 = re.sub('<a(\\ [a-z|A-Z|-]*\\=[a-z|A-Z|0-9|:|\.|/|_|\\?|\\|\\-|\\=|\\&|\\;|\\"|\\%|\\#]*)*>', '', s1)
    s1 = re.sub('</a>', '', s1)
    # list = re.findall('<font color=\\"#CC0000\\">(\S*)</font>', s1)
    # for li in list:
    #     print(li)
    # s1 = re.sub('<font color=\\"#CC0000\\">', '', s1)
    # s1 = re.sub('</font>', '', s1)
    # print(s1.find('发表啊'))
    print(s1)
    # ky = ['a', 'b']
    # print(ky)
