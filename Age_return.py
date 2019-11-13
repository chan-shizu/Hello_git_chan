from time import sleep
from datetime import datetime
import subprocess
import requests
import json
import requests
import json

#コマンドの実行
def exec(cmd):
    r = subprocess.check_output(cmd, shell = True)
    return r.decode("UTF8").strip()
    
#研究室のパソコンだと証明書(SSL)のエラーで動かない. ノートパソコンならうごいた.

def camera_to_azure():
    subscription_key = "d9d37d228bbb4daaabc51348ba0113c1"
    assert subscription_key

    face_api_url = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&recognitionModel=recognition_01&returnRecognitionModel=false HTTP/1.1'

#ローカルの画像をマイクロソフトに送る
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key':  subscription_key }
    fname = '1112.jpg'
    exec("fswebcam "+fname)
    image_url = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0/detect'
    data = open(fname, 'rb')
    img = data.read()
    
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,emotion'
    }

    response = requests.post(image_url, params=params, headers=headers, data=img,  verify=False)

    for i in range(len(response.json())):
    
        print(json.dumps(response.json()[i]["faceAttributes"]["age"]))
        #print(json.dumps(response.json()[i]["faceAttributes"]["emotion"]))

if __name__ == '__main__':
    for i in range(10):
        camera_to_azure()
        sleep(20)

