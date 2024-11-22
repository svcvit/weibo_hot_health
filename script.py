import requests
import json

def send_request():
    response = requests.get(
        url="https://a.sina.cn/s/api/hotTopic/search",
        params={
            "plat": "health",
            "sort": "hot",
            "from": "wb",
        },
        headers={
            "Host": "a.sina.cn",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Weibo (iPhone16,2__weibo__14.10.3__iphone__os17.6_wbox_468_435_757866_h0i073u2by)",
            "Referer": "https://wboxservice.com/h0i073u2by/468/page-frame.html",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        },
    )
    data = response.json()
    
    # 将 JSON 数据美化后保存为 weibo_health.json 文件，确保中文正常显示
    with open('weibo_health.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # 使用 indent=4 进行美化

    return data

send_request()