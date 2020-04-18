import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587

with open("bilgiler.json") as read_file:
    data = read_file.read()

obj = json.loads(data)

username = obj['username']
password = obj['password']
from_email = username
to_list=["selamet96@gmail.com"]
try:
    email_conn = smtplib.SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username,password)



    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello there!"
    the_msg["From"] = from_email
    #the_msg["To"] = to_list
    plain_txt = "Testing the message"

    html_txt = """\
    <html>
        <head> </head>
        <body>
            <p> Hey! <br>
                Email deneme  <b>message</b> Made by <a href="greatcode.co"> greatcode </a>

            </p>

        </body>
    </html>
    """


    part_1 = MIMEText(plain_txt,'plain')
    part_2 = MIMEText(html_txt,"html")

    the_msg.attach(part_1)
    the_msg.attach(part_2)


    email_conn.sendmail(from_email,to_list, the_msg.as_string())
    email_conn.quit()

except smtplib.SMTPException:
    print("mail gönderilemedi")
