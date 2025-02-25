# -*- coding: utf-8 -*-

"""
配置类
@author : lcry
@time : 2022/9/15 12:35
"""
import os

# 以下参数根据自己的需要进行修改：
SYS_CONFIG = {
    # 获取到的header中t值,必须修改为自己的
    "header_t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzMTc5NTAsIm5iZiI6MTY2MzIxNTc1MCwiaWF0IjoxNjYzMjEzOTUwLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo3MjcwNzcxMSwiZGVidWciOiIiLCJsYW5nIjoiIn0._ZuMKxkr6z2utErtmxsw0jJ0tPOQEYHEkf2LYDksCdo",
    # 获取到的header中的user-agent值
    "header_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
    # 设定的完成耗时，单位s，默认5分钟
    "cost_time": 300,
    # 需要通关的次数，默认1
    "cycle_count": 1
}


def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
