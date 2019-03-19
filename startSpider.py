from scrapy import cmdline

#
# import requests
# import time
# import threading
# from 91school import data5u
#
#
# # 获取代理IP的线程类
#
#
# class GetIpThread(threading.Thread):
#     def __init__(self, apiUrl, fetchSecond):
#         super(GetIpThread, self).__init__()
#         self.fetchSecond = fetchSecond
#         self.apiUrl = apiUrl
#
#     def run(self):
#         while True:
#             # 获取IP列表
#             res = requests.get(self.apiUrl).content.decode()
#             # 按照\n分割获取到的IP
#             data5u.IPPOOL = res.split('\n')
#             # 休眠
#             time.sleep(self.fetchSecond)
#
#
#
# if __name__ == "__main__":
#     # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
#     order = "8cf43b65ecaff2784a14c00006094c34"
#     # 获取IP的API接口
#     apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
#     # 获取IP时间间隔，建议为5秒
#     fetchSecond = 5
#     # 开始自动获取IP
#     GetIpThread(apiUrl, fetchSecond).start()

cmdline.execute("scrapy crawl 91good_school".split())
