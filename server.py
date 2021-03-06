import os
from hashlib import sha256
from bottle import Bottle, request, static_file

page_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>Ahmet Furkan Kavraz</title>
        <meta charset="utf-8"/>
        <link href="./styling" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Staatliches&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Tangerine:700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Bangers&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Londrina+Solid&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Lalezar&display=swap" rel="stylesheet">
        <style>
            .main {
                text-align: left;
                margin: 0 auto;
                background-color:rgb(95, 95, 95);
                color: white;
                width: 1000px;
            }
        </style>
    </head>
    <body style="background-color:rgb(95, 95, 95);display: flex;color: white;">
        <img src="/mylogo" class="mylogo" alt="AFK Logo"/>
        <div class="main" >
            <p class="start" id="article" style="font-family: Tangerine; font-size: 20px;text-align:center;">This portfolio belongs to fictional character and prepared for university homework!</p>
            <div class="title" id="nav">
                <h2><a href="index.html" class="title1">Home</a></h2>
                <h2><a href="about.html" class="title2">About</a></h2>
                <h2><a href="projects.html" class="title3">Projects</a></h2>
            </div>
            
            <div class="entry" >
                <div class="entry1">
                    <div class="article1">
                    <p>Hello my Website.</p>
                    <p>I am developer for Military Industry. Also I am Swary's CEO.</p>
                    <p>We develop softwares about Military Equipment and Space Vehicles.</p>
                    </div>
                    <h3 class="contact">Contact Us</h3>
                    <span class="cont" id="nav1">
                    <a class="cont1" href="https://github.com/itu-itis-2019/assignment1-ituitis-kavraz19">Gıthub</a>
                    <a class="cont1" href="https://tr.linkedin.com/in/ahmet-furkan-kavraz-917944186">Lınkedın</a>
                    <a class="cont1" href="https://www.facebook.com/ahmetfurkankavraz">Facebook</a>
                    </span>
                </div>
                <img src="/myphoto" class="myphoto" alt="Ahmet Furkan Kavraz Photo"/> 
            </div>
            <hr/>
            <div class="form">
                <ul style= "color: white ;font-family: Staatliches; font-size: 25px ">
                    <li><a href="/" style= "color: white">Lıst IPs</a></li>
                    <li><a href="/reset" style= "color: white">Reset IPs</a></li>
                </ul>
                %(content)s
            </div>
            <hr/>
            <div class="form" >
                <ul style= "color: white ;font-family: Staatliches; font-size: 25px ">
                    <li><a href="/">Lıst Comments</a></li>
                    <li><a href="/comment">Add Comment</a></li>
                </ul>
                %(commentss)s
            </div>
            <br/>
            <hr/>
            <a href="source.html" class="source">Click for Source of this web site</a>
        </div>
         <img src="/mylogo" class="mylogo" alt="AFK Logo" />         
    </body>
</html>
"""

def styling():
    return static_file("./index.css", root = "./")
def about_html():
    return static_file("./about.html", root = "./")
def styling1():
    return static_file("./about.css", root = "./")
def projects_html():
    return static_file("./projects.html", root = "./")
def styling2():
    return static_file("./projects.css", root = "./")
def source_html():
    return static_file("./source.html", root = "./")
def styling3():
    return static_file("./source.css", root = "./")
def sfmslogo():
    return static_file("./images/sfmslogo.svg", root = "./")
def myphoto():
    return static_file("./images/myphoto.png", root = "./")
def aselsan():
    return static_file("./images/AselsanLogo.png", root = "./")
def cplus():
    return static_file("./images/C++logo.svg", root = "./")
def clogo():
    return static_file("./images/Clogo.svg", root = "./")
def csslogo():
    return static_file("./images/CSS.svg", root = "./")
def drone():
    return static_file("./images/dronestrikenew.png", root = "./")
def html():
    return static_file("./images/html.svg", root = "./")
def itulogo():
    return static_file("./images/itulogo.png", root = "./")
def javalogo():
    return static_file("./images/Javalogo.svg", root = "./")
def javascript():
    return static_file("./images/Javascript.svg", root = "./")
def microsoft():
    return static_file("./images/Microsoft_.NET_Framework_v4.5_logo.png", root = "./")
def python():
    return static_file("./images/python.png", root = "./")
def mylogo():
    return static_file("./images/mylogo.svg", root = "./")
    
a = []
c = []
listip = []
yorum = [{"name": "Ahmet Furkan Kavraz &emsp;", "comment": "Welcome to my websıte."},]
def farkli(listip):
    liste2=[]
    for l in range(len(listip)):
        değer = 0
        for k in range(len(listip)):
            if listip[l] == listip[k]:
                değer += 1
        liste2.append((listip[l],değer))
    liste3 = []
    for t in range(len(liste2)):
        if liste2[t] not in liste3:
            liste3.append(liste2[t])
    sonuc ="""<table style = "color: white ; font-family: Staatliches; font-size: 20px">
        <tr>
            <th>IP Adresses</th>
            <th>Counter</th>
        </tr>"""
    for p in range(len(liste3)):
        ip_adress = (liste3[p])[0]
        count = (liste3[p])[1]
        sonuc += "<tr><td>{}</td><td>{}</td></tr>".format(str(ip_adress),str(count))
    sonuc += """</table>"""
    return sonuc    


def show_ip():    
    listip.append(request.headers.get("X-Forwarded-For", "127.0.0.1"))
    content = """
      <table style = "color: white ; font-family: Staatliches; font-size: 20px">
      <tr>
        <th>Name &emsp; </th>
        <th>Comments</th>
      </tr>
    """
    index = 0
    for a in yorum:
        yorum_content = """
          <tr>
            <td>%(name)s</td>
            <td>%(comment)s</td>
          </tr>
        """ % {
            "name": a["name"],
            "comment": a["comment"],
            "index": index,
        }
        content += yorum_content
        index = index + 1
    content += "</table>"
    return page_template % {"content": farkli(listip),"commentss": content}

def hashing(sayi):
    sayi = sayi.encode()
    hashsayi = sha256(sayi).hexdigest()
    return hashsayi

def hashed():
    content = """   
        <form class = "form" method="POST" action="/resetcompleted" style = "color: white ; font-family: Staatliches; font-size: 20px">
            Password : <input type="text" name="password"/><br/>
            <input type="submit" value="Reset"/>
        </form>
    """
    return page_template % {"content": content, "commentss": ""}

myhash = "815797c172f415291f7ed117eea9a2279d6dac9a3f76444ce59e185877ed186b"
def reset():
    password = request.POST.get("password")
    password1 = hashing(password)
    if password1 == myhash:
        global listip
        listip = []
        content = "<p style = 'font-family:Staatliches; font-size: 18px; '>Reset successful.</p>"
        return page_template % {"content": content,"commentss":"" }
    else: 
        content = "<p style = 'font-family:Staatliches; font-size: 18px; '>Reset failed.</p>"
        return page_template % {"content": content,"commentss":"" }

def comment_page():
    content = """
      <form class = "form" method="POST" action="/comment2" accept-charset= "ISO-8859-9" style = "color: white ; font-family: Staatliches; font-size: 20px">
        <input type="radio" name="writename" value="0">Wrıte My Name<br />
        <input type="radio" name="writename" value="1">I wıll be anonymous<br/>
        Name &emsp;   : <input type="text" name="name"/><br/>
        Comment : <input type="text" name="comment"/><br/>
        <input type="submit" value="Submit"/>
      </form>
    """
    return page_template % {"commentss": content, "content": ""}

def comment2_page():
    name = request.POST.get("name")
    comment = request.POST.get("comment")
    writename = request.POST.get("writename")
    global yorum
    if writename == "0":
        yorum = yorum + [{"name": name,"comment": comment},]
        return comment_page()
    elif writename == "1":
        yorum = yorum + [{"name": "Anonymous","comment": comment},]
        return comment_page()
    else:
        yorum = yorum + [{"name": name,"comment": comment},]
        return comment_page()
        
def create_app():
    app = Bottle()
    app.route("/", "GET", show_ip)
    app.route("/index.html", "GET", show_ip)
    app.route("/reset", "GET", hashed)
    app.route("/resetcompleted", "POST", reset)
    app.route("/styling", "GET" , styling)
    app.route("/mylogo", "GET", mylogo)
    app.route("/about.html", "GET" , about_html)
    app.route("/styling1", "GET" , styling1)
    app.route("/projects.html", "GET" , projects_html)
    app.route("/styling2", "GET" , styling2)
    app.route("/source.html", "GET" , source_html)
    app.route("/styling3", "GET" , styling3)
    app.route("/comment", "GET", comment_page)
    app.route("/comment2", "POST", comment2_page)
    app.route("/aselsan", "GET", aselsan)
    app.route("/cplus", "GET", cplus)
    app.route("/clogo", "GET", clogo)
    app.route("/csslogo", "GET", csslogo)
    app.route("/drone", "GET", drone)
    app.route("/html", "GET", html)
    app.route("/itulogo", "GET", itulogo)
    app.route("/javalogo", "GET", javalogo)
    app.route("/javascript", "GET", javascript)
    app.route("/microsoft", "GET", microsoft)
    app.route("/python", "GET", python)
    app.route("/myphoto", "GET", myphoto)
    app.route("/sfmslogo", "GET", sfmslogo)
    return app


application = create_app()
application.run(host="127.0.0.1",reloader=True , port=int(os.environ.get("PORT", 8080)))