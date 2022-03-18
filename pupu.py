import json
from time import strftime, sleep

import requests


def get_time():  # 获取时间
    url = 'https://j1.pupuapi.com/client/recommendation/product/net/group?store_id=831b632e-12bd-4c23-a6fd-a18749d8d508&product_id=0e4fee60-e839-4f15-84c9-d5820aa3608c&size=8'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    name = dict1["list"][0]['items'][0]['name']  # 商品名字
    price = str(int(dict1["list"][0]['items'][0]['price'] / 100))  # 折扣价
    print("-------------" + name + "-------------")
    try:  # 使程序终止时不会报错
        while (True):
            nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(nowTimeAndPrint)
            sleep(3)    #每隔3秒获取一次信息
    except:
            print("程序结束")


def push_info():
    url = 'https://j1.pupuapi.com/client/recommendation/product/net/group?store_id=831b632e-12bd-4c23-a6fd-a18749d8d508&product_id=0e4fee60-e839-4f15-84c9-d5820aa3608c&size=8'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=head)
    info1 = json.loads(res.text)
    #解析json数据
    name = info1["list"][0]["items"][0]["name"]   # 获取商品名字
    spec = info1["list"][0]['items'][0]['spec']  #  获取规格
    price = str(int(info1["list"][0]['items'][0]['price'] / 100))  # 获取折扣价
    market_price = str(int(info1["list"][0]['items'][0]['market_price'] / 100))  # 获取原价
    share_content = info1["list"][0]["items"][0]["sub_title"]  # 获取商品特点
    print("-------------商品：" + name + "-------------")
    print("规格：" + spec)
    print("原价：" + market_price)
    print("折扣价/原价：" + price + "/" + market_price)
    print("详细内容：" + share_content)



if __name__ == '__main__':
        push_info()    #调用商品信息
        print("\n")
        get_time()     #调用时间
