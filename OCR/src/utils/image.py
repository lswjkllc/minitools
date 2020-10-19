import base64


def image2base64(path):
    """
    图片转base64
    """
    with open(path, "rb") as fp:
        return base64.b64encode(fp.read())
