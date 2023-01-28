"""
cron: 11 11 11 11 11
new Env('ck提取');
"""
import os


ck_list = os.environ['JD_COOKIE'].split('&')
len = len(ck_list)
print(f'共有{len}个ck')
for ck in ck_list:
    print(ck)
