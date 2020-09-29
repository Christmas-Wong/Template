# -*- coding: utf-8 -*-
'''
@Time    : 2020/9/29 22:31
@Author  : Fei Wang
@File    : test.py
@Software: PyCharm
@Description:
'''
from utils import log_utils
from utils import config_utils


if __name__ == "__main__":
    logger = log_utils.get_logger(None, None)
    logger.info("日志测试")
    config, config_dict = config_utils.get_config_from_json("D:\\file\pythonProject\\template_v1\\src\\configs\\test.json")
    logger.info(config.get("batch_size"))