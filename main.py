import os
import crypt
from flask import Flask, render_template, request, redirect, make_response
import time
from replit import db

app = Flask(__name__)
# start the app

@app.route('/')
def home():
  return "hi"
@app.route('/app')
def apprunner():
    return ""
# login page for the client sys for login


@app.route('/api/app/login')
def applogin():
    return render_template('applogin.html')


@app.route('/api/app/register')
def appregsiter():
    return render_template('appregister.html')


@app.route('/api/app/login/register/process', methods=['POST', 'GET'])
def registercookieapp():
    from replit import db
    user = request.form['username']
    users = request.form['password']
    resp = make_response(render_template('homeapps.html'))
    usernamec = crypt.caesarize(user)
    passwordc = crypt.caesarize(users)
    print(usernamec + "\n" + passwordc)
    resp.set_cookie('NA', usernamec)
    resp.set_cookie('PA', passwordc)
    usbda = "app" + usernamec
    db[usbda] = passwordc
    print(usernamec + "\n" + passwordc)
    return resp


@app.route('/api/app/login/process', methods=['POST', 'GET'])
def logincookieapp():
    user = request.form['username']
    users = request.form['password']
    resp = make_response(render_template('homeapps.html'))
    usernamec = crypt.caesarize(user)
    passwordc = crypt.caesarize(users)
    print(usernamec + "\n" + passwordc)
    resp.set_cookie('NA', usernamec)
    resp.set_cookie('PA', passwordc)

    return resp


@app.route('/api/app/', methods=['POST', 'GET'])
def databasecookie():
    from replit import db
    if 'NA' in request.cookies:
        username = request.cookies.get('NA')
        password = request.cookies.get("PA")
        us = crypt.uncaesarize(username)
        ps = crypt.uncaesarize(password)
        htmlcodeapp = "hi " + us + "<br> you're password is : " + ps
        hlapp = htmlcodeapp
        try:
            dya = db["app" + username]
            print(dya)
            if us == dya:
                htmlcodeapp = "hi " + us + "<br> you're password is : " + ps
                hlapp = htmlcodeapp
            else:
                htmlcodeapp = '''<meta http-equiv="refresh" content="1;url=https://devp.geoloup.com/api/app/login">'''
                hlapp = htmlcodeapp
        except:
            htmlcodeapp = '''<meta http-equiv="refresh" content="1;url=https://devp.geoloup.com/api/app/register">'''
            hlapp = htmlcodeapp
    elif 'PA' in request.cookies:
        username = request.cookies.get('NA')
        password = request.cookies.get("PA")
        us = crypt.uncaesarize(username)
        ps = crypt.uncaesarize(password)
        htmlcodeapp = "hi " + us + "<br> you're password is : " + ps
        hlapp = htmlcodeapp
        try:
            dya = db["app" + username]
            if us == dya:
                htmlcodeapp = "hi " + us + "<br> you're password is : " + ps
                hlapp = htmlcodeapp
            else:
                htmlcodeapp = '''<meta http-equiv="refresh" content="1;url=https://devp.geoloup.com/api/app/login">'''
                hlapp = htmlcodeapp
        except:
            htmlcodeapp = '''<meta http-equiv="refresh" content="1;url=https://devp.geoloup.com/api/app/register">'''
            hlapp = htmlcodeapp
    else:
        htmlcodeapp = '''<meta http-equiv="refresh" content="1;url=https://devp.geoloup.com/api/app/login">'''
        hlapp = htmlcodeapp
    return hlapp

# home page


@app.route('/')
def index():
    return render_template('formbox.html')
# Route for handling the login page logic


@app.route("/api/info")
def api():
    api_name = request.args.get("name")
    api_info = request.args.get('app')
    api_file = "/home/runner/python/compte/" + api_name
    file = open(api_file, "a")
    file.write("\n" + api_info)
    file.close()

# pixel art api

@app.route("/api/file")
def sys_file():
    print("hi")
    return render_template("homep.html")


@app.route("/api/redirect")
def redirects():
    link = request.args.get("link")
    links = "https://" + link
    print(links)
    return redirect(links)


@app.route('/homes', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    user = request.form['nm']
    users = request.form['nms']
    resp = make_response(render_template('homepage.html'))
    sd = crypt.caesarize(user)
    sg = crypt.caesarize(users)
    print(sd + "\n" + sg)
    resp.set_cookie('userID', sd)
    resp.set_cookie('userAD', sg)

    return resp

# game loding

@app.route("/home")
def loadhome():
    return render_template("home.html")


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'


@app.route('/documentation/iframe/codebox')
def codebox():
    userAD = request.cookies.get('userAD')
    print(userAD)
    return render_template("codebox.html")


@app.route('/documentation/iframe/')
def iframe():
    return render_template("iframe.html")


@app.route('/text/')
def text():
    return render_template("texteditor.html")


@app.route('/api/save/text/save', methods=['POST', 'GET'])
def saver():
    text = request.form['text']
    resp = make_response(render_template('redirect.html'))
    resp.set_cookie('userTEXT', text)
    print(text)
    return resp


@app.route('/api/text/save')
def Save():
    old = request.cookies.get("userTEXT")
    htmlcode = '''<html>
   <body>
      <style>
      .input,
      .textarea {
        border: 1px solid #ccc;
        font-family: inherit;
        font-size: inherit;
        padding: 1px 6px;
      }
      
      .input-wrap {
        position: relative;
      }
      .input-wrap .input {
        position: absolute;
        width: 100%;
        left: 0;
      }
      .width-machine {
        /*   Sort of a magic number to add extra space for number spinner */
        padding: 0 1rem;
      }
      
      .textarea {
        display: block;
        width: 1000%;
        height: 500px;
        overflow: hidden;
        resize: both;
        min-height: 40px;
        line-height: 20px;
      }
      
      .textarea[contenteditable]:empty::before {
        content: "text area";
        color: gray;
      }
      
      /* Just for demo */
      * {
        box-sizing: border-box;
      }
      body {
        font-family: "Heebo", sans-serif;
        max-width: 500px;
        margin: 0 auto;
        padding: 1rem;
        background-color: #3e8da8;
      }
      
      p strong {
        display: block;
      }
      h1 {
        border-bottom: 5px solid #9ccc65;
      }
      h2 {
        border-bottom: 2px solid #c5e1a5;
      }

      </style>
      <form action = "https://devp.geoloup.com/api/save/text/save" method = "POST">
        <p><input class="textarea" type = 'text' name = 'text' value=''' + old + '''/></p>
        <p><input type = 'submit' value = 'Save'/></p>
      </form>
      
   </body>
</html>'''
    print("d")
    return htmlcode


app.config.update(
    TESTING=True,
)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.run(host='0.0.0.0', port=8000)
