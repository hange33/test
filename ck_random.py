#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
cron: 1 1 1 1 *
new Env('随机提取20个ck');
'''
import os


ck_list = os.environ['JD_COOKIE'].split('&')
len = len(ck_list)
print(f'共有{len}个ck')
i = 0
j = 0
while i != 56: # 前36个为前排固定位置
    if i >= 36:
        print(ck_list[i])
        j += 1
    i += 1   