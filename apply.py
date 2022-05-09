
# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=gUbgOW16Bwh8zp5RSTf13rdq&client_secret=N1gWoPgmImoNAPhb0XLVTVdPb4kqLGhS'
response = requests.get(host)
if response:
    print(response.json())