# -*- coding:utf-8 -*-

"""
自定义的api和工具库
"""

import requests
import os, datetime

from faceA import MyException


def getPicAnalysisResult(pngpath):  # 根据路径解析对应的图片
    """
    getPicAnalysisResult-> string
    pngpath 要解析的图片的路径
    """

    # 检验图片是否存在
    if not os.path.exists(pngpath):
        raise MyException.FileNotFounfdException()

    # 按照api文档调用face++的api，进行解析
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    key = "BFr8pippepx0jLQ9R6WK3HGdxxH2XE8w"
    secret = "IG0nuulyC93VY2GW-C9cZupZiuB3GaRg"

    # return_landmark。要求返回的结果中包括点的定位信息
    # return_attributes。定义返回的结果中要包含的参数序列
    data = {"api_key": key,
            "api_secret": secret,
            "return_landmark": "1",
            "return_attributes": "gender,age,smiling,eyestatus,emotion,ethnicity"}

    try:
        files = {"image_file": open(pngpath, "rb")}

        # 上传图片，获取解析结果
        response = requests.post(http_url, data=data, files=files)

        # 解析返回文本结果
        result = response.content.decode('utf-8')


    except Exception as e:
        print(e)
        return None

    return result


import logging
def geLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(".\myapp.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(name)s[line:%(lineno)d] %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


"""
@author:raymond
@file:MyUtils.py
@time:2018/1/1613:56
"""
