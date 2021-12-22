import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
load_dotenv()
import os
import holiday
import xls2JPG

def send_enclosure():
    # 1.发件人、授权码，收件人信息
    # me = "526560086@qq.com"
    # pwd = 'uwsdaesunvmybjjh'
    # to = ['luosongtao0370@dingtalk.com', 'nfl3336@dingtalk.com', 'liumingjiang6633@dingtalk.com', 'rxz7665@dingtalk.com']
    # to = ['luosongtao0370@dingtalk.com', 'rxz7665@dingtalk.com']

    # 获取环境变量
    me = os.getenv("me")
    pwd = os.getenv("pwd")
    to = os.getenv("to").split(',')
    
    # 2.创建实例对象，设置主题等信息，
    msg = MIMEMultipart()
    msg["Subject"] = "本周请假人员情况，详见附件。"
    msg["From"] = me
    msg["To"] = ','.join(to)
    
    # 邮件内容(按每个部分)
    part1 = MIMEText("excel文件")
    msg.attach(part1)
    
    #添加图片附件
    part2 = MIMEApplication(open("请假情况.jpg", "rb").read())
    part2.add_header("Content-Disposition", "attachment", filename="meimei.jpg")
    msg.attach(part2)
    
    #添加附件
    part3 = MIMEApplication(open("请假情况.xlsx", "rb").read())
    part3.add_header("Content-Disposition", "attachment", filename="file.xlsx")
    msg.attach(part3)

    # 添加HTML
    with open("html.html", 'rb') as f:
        html = f.read()
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    #3.连接smtp服务器， 登录服务器并发送文本
    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP(smtp_server, 25)
    server.login(me, pwd)
    server.sendmail(me, to, msg.as_string()) #as_string() 把MIMEText变成一个str
    server.close()

if __name__ == '__main__':
    send_enclosure()