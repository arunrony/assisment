import os

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

print(os.environ)

app.config['MAIL_SERVER'] = 'cloud.cloudparas.in'  # os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = 465  # os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = 'me@arunbamniya.com'  # os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'sanzWFMENGCE3vi'  # os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False  # os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = True  # os.environ.get('MAIL_USE_SSL')

mail = Mail(app)


@app.route('/')
def hello_world():  # put application's code here
    msg = Message('Hello from the other side!', sender='me@arunbamniya.com', recipients=['meenagopal24@gmail.com'])
    msg.html = """<!DOCTYPE html>
    <html lang="en" xmlns="https://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta name="x-apple-disable-message-reformatting">
        <title></title>
        <!--[if mso]>
        <style>
            table {border-collapse:collapse;border-spacing:0;border:none;margin:0;}
            div, td {padding:0;}
            div {margin:0 !important;}
        </style>
        <noscript>
            <xml>
                <o:OfficeDocumentSettings>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
            </xml>
        </noscript>
        <![endif]-->
        <style>
            table, td, div, h1, p {
                font-family: Arial, sans-serif;
            }
        </style>
    </head>
    <body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
        <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">
            <table role="presentation" style="width:100%;border:none;border-spacing:0;">
        <tr>
            <td align="center" style="padding:0;">
               <h1>Hello Word</h1>
            </td>
        </tr>
    </table>
        </div>
    </body>
    </html>"""
    print(mail.send(msg))
    return "Message sent!"


if __name__ == '__main__':
    app.run()
