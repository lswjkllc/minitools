import os
import time
import base64

from sanic import Blueprint, response
from sanic.response import html

from .common import response_json, ResponseCode
from ..utils import TencentCloudOCR, BaseFile

ocr = Blueprint('ocr', url_prefix='/ocr')

@ocr.get("/index")
async def index(request):
    template = request.app.template_env.get_template("web/index.html")
    html_content = template.render(name="ocr")
    return html(html_content)

@ocr.post("/server")
async def server(request):
    req_data = request.form
    req_files = request.files
    ocr_file = req_files.get("image")
    if ocr_file is None:
        return response_json(ResponseCode.FAIL.value, "请求文件不存在")
    # 识别
    file_name = ocr_file.name
    file_type = ocr_file.type
    file_data = ocr_file.body
    bs64 = base64.b64encode(file_data)
    res, err = TencentCloudOCR.englishOCR(bs64)
    if err is not None:
        return response_json(ResponseCode.FAIL.value, f"OCR识别出错: { err }")
    # 写临时文件
    meta_name, _ = os.path.splitext(file_name)
    cur_milli_st = int(time.time() * 1000)
    workdir = os.getcwd()
    file_path = os.path.join(workdir, f"data/temp/{ meta_name }_{ str(cur_milli_st) }.txt")
    # 将临时文件路径存入 request
    request.headers["temp_file"] = file_path
    # 写临时文件
    err = BaseFile(file_path).write(res["data"])
    if err is not None:
        return response_json(ResponseCode.FAIL.value, f"文件写入错误: { err }")

    return await response.file(file_path)
