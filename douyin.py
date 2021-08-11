"""下载抖音无水印的视频"""
import re
import requests

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
headers = {'User-Agent': useragent}


def dy_url_op(data):
    '''从data中找到url,返回str'''
    url=''
    url=re.findall(r'(https?://[^\s]+)',data)
    return url[0]

def get_real_url(url,headers):
    session = requests.Session()
    req = session.get(url , timeout = 5 , headers = headers)
    vid = req.url.split("/")[4].split("?")[0]
    videoInfo = session.get("https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + vid,
        timeout = 5 , headers = headers)
    playAddr = re.findall(r'https://aweme.snssdk.com/aweme[\S]*?"',videoInfo.text)[0][:-1]
    parsedAddr = playAddr.replace("/playwm/","/play/")
    return vid, parsedAddr, session

def downlowd_video(video_url):
    '''下载视频'''
    video_data=requests.get(video_url,headers=headers)
    with open('video.mp4','wb') as f:
        f.write(video_data.content)

print("请输入如下格式:\n8.94 mdN:/ 孙红雷的瓜保熟么？%扫黑风暴开播   https://v.douyin.com/eEPNXH4/ 復制佌鏈接，打开Dou音搜索，直接观看视频！")
data = input("请输入抖音视频链接：")
vid, parsedAddr, session = get_real_url(dy_url_op(data),headers)
downlowd_video(parsedAddr)
print("下载完成！")


    
