from time import sleep
import requests
import os
import re

Folderpath = os.getcwd()  # 当前目录


def request_code(url):  # 需要cookie
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39",
        "cookie":
        "buvid3=5E2E32BC-D8A7-4F78-A193-A7E8F29B33E4184979infoc; LIVE_BUVID=AUTO8316162371483785; rpdid=|(mmJmm)YRY0J'uYuYkJ)Yuu; CURRENT_BLACKGAP=0; buvid4=12CF0A1A-4BC7-AAC2-E164-32E01087988B40777-022031316-uDqRMFcPR8562Dnk/2VxYw%3D%3D; buvid_fp_plain=undefined; blackside_state=0; _uuid=A26C5EC8-8AF8-E3A4-7C2B-C9BED1F1B23412078infoc; nostalgia_conf=-1; is-2022-channel=1; CURRENT_QUALITY=80; PVID=2; b_lsid=BD1F1104E_181579A5B9C; bsource=search_bing; fingerprint=066cfe4316b6b2b5bfe74d39f4765ded; i-wanna-go-back=-1; b_ut=7; SESSDATA=d587a650%2C1670584208%2C9a44d%2A61; bili_jct=ea1d93a4767bed16d7d0b8165c5c1e6d; DedeUserID=1609755646; DedeUserID__ckMd5=93ad2e0d5cb5ed6a; sid=jcc6aqdk; innersign=1; CURRENT_FNVAL=4048; b_timer=%7B%22ffp%22%3A%7B%22333.851.fp.risk_5E2E32BC%22%3A%22181579A626E%22%2C%22333.42.fp.risk_5E2E32BC%22%3A%22181579A73FE%22%2C%22333.1007.fp.risk_5E2E32BC%22%3A%22181579A7DF1%22%2C%22333.788.fp.risk_5E2E32BC%22%3A%22181579B8F41%22%7D%7D; buvid_fp=066cfe4316b6b2b5bfe74d39f4765ded"
    }

    resp_code = requests.get(url=url, headers=headers)
    return resp_code.json()


def up_name(json):
    # uid对应名字
    upname = json["data"]["name"]
    return upname


if __name__ == '__main__':
    uid = [672346917, 672353429, 351609538, 672328094, 672342685, 703007996]
    for i in uid:
        url = "https://api.bilibili.com/x/space/acc/info?mid=" + str(
            i) + "&jsonp=jsonp"
        resp_src = request_code(url=url)
        if str(resp_src) != "{'code': -404, 'message': '啥都木有', 'ttl': 1}":
            # 正则提取后转化为字符串
            name = ''.join(re.findall(r"[^{'.*?'}]+", up_name(resp_src), re.S))
            with open(Folderpath + '\\uid.txt', 'a+', encoding='utf-8') as f:
                f.write("UP主名字：" + str(name) + "\t" + "B站UID：" + str(i) +
                        "\n")
            sleep(1.3)  # 时间太少会被封ip，大概1秒以上即可
        else:
            print("UID" + str(i) + "已注销或不存在")
            with open(Folderpath + '\\erroruid.txt', 'a+', encoding='utf-8') as f:
                f.write("UID" + str(i) + "已注销或不存在\n")
