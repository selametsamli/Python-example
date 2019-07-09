import json
import smtplib

host = "smtp.gmail.com"
port = 587

with open("bilgiler.json") as read_file:
    data = read_file.read()

obj = json.loads(data)

username = obj['username']
password = obj['password']
from_email = username
to_list=["selamet96@gmail.com"]

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,"hello there this is email message")

email_conn.quit()

from smtplib import SMTP

email_conn2 = SMTP(host,port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username,password)
email_conn2.sendmail(from_email,to_list,"hello there this is email message")

email_conn2.quit()


from smtplib import SMTP,SMTPAuthenticationError,SMTPException

pass_wrong = SMTP(host,port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username,"yanlis")
    pass_wrong.sendmail(from_email,to_list,"hello there this is email message")
except SMTPAuthenticationError:
    print("cloud not login")
except:
    print("an eror occured")
email_conn2.quit()
