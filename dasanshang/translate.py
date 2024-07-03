import json
import requests

API_KEY = "vh8mANKl1u8ZsIqHlV59triH"
SECRET_KEY = "luBpwRiePpPcuCZlrdAKhw5Z7VPpEnvP"
def translate(text_to_translate):
    try:
        access_token = get_access_token()
        if not access_token:
            print("Failed to get access_token")
            return

        url = "https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=" + access_token

        payload = json.dumps({
            "q": text_to_translate,  # 添加要翻译的文本
            "from": "zh",
            "to": "en"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            return(response.json()['result']['trans_result'][0]['dst'])
        else:
            print(f"Error: {response.status_code}, {response.text}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))