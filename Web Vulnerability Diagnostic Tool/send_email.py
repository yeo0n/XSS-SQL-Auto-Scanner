import os
import smtplib
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

file_list = os.listdir("./out")

email=input("전송받을 이메일 : ")
msg = MIMEMultipart()

msg['From'] = 'jme07136@gmail.com'
msg['To'] = email
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = Header(s='XSAS <웹 취약점 분석 도구>', charset='utf-8')
body = MIMEText('XSAS 웹 취약점 진단 보고서 첨부 파일 확인 부탁드립니다.', _charset='utf-8')
msg.attach(body)

files = list()
files.append("./out/"+file_list[0])

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
mailServer.login('jme07136@gmail.com', 'kqul ozyu bzcg iabl')  # 본인 계정과 앱 비밀번호 사용(구글 앱 비밀번호 사용해야함 안그러면 로그인이 안됐음)
mailServer.send_message(msg)
mailServer.quit()