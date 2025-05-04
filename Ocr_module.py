import requests
import base64


class OCR:
    def __init__(self):
        self.ocr_key = "EesgWswSkMF9dPm6Ym9VzHnX"  # ocr的key
        self.secret_key = "rblveDGnhZi6J51YVVCPS5lM34XX2rn9"  # 密钥
        self.ocr_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"  # ocr网址

    def image_to_base64(self, image_path: str):  # 获取base64格式
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')

    def get_access_token(self) -> str:  # 获取令牌
        url = (f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"
               f"&client_id={self.ocr_key}&client_secret={self.secret_key}")
        response = requests.get(url)
        return response.json().get("access_token")

    def image_to_text(self, image_path: str) -> str:  # 图片转文字
        try:
            access_token = self.get_access_token()
            url = f"{self.ocr_url}?access_token={access_token}"
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {
                'image': self.image_to_base64(image_path)
            }
            response = requests.post(url, headers=headers, data=data)
            result = response.json()
            if 'words_result' in result:
                return '\n'.join([item['words'] for item in result['words_result']])
            return result
        except Exception as e:
            return f"请求发生异常：{str(e)}"
