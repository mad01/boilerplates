#!/usr/bin/env python
import boto.ses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def ses_send_html_mail(
    htmlFile="foobar.html",
    subject="example",
    send_from="from@example.com",
    send_to=["to@example.com"],
    aws_region="us-west-2"):

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = send_from
    message["To"] = send_to # can be string or list of strings

    html = open(htmlFile, 'r').read()
    attachment = MIMEText(html, 'html')
    message.attach(attachment)

    aws_connect = boto.ses.connect_to_region(aws_region)
    send_mail = aws_connect.send_raw_email(
            message.string(),
            source=message['From'],
            destinations=message['To']
    )
    return send_mail
