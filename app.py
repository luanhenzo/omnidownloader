from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)
app.config['DEBUG'] = True

uploads = r'C:/Users/luansinh0/Documents/Desenvolvimento/GitHub/omni_downloader/uploads/'


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if 'yt_url' in request.form:
            yt_url = request.form['yt_url']
            video = YouTube(yt_url)
            vs = video.streams.get_highest_resolution()
            vs.download(uploads)
            return send_file(uploads + vs.title + ".mp4", as_attachment=True)
        elif 'tt_url' in request.form:
            tt_url = request.form['tt_url']
            print(tt_url)
            return render_template('index.html')
        elif 'ttk_url' in request.form:
            ttk_url = request.form['ttk_url']
            print(ttk_url)
            return render_template('index.html')
        elif 'insta_url' in request.form:
            insta_url = request.form['insta_url']
            print(insta_url)
            return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()