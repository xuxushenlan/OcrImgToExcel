import base64, requests, os, time


APP_ID = '39962279'
API_KEY = 'CycG0xQcLiZruQcGiqLqbFBY'
SECRET_KEY = 'kDPANcIOuH2r3Ybs9uQnQ99Pt3CBK77k'


def get_excel(imgfile):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/table?access_token=24.d6aafa02f2c2b0b7305e7a7e19eb7d23.2592000.1698481377.282335-39962279"

    payload = {
        'image': imgfile,
        'return_excel': 'true'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    print(response.text)

    return response


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "http://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    response = requests.post(url, params=params, verify=False)
    print(response.json())
    return str(response.json().get("access_token"))


if __name__ == '__main__':
    imagelist = os.listdir('image')
    count = 0
    for imagefile in imagelist:
        filename = imagefile.split('.')[0]
        imgpath = f'image\\{imagefile}'
        print(imgpath)
        f = open(imgpath, 'rb')
        img = base64.b64encode(f.read())
        if count < 2:
            count += 1
        else:
            count = 1
            print('睡一分钟,再继续！')
            time.sleep(60)
        print('请求文件', filename)
        result = get_excel(img)
        with open(f'json\\{filename}.json', 'wb') as json:
            json.write(result.text.encode('utf8'))
        with open(f'excel\\{filename}.xlsx', 'wb') as excel:
            excel.write(base64.b64decode(result.json().get('excel_file')))
