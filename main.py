import requests

try:
    r = requests.get('https://go ogle.com')
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('error : ', e)