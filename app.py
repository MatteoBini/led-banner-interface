from flask import Flask, render_template, url_for, request
from banner import Banner
app = Flask(__name__)


@app.route('/')
def index():
    url_for('static', filename='css/style.css')
    url_for('static', filename='js/script.js')
    return render_template('index.html')


@app.route('/api/banner-string', methods=['POST'])
def api():
    data = request.get_json()  # decode the binary data to dictionary

    banner = Banner()
    errors = banner.send(data["string"])

    if errors:
        print("<h1>There's been an error.</h1>")
        return

    return


if __name__ == '__main__':
    app.run()
