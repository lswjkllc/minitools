import os
import sys

from sanic import Sanic
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .blueprints import ocr
from .utils import image2base64, TencentCloudOCR, BaseFile


app = Sanic(__name__)

app.register_blueprint(ocr)

@app.listener('before_server_start')
async def setup_db_redis(app, loop):
    workdir = os.getcwd()
    templates_path = os.path.join(workdir, 'src/templates')
    app.template_env = Environment(
        loader=FileSystemLoader(templates_path),
        autoescape=select_autoescape(['html', 'xml']),
        enable_async=False
    )

@app.middleware('response')
async def pop_temp_file(request, response):
    temp_file = request.headers.pop("temp_file", None)
    if temp_file is not None and os.path.exists(temp_file):
        os.remove(temp_file)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, workers=1)
    