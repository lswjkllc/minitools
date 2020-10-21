from sanic.config import Config

from . import base as base_config

# 初始化配置
config = Config(load_env=False)
# 加载基础配置
config.from_object(base_config)
# 从环境变量中加载配置
config.load_environment_vars("MINI_OCR_")
