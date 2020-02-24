#! -*- coding: utf-8 -*-
"""
Author: ZhenYuSha
Create type_time: 2020-2-24
Info: 定期向企业微信推送消息
"""
import requests, json
import datetime
import time

wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4baf3c3c-f3ea-4554-9a45-9fbbb2076269"    # 测试机器人1号
send_message = "测试：测试机器人1号………………………………！"


def get_current_time():
    """获取当前时间，当前时分秒"""
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hour = datetime.datetime.now().strftime("%H")
    mm = datetime.datetime.now().strftime("%M")
    ss = datetime.datetime.now().strftime("%S")
    return now_time, hour, mm, ss


def sleep_time(hour, m, sec):
    """返回总共秒数"""
    return hour * 3600 + m * 60 + sec


def send_msg(content):
    """艾特全部，并发送指定信息"""
    data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list":["@all"]}})
    r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)


def every_time_send_msg(interval_h=0, interval_m=1, interval_s=0, special_h="00", special_m="00", mode="special"):
    """每天指定时间发送指定消息"""

    # 设置自动执行间隔时间
    second = sleep_time(interval_h, interval_m, interval_s)
    # 死循环
    while 1 == 1:
        # 获取当前时间和当前时分秒
        c_now, c_h, c_m, c_s = get_current_time()
        print("当前时间：", c_now, c_h, c_m, c_s)
        if mode == "special":
            if c_h == special_h and c_m == special_m:
                # 执行
                print("正在发送...")
                send_msg(send_message)
        else:
            send_msg(send_message)
        print("每隔" + str(interval_h) + "小时" + str(interval_m) + "分" + str(interval_s) + "秒执行一次")
        # 延时
        time.sleep(second)


if __name__ == '__main__':
    every_time_send_msg(mode="no")