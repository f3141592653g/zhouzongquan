# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

# pop3收邮件  smtp 发送邮件
#smtp.qq.com 我把邮件上传到stmp.qq.com 对方来这里拉取邮件
#qq 163 我把邮件上传到smtp.qq.com -->smtp.163.com --对方再去拉取邮件
#主题 发件人 收件人 正文 附件 抄送
import smtplib
from email.mime.text import MIMEText#专门发送正文
from email.mime.multipart import MIMEMultipart#发送多个部分
from email.mime.application import MIMEApplication#发送附件
from conf import read_path
#构造一个邮件体：正文 附件
msg=MIMEMultipart()
msg['Subject']='来自XXX的问候'#主题
msg['From']='XXXXX@qq.com'#发件人
msg['To']='YYYYYY@qq.com'#收件人
#构造邮件正文
part_text=MIMEText('邮件正文')#正文
msg.attach(part_text)#把正文加到邮件体里面去
#构建邮件附件
part_attach=MIMEApplication(open(read_path.report_path,'rb+').read())
part_attach.add_header('Content-Disposition', 'attachment',
filename='mengli.html')
msg.attach(part_attach)
#发送邮件 smtp
s=smtplib.SMTP_SSL('smtp.qq.com')#链接服务器