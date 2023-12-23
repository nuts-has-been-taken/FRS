from datetime import datetime
import requests
import os

def recog_identity(user_id:str, identity:str, name:str, phone:str):
    if identity == "教授":
        msg=f"""\n身分辨識成功！\n使用者 [{name}] 教授已被確認\n歡迎進入實驗室"""
        return msg
    elif identity == "學生":
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        msg=f"""\n身分辨識成功！\n使用者 [{name}] 身分: 學生 已被確認\n簽到時間:{current_time}, 目前論文進度: 3/10\n快去工作!!"""
        return msg
    elif identity == "通緝犯":
        msg=f"""\nWARNING!!! 偵測到通緝犯\n [{name}]，請馬上執行逮捕，地點..."""
        return msg
    else:
        msg=f"""\n身分辨識成功！\n使用者 [{name}] \n身分: {identity} 已被確認"""
        return msg

def line_create_user(name, uuid):
    pass

def line_recog_unknown_user():
    msg="""\n檢測到未知用戶，請檢查攝像頭"""
    send_line_notify(msg)
    return

def line_recog_user(user_info:dict):
    user_id = user_info['id']
    name = user_info['name']
    phone = user_info['phone']
    identity = user_info['identity']
    msg = recog_identity(user_id, identity, name, phone)
    send_line_notify(msg)
    return

def send_line_notify(msg:str):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + os.getenv("LINE_NOTIFY_TOKEN")}
    payload = {"message":msg}
    r = requests.post(url, headers=headers, params=payload)
    return