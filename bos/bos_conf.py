#!/usr/bin/env python
#coding=utf-8

# 从Python SDK导入BOS配置管理模块以及安全认证模块
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

# 从配置目录导入 AK & SK & HOST
import sys
sys.path.append("..")
from conf.conf import *

# 导入Python标准日志模块
import logging

# 设置日志文件的句柄和日志级别
logger = logging.getLogger('baidubce.services.bos.bosclient')
fh = logging.FileHandler("logs/bos.log")
fh.setLevel(logging.DEBUG)

# 设置日志文件输出的顺序、结构和内容
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

# 创建BceClientConfiguration
config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = bos_host)