import os

# 服务名称
NAME = "mini-ocr"
# 日志文件存放路径
DATA_PATH = "/tmp"                                # os.path.expanduser("~/data/app/ocr/data/")
# 上传文件子目录
UPLOAD_DIR = "uploads"
# 日志目录
LOG_PATH = "/tmp"                                 # os.path.expanduser("~/data/app/ocr/data/")
# 服务监听地址和端口
HOST = "0.0.0.0"
PORT = 8000
# 是否为调试模式
DEBUG = False
# 是否热加载代码
AUTO_RELOAD = False
# 是否记录访问日志
ACCESS_LOG = False
# 工作进程数
WORKERS = 1

# 服务地址
SERVER_ENDPOINT = "http://chanecho.com/tools"    # "http://localhost:8000"
