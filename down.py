from flask import Flask, render_template, request
from pytube import YouTube
import urllib.request


app = Flask(__name__)


@app.route("/",methods =["GET", "POST"])
def down():
    if request.method == "POST":

        link = request.form.get("link")
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download()
        # data = link.read()
        print(stream.download())
        return "Download Completed"


    return render_template("main.html")



    # webUrl = urllib.request.urlopen('variable')
    # link = webUrl
    # video = YouTube(link)
    # stream = video.streams.get_highest_resolution()
    # stream.download()
    # data = webUrl.read()
    # print(stream.download())
    # return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)

