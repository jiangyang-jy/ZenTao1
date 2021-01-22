import requests


def login(s, user="19842314796", pwd="qQ123456"):
    url = "http://api.shopip.caisxs.com/user/login"
    """body为json格式"""
    body = {
        "device_type": "Android",
        "device_number": "3517033688244",
        "mobile": user,
        "code": pwd
    }
    r = s.post(url, json=body)
    token = r.json()["data"]["token"]
    h = {"token": token}
    s.headers.update(h)


if __name__ == '__main__':
    s = requests.Session()
    login(s, user="19842314796", pwd="qQ123456")

