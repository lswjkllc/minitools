import os
import time
import base64

from sanic import Blueprint, response
from sanic.response import html

from .common import response_json, ResponseCode
from ..config import  config
from ..utils import TencentCloudOCR, BaseFile

ocr = Blueprint('ocr', url_prefix='/ocr')

@ocr.get("/index")
async def index(request):
    template = request.app.template_env.get_template("web/index.html")
    html_content = template.render(name="ocr", endpoint=config["SERVER_ENDPOINT"])
    return html(html_content)

@ocr.post("/server")
async def server(request):
    req_data = request.form
    req_files = request.files
    ocr_file = req_files.get("image")
    if ocr_file is None:
        return response_json(ResponseCode.FAIL, "请求文件不存在")
    # 识别
    file_name = ocr_file.name
    file_type = ocr_file.type
    file_data = ocr_file.body
    bs64 = base64.b64encode(file_data)
    res, err = TencentCloudOCR.englishOCR(bs64)
    if err is not None:
        return response_json(ResponseCode.FAIL.value, f"OCR识别出错: { err }")
    return response_json(texts=res["data"])
