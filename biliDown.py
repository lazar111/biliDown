import requests
import re

def downAndSave(url,header,retry_time=3):
    try:
        if retry_time == 0:
            raise Exception("")
        BV_number = re.findall('BV.{10}', url)[0]
        url_base = 'https://m.bilibili.com/video/'
        url = url_base+BV_number
        res = requests.get(url, headers=header)
        res.encoding = 'utf-8'
        if res.status_code != 200:
            downAndSave(url,header,retry_time-1)
        re1 = 'readyVideoUrl.*?\'(.*?)\\\''
        video_url = 'https:'+re.findall(re1,res.text)[0]

        res_video = requests.get(video_url,headers=header)
        video_name = re.findall('BV.{10}',url)[0]+'.mp4'
        with open(video_name, 'wb') as f:
            f.write(res_video.content)
            print("下载成功")
    except:
        if retry_time != 0:
            downAndSave(url,header,retry_time-1)
        else:
            print("下载失败")


def main():
    header_mobile = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}
    url = 'https://www.bilibili.com/video/BV1NT4y1E7ya?spm_id_from=333.5.b_686967685f656e65726779.3'
    downAndSave(url,header_mobile)

if __name__ == __name__:
    main()