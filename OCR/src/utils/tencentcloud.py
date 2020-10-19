import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

import ssl
# ssl._create_default_https_context = ssl.create_unverified_context


class TencentCloudOCR(object):
    _endpoint = "ocr.tencentcloudapi.com"
    _secretId = "AKIDg6Az3tar6CMKjtgUFl2BoRqKaWZUbflA"
    _secretKey = "MegT7YpreOxKSKgaGfd9AwUpwtl38qMg"

    @classmethod
    def englishOCR(cls, bs, action="ImageBase64", region="ap-shanghai"):
        bs = str(bs, encoding="utf-8")
        try: 
            cred = credential.Credential(cls._secretId, cls._secretKey) 
            httpProfile = HttpProfile()
            httpProfile.endpoint = cls._endpoint

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = ocr_client.OcrClient(cred, region, clientProfile) 

            req = models.EnglishOCRRequest()
            params = {
                action: bs
            }
            req.from_json_string(json.dumps(params))

            resp = client.EnglishOCR(req)
            texts = resp.TextDetections
            total = len(texts)
            actual = 0
            res = []
            for ele in texts:
                text = ele.DetectedText
                text = text.strip()
                if not text:
                    continue
                actual += 1
                res.append(text)
            return {
                "data": res,
                "total": total,
                "actual": actual
            }, None
        except Exception as e:
            return None, e
