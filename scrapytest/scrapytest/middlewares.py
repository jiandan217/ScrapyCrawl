# -*- coding: utf-8 -*-
# �������ģ��
import random
# ����settings�ļ��е�IPPOOL
from .settings import IPPOOL
# ����ٷ��ĵ���Ӧ��HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOlS(HttpProxyMiddleware):
    # ��ʼ��
    def __init__(self, ip=''):
        self.ip = ip
    # ������
    def process_request(self, request, spider):
        # �����ѡ��һ��IP
        thisip = random.choice(IPPOOL)
        print("this ip is "+ thisip["ipaddr"])
        request.meta["proxy"] = "http://"+thisip["ipaddr"]