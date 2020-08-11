from flask import Flask, render_template, request, url_for
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = "https://www.googleapis.com/youtube/v3/search"

        search_params = {
            'key': 'Your Youtube Api',
            'q': request.form.get('query'),
            'part': 'snippet',
            'maxResults': 8,
            'type': 'video',
        }

        r = requests.get(url, params=search_params).json()
        print(r)
        return render_template('yt.html', r=r)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
