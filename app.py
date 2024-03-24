"""
配置信息
"""
import os
import logging.handlers

# 基础URL
BASE_URL = "http://127.0.0.1/index.php"

# 当前文件所属文件夹的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 该语句返回当前文件的上一层文件夹的绝对路径

def config_log():
    """日志配置方法"""

    # 实例化日志器
    logger = logging.getLogger()

    # 实例化处理器
    sh = logging.StreamHandler()  # 控制台
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=5,
                                                   backupCount=3)  # 文件

    # 实例化格式器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 将格式器添加给处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    # 将处理器添加给日志器
    logger.addHandler(sh)
    logger.addHandler(th)
