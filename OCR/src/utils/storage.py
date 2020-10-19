import os

import pandas as pd
from enum import Enum


class StorageRegion(Enum):
    LOCAL = "local"
    OSS = "oss"
    REQUEST = "request"


class BaseFileException(Enum):
    NOTSUPPORT = "不支持的文件类型"


class BaseFile(object):
    """
    基础文件
    处理文件类型为: TXT
    """

    def __init__(self, path, region="local"):
        self.path = path
        self.region = region
    
    def read(self):
        if self.region == StorageRegion.LOCAL.value:
            try:
                with open(self.path, "r") as fp:
                    return fp.read(), None
            except Exception as e:
                return None, e
        return None, BaseFileException.NOTSUPPORT.value
    
    def readlines(self):
        if self.region == StorageRegion.LOCAL.value:
            try:
                with open(self.path, "r") as fp:
                    return fp.readlines(), None
            except Exception as e:
                return None, e
        return None, BaseFileException.NOTSUPPORT.value

    def write(self, data: list):
        if self.region == StorageRegion.LOCAL.value:
            try:
                with open(self.path, "w") as fp:
                    fp.write("\n".join(data))
                return None
            except Exception as e:
                return e
        return BaseFileException.NOTSUPPORT.value


class ExcelFile(BaseFile):
    """
    excel 文件处理
    """

    def read2PD(self):
        """
        读取文件到 DdataFrame
        """
        if self.region == StorageRegion.LOCAL.value:
            try:
                return pd.read_excel(self.path), None
            except Exception as e:
                return None, e
        return None, BaseFileException.NOTSUPPORT.value

    def write(self, data: pd.DataFrame):
        """
        写入文件到 EXCEL
        """
        if self.region == StorageRegion.LOCAL.value:
            try:
                data.to_excel(self.path, encoding="utf-8", index=False)
                return None
            except Exception as e:
                return e
        return BaseFileException.NOTSUPPORT.value
