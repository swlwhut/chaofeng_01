# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import numpy
import numpy as np
import requests
import base64
import cv2

#'''
#图像清晰度增强
#'''


def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    with open('001.jpg', 'wb') as f:
        f.write(img_data)

    return img
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
# 二进制方式打开图片文件,括号里是文件路径
f = open('D:\\chaofeng\\img\\001.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.0258fd3535c2415c5999325f07644d78.2592000.1654497118.282335-26174790'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
#if response:
#    print(response.json())
#    img_code=response.json()
#    print(img_code)
#    base64_to_image(img_code)

text = response.text
jsonobj = json.loads(text)
img_code = jsonobj['image']
print(img_code)
base64_to_image(img_code)







# encoding:utf-8

