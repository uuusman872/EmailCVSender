import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser
from email.mime.base import MIMEBase
from email import encoders

file = "config.ini"
config = ConfigParser()
config.read(file)

EMAIL = config['Account']['EMAIL']
PASSWORD = config['Account']['PASSWORD']
TO = "uuusman872@gmail.com"
FILENAME = config['EmailData']['filename']
ATTACH_FILE_NAME = config['AtachFile']['file']


msg = MIMEMultipart('alternative')
msg['Subject'] = config['EmailData']['Subject']
msg['From'] = EMAIL
msg['To'] = config['Sender']['TO']


attach_file = open(ATTACH_FILE_NAME, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 
payload.add_header('Content-Decomposition', 'attachment', filename=ATTACH_FILE_NAME)



html = codecs.open(FILENAME, 'r', "utf-8").read()
part1 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(payload)


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL, PASSWORD)
server.sendmail(EMAIL, TO, msg.as_string())
server.quit()